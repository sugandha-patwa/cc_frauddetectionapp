# Credit Card Fraud Detection System
## Complete Setup Guide with Virtual Environment

---

## 📁 FOLDER STRUCTURE

After downloading, your folder should look like this:

```
fraud_detection_app/
├── app.py                          # Main Flask application
├── fraud_detection_model.pkl       # Trained ML model
├── requirements.txt                # Python dependencies
├── setup.bat                       # Windows setup script
├── setup.sh                        # Mac/Linux setup script
├── run.bat                         # Windows run script
├── run.sh                          # Mac/Linux run script
├── README.md                       # This file
├── static/
│   └── css/
│       └── style.css              # Stylesheet
└── templates/
    ├── index.html                 # Main page
    ├── quick_test.html            # Quick test page
    ├── dashboard.html             # Dashboard page
    └── about.html                 # About page
```

---

## 🚀 QUICK START (EASIEST WAY)

### **FOR WINDOWS:**

1. **Double-click** `setup.bat`
2. Wait for installation to complete
3. **Double-click** `run.bat`
4. Open browser to **http://localhost:5000**

### **FOR MAC/LINUX:**

1. **Double-click** `setup.sh` (or run `./setup.sh` in terminal)
2. Wait for installation to complete
3. **Double-click** `run.sh` (or run `./run.sh` in terminal)
4. Open browser to **http://localhost:5000**

---

## 📋 DETAILED SETUP INSTRUCTIONS

### **STEP 1: Check Python Installation**

Open Terminal (Mac/Linux) or Command Prompt (Windows) and run:

```bash
python --version
```

or

```bash
python3 --version
```

**You need Python 3.8 or higher.**

If Python is not installed:
- **Windows:** Download from https://python.org/downloads
- **Mac:** Run `brew install python3` or download from python.org
- **Linux:** Run `sudo apt install python3 python3-venv`

---

### **STEP 2: Navigate to Project Folder**

```bash
cd path/to/fraud_detection_app
```

Example:
```bash
cd ~/Downloads/fraud_detection_app
```

---

### **STEP 3: Run Setup Script**

**Windows:**
```bash
setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**What this does:**
1. Creates a virtual environment (isolated Python environment)
2. Activates the virtual environment
3. Installs all required packages (Flask, scikit-learn, pandas, numpy)

**This takes 2-3 minutes.**

---

### **STEP 4: Run the Application**

**Windows:**
```bash
run.bat
```

**Mac/Linux:**
```bash
./run.sh
```

You should see:
```
============================================================
CREDIT CARD FRAUD DETECTION SYSTEM
============================================================

✓ Model loaded successfully!
✓ Features: 19

Starting Flask server...
Access the application at: http://127.0.0.1:5000
============================================================
```

---

### **STEP 5: Open in Browser**

Open your web browser and go to:
- **http://localhost:5000**
- OR **http://127.0.0.1:5000**

---

## 🎯 USING THE APPLICATION

### **1. Quick Test (Recommended for First Time)**
- Click **"Quick Test"** in navigation
- Click on any example card:
  - ✅ **Legitimate Transaction** - Should show LOW risk
  - ⚠️ **Suspicious Transaction** - Should show CRITICAL risk
  - ❓ **Moderate Risk** - Should show HIGH/MEDIUM risk
- See instant results!

### **2. Custom Transaction**
- Go to home page
- Fill in transaction details (or use default values)
- Click **"Analyze Transaction"**
- View fraud probability and risk level

### **3. Dashboard**
- Click **"Dashboard"** to see:
  - Model accuracy: 99.96%
  - Confusion matrix
  - Feature importance

### **4. About**
- Learn about the project
- See technology stack
- View competitive analysis

---

## 🛠️ MANUAL SETUP (If Scripts Don't Work)

### **Step 1: Create Virtual Environment**

**Windows:**
```bash
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

### **Step 2: Activate Virtual Environment**

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear in your command prompt.

### **Step 3: Install Packages**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **Step 4: Run Application**

```bash
python app.py
```

### **Step 5: To Stop the Application**

Press `Ctrl + C` in the terminal

### **Step 6: Deactivate Virtual Environment (When Done)**

```bash
deactivate
```

---

## ❓ TROUBLESHOOTING

### **Problem 1: "Python not found"**
- Install Python from https://python.org/downloads
- Make sure to check "Add Python to PATH" during installation (Windows)

### **Problem 2: "pip not found"**
```bash
python -m pip install --upgrade pip
```

### **Problem 3: "Permission denied" (Mac/Linux)**
```bash
chmod +x setup.sh run.sh
```

### **Problem 4: "Port 5000 already in use"**
Edit `app.py`, change last line:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

Then open: http://localhost:5001

### **Problem 5: Virtual environment not activating**

**Windows:**
Run this first:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Mac/Linux:**
Make sure you're using `source`:
```bash
source venv/bin/activate
```

### **Problem 6: Setup script won't run (Windows)**
- Right-click `setup.bat` → **"Run as administrator"**

### **Problem 7: Packages fail to install**
Try installing one by one:
```bash
pip install flask
pip install scikit-learn
pip install pandas
pip install numpy
```

---

## 🔄 UPDATING THE APPLICATION

To update packages:
```bash
# Activate virtual environment first
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Update packages
pip install --upgrade flask scikit-learn pandas numpy
```

---

## 🧹 CLEANING UP

### **To remove virtual environment:**
Simply delete the `venv` folder

### **To reinstall:**
Run setup script again

---

## 💡 TIPS

1. **Always activate virtual environment** before running the app
2. **Don't delete the venv folder** - it contains all installed packages
3. **Use Quick Test first** - easiest way to verify everything works
4. **Keep terminal open** while using the app
5. **Press Ctrl+C** to stop the server

---

## 📊 WHAT YOU'RE RUNNING

- **Backend:** Flask (Python web framework)
- **ML Model:** Random Forest (99.96% accuracy)
- **Frontend:** HTML5, CSS3, JavaScript
- **Dependencies:** scikit-learn, pandas, numpy

---

## 🎓 VIRTUAL ENVIRONMENT BENEFITS

✅ **Isolated:** Doesn't affect your system Python
✅ **Clean:** Only installs what this project needs
✅ **Safe:** Can delete and recreate anytime
✅ **Portable:** Works the same on any computer
✅ **Professional:** Industry best practice

---

## 📞 STILL HAVING ISSUES?

Check these:
1. ✅ Python 3.8+ installed?
2. ✅ In correct folder?
3. ✅ Virtual environment activated? (see `(venv)` in prompt)
4. ✅ All files present? (app.py, templates/, static/, etc.)
5. ✅ Internet connection working? (for package installation)

---

## 🎉 SUCCESS CHECKLIST

- [ ] Setup script ran successfully
- [ ] Virtual environment created (venv folder exists)
- [ ] Packages installed (no errors)
- [ ] App starts without errors
- [ ] Browser opens to http://localhost:5000
- [ ] Can see the fraud detection interface
- [ ] Quick Test examples work
- [ ] Can check custom transactions

---

## 📝 COMMAND REFERENCE

| Action | Windows | Mac/Linux |
|--------|---------|-----------|
| Setup | `setup.bat` | `./setup.sh` |
| Run | `run.bat` | `./run.sh` |
| Activate venv | `venv\Scripts\activate` | `source venv/bin/activate` |
| Deactivate venv | `deactivate` | `deactivate` |
| Stop server | `Ctrl + C` | `Ctrl + C` |

---

**Last Updated:** February 2026
**Version:** 1.0.0

**Ready to start? Run the setup script for your OS! 🚀**
