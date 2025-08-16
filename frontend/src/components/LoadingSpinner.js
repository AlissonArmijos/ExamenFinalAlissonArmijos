import React from 'react';
import './LoadingSpinner.css';

const LoadingSpinner = () => {
  return (
    <div className="loading-container">
      <div className="loading-spinner">
        <div className="spinner-ring"></div>
        <div className="spinner-text">Optimizando portafolio...</div>
      </div>
    </div>
  );
};

export default LoadingSpinner;
