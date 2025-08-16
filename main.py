from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import time
import logging
from typing import Dict, Any

from models import (
    SolicitudOptimizacion, 
    ResultadoOptimizacion, 
    ErrorResponse, 
    MensajeExito
)
from optimizer import optimizador

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuración de la aplicación
app_config = {
    "title": "Microservicio de Optimización de Portafolio de Inversiones",
    "description": """
    API para optimizar la selección de inversiones maximizando la ganancia total
    sin exceder la capacidad presupuestaria.
    
    ## Características
    * **Algoritmo de Programación Dinámica**: Resuelve el problema de la mochila de manera óptima
    * **Validación Robusta**: Validación completa de datos de entrada
    * **Manejo de Errores**: Respuestas de error claras y descriptivas
    * **Documentación Automática**: OpenAPI/Swagger integrado
    
    ## Endpoints
    * `POST /optimizar` - Optimiza la selección de inversiones
    * `GET /health` - Verifica el estado del servicio
    * `GET /stats` - Obtiene estadísticas del servicio
    """,
    "version": "1.0.0",
    "contact": {
        "name": "Equipo de Desarrollo",
        "email": "desarrollo@empresa.com"
    },
    "license_info": {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
}

# Eventos del ciclo de vida de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Maneja eventos del ciclo de vida de la aplicación"""
    # Startup
    logger.info("🚀 Iniciando Microservicio de Optimización de Portafolio")
    logger.info(f"📊 Versión: {app_config['version']}")
    logger.info("✅ Servicio listo para recibir solicitudes")
    
    yield
    
    # Shutdown
    logger.info("🛑 Cerrando Microservicio de Optimización de Portafolio")

# Crear aplicación FastAPI
app = FastAPI(
    **app_config,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware para logging de requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Middleware para logging de requests y medición de tiempo"""
    start_time = time.time()
    
    # Log del request
    logger.info(f"📥 {request.method} {request.url.path} - Cliente: {request.client.host}")
    
    # Procesar request
    response = await call_next(request)
    
    # Calcular tiempo de respuesta
    process_time = time.time() - start_time
    
    # Log de la respuesta
    logger.info(f"📤 {request.method} {request.url.path} - Status: {response.status_code} - Tiempo: {process_time:.4f}s")
    
    # Agregar header de tiempo de procesamiento
    response.headers["X-Process-Time"] = str(process_time)
    
    return response

# Exception handler global
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Maneja excepciones globales no capturadas"""
    logger.error(f"❌ Error no manejado en {request.url.path}: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Error interno del servidor",
            detalle="Ocurrió un error inesperado. Por favor, intente nuevamente.",
            codigo="INTERNAL_ERROR"
        ).dict()
    )

# Endpoints de la API

@app.get("/", tags=["Información"])
async def root() -> Dict[str, Any]:
    """Endpoint raíz con información del servicio"""
    return {
        "mensaje": "Microservicio de Optimización de Portafolio de Inversiones",
        "version": app_config["version"],
        "documentacion": "/docs",
        "endpoints": {
            "optimizar": "/optimizar",
            "health": "/health",
            "stats": "/stats"
        }
    }

@app.get("/health", tags=["Monitoreo"])
async def health_check() -> Dict[str, Any]:
    """Verifica el estado de salud del servicio"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "portfolio-optimizer",
        "version": app_config["version"]
    }

@app.get("/stats", tags=["Monitoreo"])
async def get_stats() -> Dict[str, Any]:
    """Obtiene estadísticas del servicio"""
    return {
        "service": "portfolio-optimizer",
        "version": app_config["version"],
        "uptime": time.time(),
        "endpoints": {
            "total": 4,
            "documented": 4
        }
    }

@app.post("/optimizar", 
          response_model=ResultadoOptimizacion,
          tags=["Optimización"],
          summary="Optimizar selección de inversiones",
          description="""
          Optimiza la selección de inversiones para maximizar la ganancia total
          sin exceder la capacidad presupuestaria.
          
          Utiliza un algoritmo de programación dinámica para garantizar la solución óptima.
          """,
          responses={
              200: {
                  "description": "Optimización exitosa",
                  "content": {
                      "application/json": {
                          "example": {
                              "seleccionados": ["B", "C"],
                              "ganancia_total": 7500,
                              "peso_total": 9000
                          }
                      }
                  }
              },
              400: {
                  "description": "Datos de entrada inválidos",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Datos de entrada inválidos",
                              "detalle": "La capacidad debe ser mayor que 0",
                              "codigo": "VALIDATION_ERROR"
                          }
                      }
                  }
              },
              422: {
                  "description": "Error de validación de esquema",
                  "content": {
                      "application/json": {
                          "example": {
                              "detail": [
                                  {
                                      "loc": ["body", "capacidad"],
                                      "msg": "ensure this value is greater than 0",
                                      "type": "value_error.number.not_gt"
                                  }
                              ]
                          }
                      }
                  }
              }
          })
async def optimizar_portafolio(solicitud: SolicitudOptimizacion) -> ResultadoOptimizacion:
    """
    Optimiza la selección de inversiones para maximizar la ganancia total.
    
    Args:
        solicitud: Solicitud de optimización con capacidad y objetos
        
    Returns:
        Resultado de la optimización con objetos seleccionados y métricas
        
    Raises:
        HTTPException: Si hay errores en la validación o procesamiento
    """
    try:
        logger.info(f"🔄 Iniciando optimización para capacidad: {solicitud.capacidad}, "
                   f"objetos: {len(solicitud.objetos)}")
        
        # Validar que la capacidad sea suficiente para al menos un objeto
        peso_minimo = min(obj.peso for obj in solicitud.objetos)
        if solicitud.capacidad < peso_minimo:
            raise HTTPException(
                status_code=400,
                detail=ErrorResponse(
                    error="Capacidad insuficiente",
                    detalle=f"La capacidad ({solicitud.capacidad}) es menor que el peso mínimo requerido ({peso_minimo})",
                    codigo="INSUFFICIENT_CAPACITY"
                ).dict()
            )
        
        # Realizar optimización
        resultado = optimizador.optimizar(solicitud.capacidad, solicitud.objetos)
        
        logger.info(f"✅ Optimización completada exitosamente: "
                   f"{len(resultado.seleccionados)} objetos seleccionados, "
                   f"ganancia: {resultado.ganancia_total}, peso: {resultado.peso_total}")
        
        return resultado
        
    except ValueError as e:
        logger.warning(f"⚠️ Error de validación: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                error="Error de validación",
                detalle=str(e),
                codigo="VALIDATION_ERROR"
            ).dict()
        )
    except Exception as e:
        logger.error(f"❌ Error durante la optimización: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                error="Error interno del servidor",
                detalle="Ocurrió un error durante la optimización. Por favor, intente nuevamente.",
                codigo="OPTIMIZATION_ERROR"
            ).dict()
        )

# Endpoint de ejemplo con datos predefinidos
@app.post("/optimizar/ejemplo", 
          response_model=ResultadoOptimizacion,
          tags=["Ejemplos"],
          summary="Ejemplo de optimización con datos predefinidos",
          description="Ejecuta la optimización con un conjunto de datos de ejemplo predefinidos.")
async def optimizar_ejemplo() -> ResultadoOptimizacion:
    """Ejemplo de optimización con datos predefinidos del enunciado"""
    from models import Objeto
    
    # Datos de ejemplo del enunciado
    objetos_ejemplo = [
        Objeto(nombre="A", peso=2000, ganancia=1500),
        Objeto(nombre="B", peso=4000, ganancia=3500),
        Objeto(nombre="C", peso=5000, ganancia=4000),
        Objeto(nombre="D", peso=3000, ganancia=2500)
    ]
    
    capacidad_ejemplo = 10000
    
    logger.info("📚 Ejecutando ejemplo con datos predefinidos")
    
    try:
        resultado = optimizador.optimizar(capacidad_ejemplo, objetos_ejemplo)
        logger.info("✅ Ejemplo ejecutado exitosamente")
        return resultado
    except Exception as e:
        logger.error(f"❌ Error en ejemplo: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                error="Error en ejemplo",
                detalle=str(e),
                codigo="EXAMPLE_ERROR"
            ).dict()
        )

if __name__ == "__main__":
    import uvicorn
    
    logger.info("🚀 Iniciando servidor de desarrollo...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
