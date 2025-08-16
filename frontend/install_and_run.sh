#!/bin/bash

echo "========================================"
echo " Instalador del Frontend React"
echo " Optimizador de Portafolio"
echo "========================================"
echo

echo "Verificando Node.js..."
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js no está instalado."
    echo "Por favor, instala Node.js desde: https://nodejs.org/"
    exit 1
fi

echo "Node.js encontrado: $(node --version)"
echo

echo "Verificando npm..."
if ! command -v npm &> /dev/null; then
    echo "ERROR: npm no está disponible."
    exit 1
fi

echo "npm encontrado: $(npm --version)"
echo

echo "Instalando dependencias..."
if ! npm install; then
    echo "ERROR: Fallo en la instalación de dependencias."
    exit 1
fi

echo
echo "========================================"
echo " Instalación completada exitosamente!"
echo "========================================"
echo
echo "Para ejecutar el frontend:"
echo "  1. Asegúrate de que el backend esté ejecutándose en http://localhost:8000"
echo "  2. Ejecuta: npm start"
echo "  3. Abre http://localhost:3000 en tu navegador"
echo

read -p "¿Deseas ejecutar el frontend ahora? (s/N): " choice

if [[ $choice =~ ^[Ss]$ ]]; then
    echo
    echo "Iniciando el frontend..."
    echo "Presiona Ctrl+C para detener"
    npm start
else
    echo
    echo "Para ejecutar más tarde, usa: npm start"
fi
