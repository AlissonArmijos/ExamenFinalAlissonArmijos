import React from 'react';
import { Bar, Doughnut } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import './ResultsChart.css';

// Registrar componentes de Chart.js
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

const ResultsChart = ({ originalData, results, capacidad }) => {
  // Preparar datos para el gráfico de barras
  const barData = {
    labels: originalData.map(obj => obj.nombre),
    datasets: [
      {
        label: 'Costo (USD)',
        data: originalData.map(obj => obj.peso),
        backgroundColor: originalData.map(obj => 
          results.seleccionados.includes(obj.nombre) 
            ? 'rgba(74, 222, 128, 0.8)' 
            : 'rgba(248, 113, 113, 0.6)'
        ),
        borderColor: originalData.map(obj => 
          results.seleccionados.includes(obj.nombre) 
            ? 'rgb(74, 222, 128)' 
            : 'rgb(248, 113, 113)'
        ),
        borderWidth: 2,
        borderRadius: 6,
      },
      {
        label: 'Ganancia (USD)',
        data: originalData.map(obj => obj.ganancia),
        backgroundColor: originalData.map(obj => 
          results.seleccionados.includes(obj.nombre) 
            ? 'rgba(102, 126, 234, 0.8)' 
            : 'rgba(156, 163, 175, 0.6)'
        ),
        borderColor: originalData.map(obj => 
          results.seleccionados.includes(obj.nombre) 
            ? 'rgb(102, 126, 234)' 
            : 'rgb(156, 163, 175)'
        ),
        borderWidth: 2,
        borderRadius: 6,
      }
    ]
  };

  // Preparar datos para el gráfico de dona
  const doughnutData = {
    labels: ['Capacidad Utilizada', 'Capacidad Restante'],
    datasets: [
      {
        data: [results.peso_total, capacidad - results.peso_total],
        backgroundColor: [
          'rgba(102, 126, 234, 0.8)',
          'rgba(156, 163, 175, 0.3)'
        ],
        borderColor: [
          'rgb(102, 126, 234)',
          'rgb(156, 163, 175)'
        ],
        borderWidth: 2,
      }
    ]
  };

  // Opciones para el gráfico de barras
  const barOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
        labels: {
          usePointStyle: true,
          padding: 20,
          font: {
            size: 12
          }
        }
      },
      title: {
        display: true,
        text: 'Comparación de Costos y Ganancias por Proyecto',
        font: {
          size: 14,
          weight: 'bold'
        },
        padding: {
          top: 10,
          bottom: 20
        }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            return `${context.dataset.label}: $${context.parsed.y.toLocaleString()}`;
          }
        }
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function(value) {
            return '$' + value.toLocaleString();
          }
        }
      }
    },
    interaction: {
      mode: 'index',
      intersect: false,
    }
  };

  // Opciones para el gráfico de dona
  const doughnutOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          usePointStyle: true,
          padding: 20,
          font: {
            size: 12
          }
        }
      },
      title: {
        display: true,
        text: 'Distribución de la Capacidad Presupuestaria',
        font: {
          size: 14,
          weight: 'bold'
        },
        padding: {
          top: 10,
          bottom: 20
        }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            const value = context.parsed;
            const percentage = ((value / capacidad) * 100).toFixed(1);
            return `${context.label}: $${value.toLocaleString()} (${percentage}%)`;
          }
        }
      }
    }
  };

  return (
    <div className="results-chart">
      <h3 className="chart-title">Visualización de Resultados</h3>
      
      <div className="charts-container">
        {/* Gráfico de barras */}
        <div className="chart-wrapper">
          <h4 className="chart-subtitle">Costos vs Ganancias por Proyecto</h4>
          <div className="chart-container">
            <Bar data={barData} options={barOptions} />
          </div>
          <div className="chart-legend">
            <div className="legend-item">
              <span className="legend-color selected"></span>
              <span>Proyectos Seleccionados</span>
            </div>
            <div className="legend-item">
              <span className="legend-color not-selected"></span>
              <span>Proyectos No Seleccionados</span>
            </div>
          </div>
        </div>

        {/* Gráfico de dona */}
        <div className="chart-wrapper">
          <h4 className="chart-subtitle">Distribución de Capacidad</h4>
          <div className="chart-container">
            <Doughnut data={doughnutData} options={doughnutOptions} />
          </div>
          <div className="capacity-info">
            <div className="capacity-item">
              <span className="capacity-label">Utilizada:</span>
              <span className="capacity-value">${results.peso_total.toLocaleString()}</span>
            </div>
            <div className="capacity-item">
              <span className="capacity-label">Disponible:</span>
              <span className="capacity-value">${(capacidad - results.peso_total).toLocaleString()}</span>
            </div>
            <div className="capacity-item">
              <span className="capacity-label">Porcentaje:</span>
              <span className="capacity-value">
                {((results.peso_total / capacidad) * 100).toFixed(1)}%
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultsChart;
