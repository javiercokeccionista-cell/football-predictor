
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('models/xgb_cal.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    preds = model.predict_proba(df)[0]
    response = {
        "model_prob": {
            "home": float(preds[0]),
            "draw": float(preds[1]),
            "away": float(preds[2])
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
