@echo off
echo ============================================================
echo CREDIT CARD FRAUD DETECTION SYSTEM - SETUP (WINDOWS)
echo ============================================================
echo.

echo [1/4] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    echo Please make sure Python is installed and added to PATH
    pause
    exit /b 1
)
echo ✓ Virtual environment created successfully!
echo.

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated!
echo.

echo [3/4] Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)
echo ✓ All packages installed successfully!
echo.

echo [4/4] Setup complete!
echo.
echo ============================================================
echo INSTALLATION SUCCESSFUL!
echo ============================================================
echo.
echo To run the application:
echo   1. Run: run.bat
echo   2. Open browser: http://localhost:5000
echo.
echo ============================================================
pause
