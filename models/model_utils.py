import joblib
import os

def save_model(model, file_name):
    """
    Save a trained model to the models directory.

    Args:
        model: The trained model to save.
        file_name (str): Name of the file to save the model as.
    """
    # Define the path to save the model
    model_path = os.path.join(os.path.dirname(__file__), file_name)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def load_model(file_name):
    """
    Load a trained model from the models directory.

    Args:
        file_name (str): Name of the file to load.

    Returns:
        The loaded model.
    """
    # Define the path to load the model
    model_path = os.path.join(os.path.dirname(__file__), file_name)
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
    return model
