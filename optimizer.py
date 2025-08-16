from typing import List, Tuple, Dict
from models import Objeto, ResultadoOptimizacion
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OptimizadorPortafolio:
    """
    Clase que implementa el algoritmo de optimización de portafolio
    utilizando programación dinámica para resolver el problema de la mochila
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def optimizar(self, capacidad: int, objetos: List[Objeto]) -> ResultadoOptimizacion:
        """
        Optimiza la selección de objetos para maximizar la ganancia
        sin exceder la capacidad presupuestaria.
        
        Args:
            capacidad: Límite presupuestario total
            objetos: Lista de objetos de inversión disponibles
            
        Returns:
            ResultadoOptimizacion con los objetos seleccionados y métricas
            
        Raises:
            ValueError: Si no hay objetos disponibles o capacidad inválida
        """
        try:
            # Validaciones básicas
            if not objetos:
                raise ValueError("No hay objetos disponibles para optimizar")
            
            if capacidad <= 0:
                raise ValueError("La capacidad debe ser mayor que 0")
            
            self.logger.info(f"Iniciando optimización con {len(objetos)} objetos y capacidad {capacidad}")
            
            # Ordenar objetos por ratio ganancia/peso (eficiencia) descendente
            objetos_ordenados = sorted(objetos, key=lambda x: x.ganancia/x.peso, reverse=True)
            
            # Aplicar algoritmo de programación dinámica
            seleccionados, ganancia_total, peso_total = self._algoritmo_programacion_dinamica(
                capacidad, objetos_ordenados
            )
            
            # Obtener nombres de objetos seleccionados
            nombres_seleccionados = [obj.nombre for obj in seleccionados]
            
            self.logger.info(f"Optimización completada: {len(seleccionados)} objetos seleccionados, "
                           f"ganancia total: {ganancia_total}, peso total: {peso_total}")
            
            return ResultadoOptimizacion(
                seleccionados=nombres_seleccionados,
                ganancia_total=ganancia_total,
                peso_total=peso_total
            )
            
        except Exception as e:
            self.logger.error(f"Error durante la optimización: {str(e)}")
            raise
    
    def _algoritmo_programacion_dinamica(self, capacidad: int, objetos: List[Objeto]) -> Tuple[List[Objeto], int, int]:
        """
        Implementa el algoritmo de programación dinámica para el problema de la mochila.
        
        Args:
            capacidad: Capacidad máxima de la mochila
            objetos: Lista de objetos ordenados por eficiencia
            
        Returns:
            Tupla con (objetos_seleccionados, ganancia_total, peso_total)
        """
        n = len(objetos)
        
        # Crear matriz DP: dp[i][w] = máxima ganancia usando los primeros i objetos con capacidad w
        dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
        
        # Crear matriz para rastrear qué objetos fueron seleccionados
        seleccion = [[False for _ in range(capacidad + 1)] for _ in range(n + 1)]
        
        # Llenar la matriz DP
        for i in range(1, n + 1):
            for w in range(capacidad + 1):
                # No incluir el objeto i
                dp[i][w] = dp[i-1][w]
                seleccion[i][w] = False
                
                # Incluir el objeto i si cabe
                if objetos[i-1].peso <= w:
                    ganancia_incluyendo = dp[i-1][w - objetos[i-1].peso] + objetos[i-1].ganancia
                    if ganancia_incluyendo > dp[i][w]:
                        dp[i][w] = ganancia_incluyendo
                        seleccion[i][w] = True
        
        # Reconstruir la solución
        objetos_seleccionados = []
        w = capacidad
        
        for i in range(n, 0, -1):
            if seleccion[i][w]:
                objetos_seleccionados.append(objetos[i-1])
                w -= objetos[i-1].peso
        
        # Calcular métricas finales
        ganancia_total = dp[n][capacidad]
        peso_total = sum(obj.peso for obj in objetos_seleccionados)
        
        return objetos_seleccionados, ganancia_total, peso_total
    
    def _algoritmo_greedy_alternativo(self, capacidad: int, objetos: List[Objeto]) -> Tuple[List[Objeto], int, int]:
        """
        Algoritmo greedy alternativo como respaldo (menos eficiente pero más simple).
        Se usa solo si hay problemas con el algoritmo principal.
        
        Args:
            capacidad: Capacidad máxima
            objetos: Lista de objetos ordenados por eficiencia
            
        Returns:
            Tupla con (objetos_seleccionados, ganancia_total, peso_total)
        """
        objetos_seleccionados = []
        peso_actual = 0
        ganancia_total = 0
        
        for obj in objetos:
            if peso_actual + obj.peso <= capacidad:
                objetos_seleccionados.append(obj)
                peso_actual += obj.peso
                ganancia_total += obj.ganancia
        
        return objetos_seleccionados, ganancia_total, peso_actual
    
    def obtener_estadisticas(self, objetos: List[Objeto]) -> Dict:
        """
        Obtiene estadísticas de los objetos disponibles.
        
        Args:
            objetos: Lista de objetos de inversión
            
        Returns:
            Diccionario con estadísticas
        """
        if not objetos:
            return {}
        
        pesos = [obj.peso for obj in objetos]
        ganancias = [obj.ganancia for obj in objetos]
        ratios = [obj.ganancia/obj.peso for obj in objetos]
        
        return {
            "total_objetos": len(objetos),
            "peso_total_disponible": sum(pesos),
            "ganancia_total_disponible": sum(ganancias),
            "peso_promedio": sum(pesos) / len(pesos),
            "ganancia_promedio": sum(ganancias) / len(ganancias),
            "ratio_ganancia_peso_promedio": sum(ratios) / len(ratios),
            "peso_minimo": min(pesos),
            "peso_maximo": max(pesos),
            "ganancia_minima": min(ganancias),
            "ganancia_maxima": max(ganancias)
        }


# Instancia global del optimizador
optimizador = OptimizadorPortafolio()
