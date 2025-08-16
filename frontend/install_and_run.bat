@echo off
echo ========================================
echo  Instalador del Frontend React
echo  Optimizador de Portafolio
echo ========================================
echo.

echo Verificando Node.js...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js no está instalado.
    echo Por favor, instala Node.js desde: https://nodejs.org/
    pause
    exit /b 1
)

echo Node.js encontrado: 
node --version
echo.

echo Verificando npm...
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: npm no está disponible.
    pause
    exit /b 1
)

echo npm encontrado:
npm --version
echo.

echo Instalando dependencias...
npm install
if %errorlevel% neq 0 (
    echo ERROR: Fallo en la instalación de dependencias.
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Instalación completada exitosamente!
echo ========================================
echo.
echo Para ejecutar el frontend:
echo   1. Asegúrate de que el backend esté ejecutándose en http://localhost:8000
echo   2. Ejecuta: npm start
echo   3. Abre http://localhost:3000 en tu navegador
echo.
echo ¿Deseas ejecutar el frontend ahora? (S/N)
set /p choice=

if /i "%choice%"=="S" (
    echo.
    echo Iniciando el frontend...
    echo Presiona Ctrl+C para detener
    npm start
) else (
    echo.
    echo Para ejecutar más tarde, usa: npm start
)

pause
