# Microservicio de Optimización de Portafolio de Inversiones

## Descripción
Este microservicio implementa un algoritmo de optimización de portafolio que maximiza la ganancia total sin exceder la capacidad presupuestaria, utilizando el problema de la mochila (knapsack problem) resuelto con programación dinámica.

## Características
- **Endpoint**: `/optimizar` (POST)
- **Algoritmo**: Programación dinámica para optimización
- **Validación**: Validación robusta de datos de entrada
- **Manejo de errores**: Respuestas de error claras y descriptivas
- **API**: Documentación automática con OpenAPI/Swagger

## Instalación

### Prerrequisitos
- Python 3.8+
- pip

### Pasos de instalación
1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd EXAMEN-FINAL
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar el servidor:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Uso de la API

### Endpoint: POST /optimizar

#### Entrada (JSON):
```json
{
  "capacidad": 10000,
  "objetos": [
    {"nombre": "A", "peso": 2000, "ganancia": 1500},
    {"nombre": "B", "peso": 4000, "ganancia": 3500},
    {"nombre": "C", "peso": 5000, "ganancia": 4000},
    {"nombre": "D", "peso": 3000, "ganancia": 2500}
  ]
}
```

#### Parámetros:
- **capacidad**: Límite presupuestario total (número entero positivo)
- **objetos**: Lista de proyectos/inversiones
  - **nombre**: Identificador del proyecto
  - **peso**: Costo requerido
  - **ganancia**: Beneficio esperado

#### Salida (JSON):
```json
{
  "seleccionados": ["B", "C"],
  "ganancia_total": 7500,
  "peso_total": 9000
}
```

## Ejemplos de uso

### Caso 1: 5 fondos con capacidad 10000
**Entrada:**
```json
{
  "capacidad": 10000,
  "objetos": [
    {"nombre": "A", "peso": 2000, "ganancia": 1500},
    {"nombre": "B", "peso": 4000, "ganancia": 3500},
    {"nombre": "C", "peso": 5000, "ganancia": 4000},
    {"nombre": "D", "peso": 3000, "ganancia": 2500},
    {"nombre": "E", "peso": 1000, "ganancia": 800}
  ]
}
```

**Salida esperada:**
```json
{
  "seleccionados": ["B", "C", "E"],
  "ganancia_total": 9300,
  "peso_total": 10000
}
```

### Caso 2: Acciones y bonos con capacidad 8000
**Entrada:**
```json
{
  "capacidad": 8000,
  "objetos": [
    {"nombre": "Y", "peso": 3000, "ganancia": 2500},
    {"nombre": "Z", "peso": 2000, "ganancia": 1800},
    {"nombre": "Q", "peso": 2000, "ganancia": 1900}
  ]
}
```

**Salida esperada:**
```json
{
  "seleccionados": ["Y", "Z", "Q"],
  "ganancia_total": 6200,
  "peso_total": 7000
}
```

## Estructura del proyecto
```
EXAMEN-FINAL/
├── main.py                 # Aplicación principal FastAPI
├── models.py              # Modelos de datos Pydantic
├── optimizer.py           # Lógica del algoritmo de optimización
├── requirements.txt       # Dependencias del proyecto
├── tests/                 # Pruebas unitarias
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_optimizer.py
│   └── test_api.py
└── README.md              # Este archivo
```

## Pruebas

Ejecutar las pruebas:
```bash
pytest tests/ -v
```

## Documentación de la API

Una vez ejecutado el servidor, acceder a:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Docker

### Construir imagen:
```bash
docker build -t portfolio-optimizer .
```

### Ejecutar contenedor:
```bash
docker run -p 8000:8000 portfolio-optimizer
```

## Tecnologías utilizadas
- **FastAPI**: Framework web moderno y rápido
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI
- **Python**: Lenguaje de programación

## Autor
Desarrollado para el Examen Final - Microservicio de Optimización de Portafolio
