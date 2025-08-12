import os
import numpy as np
import joblib
from flask import Flask, render_template, request
MODEL_PATH = os.path.join('artifacts', 'model', 'model.pkl')
model = None
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = joblib.load(f)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('predict_form.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            # Get form data
            delay_ratio = request.form["Delay Ratio"]
            flight_distance = request.form["Flight Distance"]
            features = [
                float(request.form["Online Boarding"]),
                float(delay_ratio),
                float(request.form["Inflight wifi service"]),
                float(request.form["Class"]),
                float(request.form["Type of Travel"]),
                float(request.form["Inflight entertainment"]),
                float(flight_distance),
                float(request.form["Seat comfort"]),
                float(request.form["Leg room service"]),
                float(request.form["On-board service"]),
                float(request.form["Cleanliness"]),
                float(request.form["Ease of Online Booking"])
            ]
            input_array = np.array([features])
            if model:
                pred = model.predict(input_array)[0]
                if str(pred) == '1':
                    prediction = "Prediction: The passenger is likely to be SATISFIED."
                elif str(pred) == '0':
                    prediction = "Prediction: The passenger is likely to be NEUTRAL or DISSATISFIED."
                else:
                    prediction = f"Prediction: {pred}"
            else:
                prediction = "Model not found."
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template('predict_form.html', prediction=prediction)
if __name__ == '__main__':
    app.run(debug=True)
