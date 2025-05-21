from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoder
models = joblib.load('model.pkl')
le = joblib.load('processor_encoder.pkl')

# Define input mapping
feature_target_map = {
    'Performance': ['Processor'],
    'Camera': ['Front Camera', 'Back Camera'],
    'Battery': ['Battery Capacity'],
    'Screen_Formfactor': ['Screen Size'],
    'Multitasking': ['RAM']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract features from frontend
    ram = int(data['RAM'])
    processor = le.transform([data['Processor']])[0]
    battery = int(data['Battery'])
    front = int(data['Front Camera'])
    back = int(data['Back Camera'])
    screen = float(data['Screen Size'])

    # Map input
    input_dict = {
        'RAM': ram,
        'Processor': processor,
        'Battery Capacity': battery,
        'Front Camera': front,
        'Back Camera': back,
        'Screen Size': screen
    }

    # Predict each target using its model
    predictions = {}
    for target, features in feature_target_map.items():
        X = np.array([[input_dict[feat] for feat in features]])
        pred = round(models[target].predict(X)[0], 2)
        predictions[target] = pred

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
