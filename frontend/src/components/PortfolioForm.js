import React, { useState } from 'react';
import './PortfolioForm.css';

const PortfolioForm = ({ 
  portfolioData, 
  onUpdate, 
  onSubmit, 
  onClear, 
  onExample, 
  disabled 
}) => {
  const [localData, setLocalData] = useState(portfolioData);

  // Función para actualizar la capacidad
  const handleCapacidadChange = (e) => {
    const newCapacidad = parseInt(e.target.value) || 0;
    const newData = { ...localData, capacidad: newCapacidad };
    setLocalData(newData);
    onUpdate(newData);
  };

  // Función para actualizar un objeto específico
  const handleObjetoChange = (index, field, value) => {
    const newObjetos = [...localData.objetos];
    newObjetos[index] = { ...newObjetos[index], [field]: value };
    const newData = { ...localData, objetos: newObjetos };
    setLocalData(newData);
    onUpdate(newData);
  };

  // Función para agregar un nuevo objeto
  const handleAddObjeto = () => {
    const newObjeto = {
      nombre: `Proyecto_${localData.objetos.length + 1}`,
      peso: 1000,
      ganancia: 500
    };
    const newObjetos = [...localData.objetos, newObjeto];
    const newData = { ...localData, objetos: newObjetos };
    setLocalData(newData);
    onUpdate(newData);
  };

  // Función para eliminar un objeto
  const handleRemoveObjeto = (index) => {
    if (localData.objetos.length > 1) {
      const newObjetos = localData.objetos.filter((_, i) => i !== index);
      const newData = { ...localData, objetos: newObjetos };
      setLocalData(newData);
      onUpdate(newData);
    }
  };

  // Función para limpiar el formulario local
  const handleClearLocal = () => {
    const defaultData = {
      capacidad: 10000,
      objetos: [
        { nombre: 'A', peso: 2000, ganancia: 1500 },
        { nombre: 'B', peso: 4000, ganancia: 3500 },
        { nombre: 'C', peso: 5000, ganancia: 4000 },
        { nombre: 'D', peso: 3000, ganancia: 2500 }
      ]
    };
    setLocalData(defaultData);
    onClear();
  };

  // Función para validar el formulario
  const isFormValid = () => {
    return localData.capacidad > 0 && 
           localData.objetos.length > 0 &&
           localData.objetos.every(obj => 
             obj.nombre.trim() !== '' && 
             obj.peso > 0 && 
             obj.ganancia > 0
           );
  };

  return (
    <div className="portfolio-form" id="form">
      <h2 className="form-title">Configuración del Portafolio</h2>
      
      {/* Capacidad */}
      <div className="form-group">
        <label htmlFor="capacidad" className="form-label">
          Capacidad Presupuestaria (USD)
        </label>
        <input
          type="number"
          id="capacidad"
          className="form-input"
          value={localData.capacidad}
          onChange={handleCapacidadChange}
          min="1"
          placeholder="Ej: 10000"
          disabled={disabled}
        />
        <small className="form-help">
          Ingresa el límite presupuestario total disponible
        </small>
      </div>

      {/* Lista de Objetos */}
      <div className="form-group">
        <div className="form-header">
          <label className="form-label">Proyectos de Inversión</label>
          <button
            type="button"
            className="btn btn-secondary btn-sm"
            onClick={handleAddObjeto}
            disabled={disabled}
          >
            + Agregar Proyecto
          </button>
        </div>
        
        <div className="objetos-list">
          {localData.objetos.map((objeto, index) => (
            <div key={index} className="objeto-item">
              <div className="objeto-header">
                <span className="objeto-number">#{index + 1}</span>
                {localData.objetos.length > 1 && (
                  <button
                    type="button"
                    className="btn-remove"
                    onClick={() => handleRemoveObjeto(index)}
                    disabled={disabled}
                    title="Eliminar proyecto"
                  >
                    ×
                  </button>
                )}
              </div>
              
              <div className="objeto-fields">
                <div className="field-group">
                  <label className="field-label">Nombre</label>
                  <input
                    type="text"
                    className="form-input"
                    value={objeto.nombre}
                    onChange={(e) => handleObjetoChange(index, 'nombre', e.target.value)}
                    placeholder="Ej: Proyecto_A"
                    disabled={disabled}
                  />
                </div>
                
                <div className="field-group">
                  <label className="field-label">Costo (USD)</label>
                  <input
                    type="number"
                    className="form-input"
                    value={objeto.peso}
                    onChange={(e) => handleObjetoChange(index, 'peso', parseInt(e.target.value) || 0)}
                    placeholder="Ej: 2000"
                    min="1"
                    disabled={disabled}
                  />
                </div>
                
                <div className="field-group">
                  <label className="field-label">Ganancia (USD)</label>
                  <input
                    type="number"
                    className="form-input"
                    value={objeto.ganancia}
                    onChange={(e) => handleObjetoChange(index, 'ganancia', parseInt(e.target.value) || 0)}
                    placeholder="Ej: 1500"
                    min="1"
                    disabled={disabled}
                  />
                </div>
              </div>
              
              {/* Ratio de eficiencia */}
              <div className="objeto-efficiency">
                <span className="efficiency-label">Ratio Ganancia/Costo:</span>
                <span className="efficiency-value">
                  {(objeto.ganancia / objeto.peso).toFixed(3)}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Botones de acción */}
      <div className="form-actions">
        <button
          type="button"
          className="btn btn-primary"
          onClick={onSubmit}
          disabled={disabled || !isFormValid()}
        >
          {disabled ? 'Optimizando...' : '🔄 Optimizar Portafolio'}
        </button>
        
        <button
          type="button"
          className="btn btn-secondary"
          onClick={onExample}
          disabled={disabled}
        >
          📚 Ejecutar Ejemplo
        </button>
        
        <button
          type="button"
          className="btn btn-outline"
          onClick={handleClearLocal}
          disabled={disabled}
        >
          🗑️ Limpiar Formulario
        </button>
      </div>

      {/* Información adicional */}
      <div className="form-info">
        <div className="info-card">
          <h4>💡 Cómo funciona</h4>
          <p>
            El algoritmo utiliza programación dinámica para encontrar la combinación 
            óptima de proyectos que maximice la ganancia total sin exceder la capacidad presupuestaria.
          </p>
        </div>
        
        <div className="info-card">
          <h4>📊 Métricas importantes</h4>
          <p>
            El ratio Ganancia/Costo indica la eficiencia de cada proyecto. 
            Los proyectos con mayor ratio tienen prioridad en la optimización.
          </p>
        </div>
      </div>
    </div>
  );
};

export default PortfolioForm;
