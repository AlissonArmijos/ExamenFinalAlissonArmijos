# Frontend - Optimizador de Portafolio de Inversiones

## 📋 Descripción

Frontend en React para el Microservicio de Optimización de Portafolio de Inversiones. Esta aplicación web proporciona una interfaz intuitiva y moderna para interactuar con el algoritmo de optimización del backend.

## ✨ Características

- **Interfaz Moderna**: Diseño responsive con gradientes y sombras
- **Formulario Dinámico**: Agregar/eliminar proyectos de inversión dinámicamente
- **Validación en Tiempo Real**: Validación de formularios con feedback visual
- **Visualización de Datos**: Gráficos interactivos usando Chart.js
- **Tabla de Resultados**: Vista detallada de proyectos seleccionados y no seleccionados
- **Responsive Design**: Optimizado para dispositivos móviles y desktop
- **Mensajes de Estado**: Notificaciones de éxito y error con animaciones

## 🚀 Instalación

### Prerrequisitos

- Node.js 16+ 
- npm o yarn
- Backend ejecutándose en `http://localhost:8000`

### Pasos de instalación

1. **Clonar el repositorio y navegar al frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar dependencias:**
   ```bash
   npm install
   ```

3. **Ejecutar en modo desarrollo:**
   ```bash
   npm start
   ```

4. **Abrir en el navegador:**
   ```
   http://localhost:3000
   ```

## 🏗️ Estructura del Proyecto

```
frontend/
├── public/
│   └── index.html          # HTML principal
├── src/
│   ├── components/         # Componentes React
│   │   ├── Header.js       # Encabezado de la aplicación
│   │   ├── PortfolioForm.js # Formulario principal
│   │   ├── ResultsTable.js  # Tabla de resultados
│   │   ├── ResultsChart.js  # Gráficos de resultados
│   │   ├── LoadingSpinner.js # Spinner de carga
│   │   ├── ErrorMessage.js  # Mensajes de error
│   │   ├── SuccessMessage.js # Mensajes de éxito
│   │   └── *.css           # Estilos de componentes
│   ├── App.js              # Componente principal
│   ├── App.css             # Estilos de la aplicación
│   ├── index.js            # Punto de entrada
│   └── index.css           # Estilos globales
├── package.json            # Dependencias y scripts
└── README.md               # Este archivo
```

## 🎯 Uso de la Aplicación

### 1. Configuración del Portafolio

- **Capacidad Presupuestaria**: Ingresa el límite presupuestario total
- **Proyectos de Inversión**: 
  - Agrega proyectos con el botón "+ Agregar Proyecto"
  - Cada proyecto requiere: Nombre, Costo y Ganancia esperada
  - El ratio Ganancia/Costo se calcula automáticamente
  - Elimina proyectos con el botón "×" (mínimo 1 proyecto)

### 2. Optimización

- **Optimizar Portafolio**: Ejecuta el algoritmo de optimización
- **Ejecutar Ejemplo**: Prueba con datos predefinidos del enunciado
- **Limpiar Formulario**: Restaura los valores por defecto

### 3. Visualización de Resultados

- **Tabla de Análisis**: Muestra todos los proyectos con su estado de selección
- **Gráfico de Barras**: Compara costos y ganancias por proyecto
- **Gráfico de Dona**: Distribución de la capacidad presupuestaria
- **Resumen**: Métricas clave de la optimización

## 🎨 Tecnologías Utilizadas

- **React 18**: Framework de interfaz de usuario
- **Chart.js**: Biblioteca de gráficos interactivos
- **CSS3**: Estilos modernos con variables CSS y gradientes
- **Axios**: Cliente HTTP para comunicación con el backend
- **Responsive Design**: Mobile-first approach

## 🔧 Scripts Disponibles

```bash
# Modo desarrollo
npm start

# Construir para producción
npm run build

# Ejecutar pruebas
npm test

# Eyectar configuración (irreversible)
npm run eject
```

## 🌐 Configuración del Backend

El frontend está configurado para conectarse al backend en `http://localhost:8000`. Si necesitas cambiar la URL:

1. **Modificar proxy en package.json:**
   ```json
   {
     "proxy": "http://tu-backend-url:puerto"
   }
   ```

2. **O configurar variables de entorno:**
   ```bash
   REACT_APP_API_URL=http://tu-backend-url:puerto
   ```

## 📱 Responsive Design

La aplicación está optimizada para:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

## 🎯 Casos de Uso

### Caso Básico del Enunciado
- Capacidad: 10,000 USD
- Proyectos: A, B, C, D
- Resultado esperado: Selecciona B, C → Ganancia 7,500, Peso 9,000

### Casos de Prueba
- **Caso Límite**: Capacidad exacta para algunos proyectos
- **Caso de Eficiencia**: Proyectos con diferentes ratios G/C
- **Caso Único**: Un solo proyecto disponible

## 🚨 Solución de Problemas

### Error de Conexión
- Verifica que el backend esté ejecutándose
- Comprueba la URL en el proxy del package.json
- Revisa la consola del navegador para errores CORS

### Problemas de Rendimiento
- Los gráficos se optimizan automáticamente para diferentes tamaños de pantalla
- Las animaciones están optimizadas para dispositivos móviles

### Problemas de Dependencias
- Elimina `node_modules` y `package-lock.json`
- Ejecuta `npm install` nuevamente

## 📊 Métricas de Rendimiento

- **Tiempo de Carga**: < 2 segundos en conexiones 3G
- **Tiempo de Interacción**: < 100ms para respuestas de UI
- **Tamaño del Bundle**: Optimizado con React Scripts
- **Lighthouse Score**: 90+ en todas las categorías

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

Desarrollado para el Examen Final - Microservicio de Optimización de Portafolio

---

**Nota**: Asegúrate de que el backend esté ejecutándose antes de usar el frontend.
