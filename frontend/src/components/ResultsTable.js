import React from 'react';
import './ResultsTable.css';

const ResultsTable = ({ originalData, results, capacidad }) => {
  // Crear datos combinados para la tabla
  const tableData = originalData.map(objeto => ({
    ...objeto,
    seleccionado: results.seleccionados.includes(objeto.nombre),
    ratio: (objeto.ganancia / objeto.peso).toFixed(3)
  }));

  // Ordenar por ratio de eficiencia descendente
  const sortedData = [...tableData].sort((a, b) => parseFloat(b.ratio) - parseFloat(a.ratio));

  return (
    <div className="results-table">
      <h3 className="table-title">Análisis de Proyectos</h3>
      
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Proyecto</th>
              <th>Costo (USD)</th>
              <th>Ganancia (USD)</th>
              <th>Ratio G/C</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {sortedData.map((objeto, index) => (
              <tr 
                key={index} 
                className={`table-row ${objeto.seleccionado ? 'selected' : 'not-selected'}`}
              >
                <td className="project-name">
                  <span className="project-badge">{objeto.nombre}</span>
                </td>
                <td className="cost">
                  ${objeto.peso.toLocaleString()}
                </td>
                <td className="profit">
                  ${objeto.ganancia.toLocaleString()}
                </td>
                <td className="ratio">
                  <span className="ratio-value">{objeto.ratio}</span>
                </td>
                <td className="status">
                  {objeto.seleccionado ? (
                    <span className="status-badge selected">✅ Seleccionado</span>
                  ) : (
                    <span className="status-badge not-selected">❌ No seleccionado</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Resumen de la tabla */}
      <div className="table-summary">
        <div className="summary-row">
          <span className="summary-label">Total Proyectos:</span>
          <span className="summary-value">{originalData.length}</span>
        </div>
        <div className="summary-row">
          <span className="summary-label">Seleccionados:</span>
          <span className="summary-value success">{results.seleccionados.length}</span>
        </div>
        <div className="summary-row">
          <span className="summary-label">Capacidad Utilizada:</span>
          <span className="summary-value">
            {((results.peso_total / capacidad) * 100).toFixed(1)}%
          </span>
        </div>
        <div className="summary-row">
          <span className="summary-label">Eficiencia Promedio:</span>
          <span className="summary-value">
            {(originalData.reduce((sum, obj) => sum + (obj.ganancia / obj.peso), 0) / originalData.length).toFixed(3)}
          </span>
        </div>
      </div>
    </div>
  );
};

export default ResultsTable;
