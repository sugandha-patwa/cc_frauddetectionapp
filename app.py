from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import json
from datetime import datetime

app = Flask(__name__)

# Load the trained model
with open('fraud_detection_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
scaler = model_data['scaler']
feature_names = model_data['feature_names']

# Feature descriptions for the form
FEATURE_INFO = {
    'amount': {'label': 'Transaction Amount (₹)', 'placeholder': '1000', 'type': 'number', 'min': 0},
    'time': {'label': 'Transaction Time (seconds from midnight)', 'placeholder': '43200', 'type': 'number', 'min': 0, 'max': 86400},
    'V1': {'label': 'Feature V1', 'placeholder': '0.5', 'type': 'number', 'step': '0.01'},
    'V2': {'label': 'Feature V2', 'placeholder': '-0.3', 'type': 'number', 'step': '0.01'},
    'V3': {'label': 'Feature V3', 'placeholder': '0.2', 'type': 'number', 'step': '0.01'},
    'V4': {'label': 'Feature V4', 'placeholder': '-0.1', 'type': 'number', 'step': '0.01'},
    'V5': {'label': 'Feature V5', 'placeholder': '0.4', 'type': 'number', 'step': '0.01'},
    'V6': {'label': 'Feature V6', 'placeholder': '0.0', 'type': 'number', 'step': '0.01'},
    'V7': {'label': 'Feature V7', 'placeholder': '-0.2', 'type': 'number', 'step': '0.01'},
    'V8': {'label': 'Feature V8', 'placeholder': '0.3', 'type': 'number', 'step': '0.01'},
    'V9': {'label': 'Feature V9', 'placeholder': '0.1', 'type': 'number', 'step': '0.01'},
    'V10': {'label': 'Feature V10', 'placeholder': '-0.4', 'type': 'number', 'step': '0.01'},
    'distance_from_home': {'label': 'Distance from Home (km)', 'placeholder': '5', 'type': 'number', 'min': 0},
    'distance_from_last_transaction': {'label': 'Distance from Last Transaction (km)', 'placeholder': '2', 'type': 'number', 'min': 0},
    'ratio_to_median_purchase_price': {'label': 'Ratio to Median Purchase Price', 'placeholder': '1.0', 'type': 'number', 'step': '0.1', 'min': 0},
    'repeat_retailer': {'label': 'Repeat Retailer?', 'type': 'select', 'options': [('0', 'No'), ('1', 'Yes')]},
    'used_chip': {'label': 'Used Chip?', 'type': 'select', 'options': [('0', 'No'), ('1', 'Yes')]},
    'used_pin_number': {'label': 'Used PIN?', 'type': 'select', 'options': [('0', 'No'), ('1', 'Yes')]},
    'online_order': {'label': 'Online Order?', 'type': 'select', 'options': [('0', 'No'), ('1', 'Yes')]},
}

def get_risk_level(probability):
    """Categorize risk level based on fraud probability"""
    if probability < 0.3:
        return 'LOW', '#28a745'
    elif probability < 0.6:
        return 'MEDIUM', '#ffc107'
    elif probability < 0.85:
        return 'HIGH', '#fd7e14'
    else:
        return 'CRITICAL', '#dc3545'

@app.route('/')
def index():
    """Main page with transaction input form"""
    return render_template('index.html', features=FEATURE_INFO, feature_names=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    """Process transaction and return fraud prediction"""
    try:
        # Get form data
        transaction_data = []
        for feature in feature_names:
            value = request.form.get(feature)
            if value is None or value == '':
                return jsonify({'error': f'Missing value for {feature}'}), 400
            transaction_data.append(float(value))
        
        # Scale the input
        transaction_scaled = scaler.transform([transaction_data])
        
        # Make prediction
        prediction = model.predict(transaction_scaled)[0]
        probability = model.predict_proba(transaction_scaled)[0]
        
        # Get risk level
        risk_level, risk_color = get_risk_level(probability[1])
        
        # Prepare response
        result = {
            'is_fraud': bool(prediction),
            'fraud_probability': float(probability[1]) * 100,
            'legitimate_probability': float(probability[0]) * 100,
            'risk_level': risk_level,
            'risk_color': risk_color,
            'prediction_text': 'FRAUDULENT' if prediction else 'LEGITIMATE',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'transaction_data': dict(zip(feature_names, transaction_data))
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/quick-test')
def quick_test():
    """Page with preset transaction examples"""
    # Preset examples
    examples = {
        'legitimate': {
            'name': 'Legitimate Transaction',
            'description': 'Small purchase at regular retailer with chip and PIN',
            'data': {
                'amount': 35.50,
                'time': 43200,
                'V1': 0.1, 'V2': -0.2, 'V3': 0.3, 'V4': -0.1, 'V5': 0.2,
                'V6': 0.0, 'V7': -0.1, 'V8': 0.1, 'V9': 0.0, 'V10': -0.2,
                'distance_from_home': 3.5,
                'distance_from_last_transaction': 2.0,
                'ratio_to_median_purchase_price': 1.1,
                'repeat_retailer': 1,
                'used_chip': 1,
                'used_pin_number': 1,
                'online_order': 0
            }
        },
        'suspicious': {
            'name': 'Suspicious Transaction',
            'description': 'Large online purchase from new retailer, far from home',
            'data': {
                'amount': 1250.00,
                'time': 82800,
                'V1': 2.3, 'V2': -1.9, 'V3': 1.8, 'V4': -2.1, 'V5': 1.5,
                'V6': -1.2, 'V7': 2.0, 'V8': 0.8, 'V9': -1.3, 'V10': 1.9,
                'distance_from_home': 150.0,
                'distance_from_last_transaction': 80.0,
                'ratio_to_median_purchase_price': 5.2,
                'repeat_retailer': 0,
                'used_chip': 0,
                'used_pin_number': 0,
                'online_order': 1
            }
        },
        'moderate': {
            'name': 'Moderate Risk Transaction',
            'description': 'Medium purchase at unusual location',
            'data': {
                'amount': 185.00,
                'time': 54000,
                'V1': 1.2, 'V2': -0.8, 'V3': 0.9, 'V4': -1.1, 'V5': 0.7,
                'V6': -0.5, 'V7': 1.0, 'V8': 0.3, 'V9': -0.6, 'V10': 0.8,
                'distance_from_home': 45.0,
                'distance_from_last_transaction': 30.0,
                'ratio_to_median_purchase_price': 2.5,
                'repeat_retailer': 0,
                'used_chip': 1,
                'used_pin_number': 0,
                'online_order': 0
            }
        }
    }
    return render_template('quick_test.html', examples=examples)

@app.route('/dashboard')
def dashboard():
    """Dashboard showing model performance metrics"""
    return render_template('dashboard.html')

@app.route('/about')
def about():
    """About page with project information"""
    return render_template('about.html')

if __name__ == '__main__':
    print("="*60)
    print("CREDIT CARD FRAUD DETECTION SYSTEM")
    print("="*60)
    print("\n✓ Model loaded successfully!")
    print(f"✓ Features: {len(feature_names)}")
    print("\nStarting Flask server...")
    print("Access the application at: http://127.0.0.1:5000")
    print("="*60)
    app.run(debug=True, host='0.0.0.0', port=5000)
