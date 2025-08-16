#!/usr/bin/env python3
"""
Script de prueba para verificar el funcionamiento del backend
"""

import requests
import json
import time
from typing import Dict, Any

# Configuración
BASE_URL = "http://localhost:8000"
TIMEOUT = 10

def test_health_check() -> bool:
    """Prueba el endpoint de health check"""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check exitoso: {data['status']}")
            return True
        else:
            print(f"❌ Health check falló: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en health check: {e}")
        return False

def test_root_endpoint() -> bool:
    """Prueba el endpoint raíz"""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint exitoso: {data['mensaje']}")
            return True
        else:
            print(f"❌ Root endpoint falló: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en root endpoint: {e}")
        return False

def test_optimizacion_caso_basico() -> bool:
    """Prueba el caso básico del enunciado"""
    try:
        payload = {
            "capacidad": 10000,
            "objetos": [
                {"nombre": "A", "peso": 2000, "ganancia": 1500},
                {"nombre": "B", "peso": 4000, "ganancia": 3500},
                {"nombre": "C", "peso": 5000, "ganancia": 4000},
                {"nombre": "D", "peso": 3000, "ganancia": 2500}
            ]
        }
        
        response = requests.post(f"{BASE_URL}/optimizar", json=payload, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Optimización exitosa:")
            print(f"   Seleccionados: {data['seleccionados']}")
            print(f"   Ganancia total: {data['ganancia_total']}")
            print(f"   Peso total: {data['peso_total']}")
            
            # Verificar resultado esperado
            if set(data['seleccionados']) == {"B", "C"} and data['ganancia_total'] == 7500:
                print("   ✅ Resultado correcto según el enunciado")
                return True
            else:
                print("   ⚠️ Resultado diferente al esperado")
                return False
        else:
            print(f"❌ Optimización falló: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error en optimización: {e}")
        return False

def test_optimizacion_caso_limite() -> bool:
    """Prueba caso límite de capacidad"""
    try:
        payload = {
            "capacidad": 6000,
            "objetos": [
                {"nombre": "A", "peso": 1000, "ganancia": 500},
                {"nombre": "B", "peso": 2000, "ganancia": 1000},
                {"nombre": "C", "peso": 3000, "ganancia": 1500}
            ]
        }
        
        response = requests.post(f"{BASE_URL}/optimizar", json=payload, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Caso límite exitoso:")
            print(f"   Seleccionados: {data['seleccionados']}")
            print(f"   Ganancia total: {data['ganancia_total']}")
            print(f"   Peso total: {data['peso_total']}")
            return True
        else:
            print(f"❌ Caso límite falló: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en caso límite: {e}")
        return False

def test_optimizacion_caso_eficiencia() -> bool:
    """Prueba caso de eficiencia"""
    try:
        payload = {
            "capacidad": 2000,
            "objetos": [
                {"nombre": "A", "peso": 1000, "ganancia": 100},   # ratio: 0.1
                {"nombre": "B", "peso": 1000, "ganancia": 500},   # ratio: 0.5
                {"nombre": "C", "peso": 1000, "ganancia": 1000},  # ratio: 1.0
            ]
        }
        
        response = requests.post(f"{BASE_URL}/optimizar", json=payload, timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Caso eficiencia exitoso:")
            print(f"   Seleccionados: {data['seleccionados']}")
            print(f"   Ganancia total: {data['ganancia_total']}")
            print(f"   Peso total: {data['peso_total']}")
            
            # Verificar que se prioricen los mejores ratios
            if set(data['seleccionados']) == {"C", "B"}:
                print("   ✅ Priorización por eficiencia correcta")
                return True
            else:
                print("   ⚠️ Priorización por eficiencia incorrecta")
                return False
        else:
            print(f"❌ Caso eficiencia falló: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en caso eficiencia: {e}")
        return False

def test_ejemplo_predefinido() -> bool:
    """Prueba el endpoint de ejemplo predefinido"""
    try:
        response = requests.post(f"{BASE_URL}/optimizar/ejemplo", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Ejemplo predefinido exitoso:")
            print(f"   Seleccionados: {data['seleccionados']}")
            print(f"   Ganancia total: {data['ganancia_total']}")
            print(f"   Peso total: {data['peso_total']}")
            return True
        else:
            print(f"❌ Ejemplo predefinido falló: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en ejemplo predefinido: {e}")
        return False

def test_validaciones() -> bool:
    """Prueba las validaciones de la API"""
    print("\n🔍 Probando validaciones...")
    
    # Test capacidad cero
    try:
        payload = {"capacidad": 0, "objetos": [{"nombre": "A", "peso": 1000, "ganancia": 500}]}
        response = requests.post(f"{BASE_URL}/optimizar", json=payload, timeout=TIMEOUT)
        if response.status_code == 422:
            print("   ✅ Capacidad cero rechazada correctamente")
        else:
            print(f"   ❌ Capacidad cero no fue rechazada: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error probando capacidad cero: {e}")
        return False
    
    # Test peso cero
    try:
        payload = {"capacidad": 1000, "objetos": [{"nombre": "A", "peso": 0, "ganancia": 500}]}
        response = requests.post(f"{BASE_URL}/optimizar", json=payload, timeout=TIMEOUT)
        if response.status_code == 422:
            print("   ✅ Peso cero rechazado correctamente")
        else:
            print(f"   ❌ Peso cero no fue rechazado: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error probando peso cero: {e}")
        return False
    
    # Test nombres duplicados
    try:
        payload = {
            "capacidad": 1000,
            "objetos": [
                {"nombre": "A", "peso": 500, "ganancia": 300},
                {"nombre": "A", "peso": 500, "ganancia": 300}
            ]
        }
        response = requests.post(f"{BASE_URL}/optimizar", json=payload, timeout=TIMEOUT)
        if response.status_code == 422:
            print("   ✅ Nombres duplicados rechazados correctamente")
        else:
            print(f"   ❌ Nombres duplicados no fueron rechazados: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Error probando nombres duplicados: {e}")
        return False
    
    return True

def main():
    """Función principal de pruebas"""
    print("🚀 Iniciando pruebas del Backend - Microservicio de Optimización de Portafolio")
    print("=" * 70)
    
    # Esperar a que el servidor esté listo
    print("⏳ Esperando a que el servidor esté listo...")
    time.sleep(2)
    
    tests = [
        ("Health Check", test_health_check),
        ("Root Endpoint", test_root_endpoint),
        ("Optimización Caso Básico", test_optimizacion_caso_basico),
        ("Optimización Caso Límite", test_optimizacion_caso_limite),
        ("Optimización Caso Eficiencia", test_optimizacion_caso_eficiencia),
        ("Ejemplo Predefinido", test_ejemplo_predefinido),
        ("Validaciones", test_validaciones),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Ejecutando: {test_name}")
        print("-" * 50)
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASÓ")
            else:
                print(f"❌ {test_name}: FALLÓ")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    print("\n" + "=" * 70)
    print(f"📊 RESUMEN DE PRUEBAS:")
    print(f"   Total: {total}")
    print(f"   Pasaron: {passed}")
    print(f"   Fallaron: {total - passed}")
    print(f"   Porcentaje: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 ¡Todas las pruebas pasaron! El backend está funcionando correctamente.")
        return True
    else:
        print(f"\n⚠️ {total - passed} prueba(s) fallaron. Revisar el backend.")
        return False

if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️ Pruebas interrumpidas por el usuario.")
        exit(1)
    except Exception as e:
        print(f"\n\n💥 Error inesperado: {e}")
        exit(1)
