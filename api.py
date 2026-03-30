from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Dummy training data
data = np.array([
    [100,1],[200,2],[5000,10],[7000,12],
    [150,1],[300,2],[9000,15],[120,1],
    [4000,8],[250,2]
])

model = IsolationForest(contamination=0.3)
model.fit(data)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    amount = input_data['amount']
    frequency = input_data['frequency']

    prediction = model.predict([[amount, frequency]])
    fraud = True if prediction[0] == -1 else False

    return jsonify({
        "fraud": fraud
    })

if __name__ == '__main__':
    app.run(port=5000)