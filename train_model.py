from sklearn.ensemble import IsolationForest
from preprocessing.preprocess_data import preprocess_data
from models.model_utils import save_model
import joblib

def train_model():
    # Preprocess the data
    file_path = 'data/system_health.csv'
    X_train, X_test, y_train, y_test, scaler = preprocess_data(file_path)

    # Train the Isolation Forest model
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X_train)

    # Save the trained model and scaler using the save_model function
    save_model(model, 'anomaly_detection.pkl')  # Save model to models/anomaly_detection.pkl
    save_model(scaler, 'scaler.pkl')            # Save scaler to models/scaler.pkl

if __name__ == "__main__":
    train_model()
