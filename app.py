import os
from flask import Flask, jsonify, render_template
import pandas as pd
from models.model_utils import load_model

app = Flask(__name__)

# Correctly join the paths for loading the model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'anomaly_detection.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'scaler.pkl')

# Load the trained model and scaler from the models folder
model = load_model(model_path)
scaler = load_model(scaler_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    # Simulate real-time data (replace with actual data from sensors)
    incoming_data = {'cpu_usage': 92, 'temperature': 77.5}
    features = pd.DataFrame([incoming_data])
    scaled_features = scaler.transform(features)

    # Predict anomaly using the loaded model
    prediction = model.predict(scaled_features)
    is_anomaly = "Yes" if prediction[0] == -1 else "No"

    return jsonify({'data': incoming_data, 'is_anomaly': is_anomaly})

if __name__ == '__main__':
    print("Starting Flask app...")  # Ensure this message is printed
    app.run(debug=True)
