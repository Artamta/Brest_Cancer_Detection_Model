
from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return "App is running!"

@app.route('/predict', methods=['POST'])
def predict():
    error = None
    message = None
    features = request.form.get('feature', '')
    try:
        features_list = [float(x.strip()) for x in features.split(',') if x.strip()]
        if len(features_list) != 30:
            error = "Please enter exactly 30 features separated by commas."
        else:
            np_features = np.asarray(features_list, dtype=np.float32)
            pred = model.predict(np_features.reshape(1, -1))
            message = ['Malignant' if pred[0] == 1 else 'Benign']
    except Exception as e:
        error = f"Invalid input: {str(e)}"
    return render_template('index.html', message=message, error=error)

if __name__ == '__main__':
    app.run(debug=True)

