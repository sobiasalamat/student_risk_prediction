import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, 'predictor', 'models', 'logistic_regression_model.pkl')
encoder_path = os.path.join(BASE_DIR, 'predictor', 'models', 'label_encoder.pkl')

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)
def predict_risk(data):
    prediction = model.predict([data])
    return prediction[0]