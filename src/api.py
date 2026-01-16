from flask import Flask, request, jsonify
from ml_model import predict_water_quality # Your SVM function
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows your UI to talk to this API

@app.route('/predict', methods=['POST'])
def get_prediction():
    data = request.json
    # Get values from the UI/Sensors
    res = predict_water_quality(data['ph'], data['turbidity'], data['do'])
    return jsonify({"status": res})

if __name__ == "__main__":
    app.run(port=5000)
