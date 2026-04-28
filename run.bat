@echo off
echo ============================================================
echo CREDIT CARD FRAUD DETECTION SYSTEM
echo ============================================================
echo.
echo Starting application...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the Flask app
python app.py

pause
