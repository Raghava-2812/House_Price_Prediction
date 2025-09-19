from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# -------------------------------
# Load pre-trained model & imputer
# -------------------------------
MODEL_PATH = 'model/house_model.pkl'
IMPUTER_PATH = 'model/imputer.pkl'

if not os.path.exists(MODEL_PATH) or not os.path.exists(IMPUTER_PATH):
    raise FileNotFoundError("Model or imputer not found. Run House_price_prediction.py first!")

model = joblib.load(MODEL_PATH)
imputer = joblib.load(IMPUTER_PATH)

FEATURES = ['LotArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
            '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
            'FullBath', 'HalfBath', 'BedroomAbvGr', 'GarageArea',
            'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
            'ScreenPorch', 'PoolArea']

# -------------------------------
# API Route
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Build feature array in the same order as FEATURES
        input_data = [[
            data.get(f, 0) for f in FEATURES
        ]]

        # Transform with imputer (handle missing values)
        input_data = imputer.transform(input_data)

        # Predict
        pred = model.predict(input_data)
        return jsonify({'SalePrice': float(pred[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# -------------------------------
# Run server
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
