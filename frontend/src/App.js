import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Header from './components/Header';
import PortfolioForm from './components/PortfolioForm';
import ResultsTable from './components/ResultsTable';
import ResultsChart from './components/ResultsChart';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import SuccessMessage from './components/SuccessMessage';

function App() {
  const [portfolioData, setPortfolioData] = useState({
    capacidad: 10000,
    objetos: [
      { nombre: 'A', peso: 2000, ganancia: 1500 },
      { nombre: 'B', peso: 4000, ganancia: 3500 },
      { nombre: 'C', peso: 5000, ganancia: 4000 },
      { nombre: 'D', peso: 3000, ganancia: 2500 }
    ]
  });

  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Función para optimizar el portafolio
  const optimizePortfolio = async () => {
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      const response = await axios.post('/optimizar', portfolioData);
      setResults(response.data);
      setSuccess('¡Optimización completada exitosamente!');
      
      // Limpiar mensaje de éxito después de 5 segundos
      setTimeout(() => setSuccess(null), 5000);
    } catch (err) {
      console.error('Error en la optimización:', err);
      
      if (err.response?.data?.error) {
        setError(err.response.data.error);
      } else if (err.response?.data?.detail) {
        setError(err.response.data.detail);
      } else {
        setError('Error al conectar con el servidor. Verifica que el backend esté ejecutándose.');
      }
    } finally {
      setLoading(false);
    }
  };

  // Función para ejecutar el ejemplo predefinido
  const runExample = async () => {
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      const response = await axios.post('/optimizar/ejemplo');
      setResults(response.data);
      setSuccess('Ejemplo ejecutado exitosamente');
      
      setTimeout(() => setSuccess(null), 5000);
    } catch (err) {
      console.error('Error en el ejemplo:', err);
      setError('Error al ejecutar el ejemplo');
    } finally {
      setLoading(false);
    }
  };

  // Función para limpiar el formulario
  const clearForm = () => {
    setPortfolioData({
      capacidad: 10000,
      objetos: [
        { nombre: 'A', peso: 2000, ganancia: 1500 },
        { nombre: 'B', peso: 4000, ganancia: 3500 },
        { nombre: 'C', peso: 5000, ganancia: 4000 },
        { nombre: 'D', peso: 3000, ganancia: 2500 }
      ]
    });
    setResults(null);
    setError(null);
    setSuccess(null);
  };

  // Función para actualizar los datos del portafolio
  const updatePortfolioData = (newData) => {
    setPortfolioData(newData);
  };

  // Función para cerrar mensajes
  const closeMessage = (type) => {
    if (type === 'error') setError(null);
    if (type === 'success') setSuccess(null);
  };

  return (
    <div className="App">
      <Header />
      
      <main className="container">
        {/* Mensajes de estado */}
        {error && (
          <ErrorMessage 
            message={error} 
            onClose={() => closeMessage('error')} 
          />
        )}
        
        {success && (
          <SuccessMessage 
            message={success} 
            onClose={() => closeMessage('success')} 
          />
        )}

        {/* Formulario principal */}
        <section className="form-section">
          <PortfolioForm
            portfolioData={portfolioData}
            onUpdate={updatePortfolioData}
            onSubmit={optimizePortfolio}
            onClear={clearForm}
            onExample={runExample}
            disabled={loading}
          />
        </section>

        {/* Spinner de carga */}
        {loading && <LoadingSpinner />}

        {/* Resultados */}
        {results && !loading && (
          <section className="results-section">
            <h2 className="section-title">Resultados de la Optimización</h2>
            
            <div className="results-grid">
              {/* Tabla de resultados */}
              <div className="results-table-container">
                <ResultsTable 
                  originalData={portfolioData.objetos}
                  results={results}
                  capacidad={portfolioData.capacidad}
                />
              </div>

              {/* Gráfico de resultados */}
              <div className="results-chart-container">
                <ResultsChart 
                  originalData={portfolioData.objetos}
                  results={results}
                  capacidad={portfolioData.capacidad}
                />
              </div>
            </div>

            {/* Resumen de resultados */}
            <div className="results-summary">
              <div className="summary-card">
                <h3>Proyectos Seleccionados</h3>
                <div className="selected-projects">
                  {results.seleccionados.map((nombre, index) => (
                    <span key={index} className="project-tag">
                      {nombre}
                    </span>
                  ))}
                </div>
              </div>
              
              <div className="summary-card">
                <h3>Ganancia Total</h3>
                <p className="summary-value success">${results.ganancia_total.toLocaleString()}</p>
              </div>
              
              <div className="summary-card">
                <h3>Inversión Total</h3>
                <p className="summary-value">${results.peso_total.toLocaleString()}</p>
              </div>
              
              <div className="summary-card">
                <h3>Capacidad Utilizada</h3>
                <p className="summary-value">
                  {((results.peso_total / portfolioData.capacidad) * 100).toFixed(1)}%
                </p>
              </div>
            </div>
          </section>
        )}
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <p>&copy; 2025 Microservicio de Optimización de Portafolio. Desarrollado para el Examen Final.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
