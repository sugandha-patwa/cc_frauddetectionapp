#!/bin/bash

echo "============================================================"
echo "CREDIT CARD FRAUD DETECTION SYSTEM - SETUP (MAC/LINUX)"
echo "============================================================"
echo ""

echo "[1/4] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    echo "Please make sure Python 3 is installed"
    exit 1
fi
echo "✓ Virtual environment created successfully!"
echo ""

echo "[2/4] Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated!"
echo ""

echo "[3/4] Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install packages"
    exit 1
fi
echo "✓ All packages installed successfully!"
echo ""

echo "[4/4] Setup complete!"
echo ""
echo "============================================================"
echo "INSTALLATION SUCCESSFUL!"
echo "============================================================"
echo ""
echo "To run the application:"
echo "  1. Run: ./run.sh"
echo "  2. Open browser: http://localhost:5000"
echo ""
echo "============================================================"
