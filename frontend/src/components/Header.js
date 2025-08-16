import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <div className="logo-icon">
              📊
            </div>
            <h1 className="logo-text">
              Optimizador de Portafolio
            </h1>
          </div>
          
          <nav className="nav">
            <a href="#form" className="nav-link">Formulario</a>
            <a href="#results" className="nav-link">Resultados</a>
            <a href="#about" className="nav-link">Acerca de</a>
          </nav>
        </div>
        
        <div className="header-subtitle">
          <p>Maximiza tu ganancia con algoritmos de optimización avanzados</p>
        </div>
      </div>
    </header>
  );
};

export default Header;
