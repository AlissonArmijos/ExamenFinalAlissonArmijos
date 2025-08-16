from pydantic import BaseModel, Field, validator
from typing import List
import re


class Objeto(BaseModel):
    """Modelo para representar un objeto de inversión"""
    nombre: str = Field(..., min_length=1, max_length=50, description="Identificador del proyecto/inversión")
    peso: int = Field(..., gt=0, description="Costo requerido para la inversión")
    ganancia: int = Field(..., gt=0, description="Beneficio esperado de la inversión")
    
    @validator('nombre')
    def nombre_valido(cls, v):
        """Validar que el nombre no contenga caracteres especiales"""
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('El nombre solo puede contener letras, números, guiones y guiones bajos')
        return v
    
    @validator('peso', 'ganancia')
    def valores_positivos(cls, v):
        """Validar que peso y ganancia sean positivos"""
        if v <= 0:
            raise ValueError('El valor debe ser mayor que 0')
        return v


class SolicitudOptimizacion(BaseModel):
    """Modelo para la solicitud de optimización"""
    capacidad: int = Field(..., gt=0, description="Límite presupuestario total")
    objetos: List[Objeto] = Field(..., min_items=1, max_items=100, description="Lista de proyectos/inversiones")
    
    @validator('capacidad')
    def capacidad_valida(cls, v):
        """Validar que la capacidad sea razonable"""
        if v > 1000000000:  # 1 billón como límite superior
            raise ValueError('La capacidad no puede exceder 1,000,000,000')
        return v
    
    @validator('objetos')
    def objetos_validos(cls, v):
        """Validar que no haya nombres duplicados"""
        nombres = [obj.nombre for obj in v]
        if len(nombres) != len(set(nombres)):
            raise ValueError('No puede haber nombres duplicados en los objetos')
        return v


class ResultadoOptimizacion(BaseModel):
    """Modelo para el resultado de la optimización"""
    seleccionados: List[str] = Field(..., description="Lista de nombres de objetos seleccionados")
    ganancia_total: int = Field(..., description="Ganancia total de los objetos seleccionados")
    peso_total: int = Field(..., description="Peso total de los objetos seleccionados")
    
    @validator('seleccionados')
    def seleccionados_validos(cls, v):
        """Validar que la lista de seleccionados no esté vacía si hay objetos"""
        if not v:
            raise ValueError('Debe haber al menos un objeto seleccionado')
        return v


class ErrorResponse(BaseModel):
    """Modelo para respuestas de error"""
    error: str = Field(..., description="Descripción del error")
    detalle: str = Field(..., description="Detalles adicionales del error")
    codigo: str = Field(..., description="Código de error interno")


class MensajeExito(BaseModel):
    """Modelo para mensajes de éxito"""
    mensaje: str = Field(..., description="Mensaje de confirmación")
    timestamp: str = Field(..., description="Timestamp de la operación")
