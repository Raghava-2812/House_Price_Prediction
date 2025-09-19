from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import joblib
import os

app = Flask(__name__)
CORS(app)

# -------------------------------
# Load training data and train model
# -------------------------------
train = pd.read_csv('train.csv')

# Select numeric features only for simplicity
FEATURES = ['LotArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
            '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
            'FullBath', 'HalfBath', 'BedroomAbvGr', 'GarageArea',
            'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
            'ScreenPorch', 'PoolArea']

X = train[FEATURES]
y = train['SalePrice']

# Handle missing values
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and imputer for reuse
if not os.path.exists('model'):
    os.mkdir('model')
joblib.dump(model, 'model/house_model.pkl')
joblib.dump(imputer, 'model/imputer.pkl')

# -------------------------------
# Routes
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Build a list in the order of FEATURES
        input_data = [[
            data.get('LotArea', 0),
            data.get('BsmtFinSF1', 0),
            data.get('BsmtFinSF2', 0),
            data.get('BsmtUnfSF', 0),
            data.get('TotalBsmtSF', 0),
            data.get('1stFlrSF', 0),
            data.get('2ndFlrSF', 0),
            data.get('LowQualFinSF', 0),
            data.get('GrLivArea', 0),
            data.get('FullBath', 0),
            data.get('HalfBath', 0),
            data.get('BedroomAbvGr', 0),
            data.get('GarageArea', 0),
            data.get('WoodDeckSF', 0),
            data.get('OpenPorchSF', 0),
            data.get('EnclosedPorch', 0),
            data.get('3SsnPorch', 0),
            data.get('ScreenPorch', 0),
            data.get('PoolArea', 0)
        ]]


        # Transform using imputer
        input_data = imputer.transform(input_data)

        # Predict
        pred = model.predict(input_data)
        return jsonify({'SalePrice': float(pred[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
