from flask import Flask, request, jsonify,render_template
import pickle
import numpy as np


app = Flask(__name__)


with open("models/uti_model_scaled.pkl", "rb") as file:
    data = pickle.load(file)

model = data.get("model") 
scaler = data.get("scaler")  

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", result="")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        gender_map = {"Male": 1, "Female": 0}
        yes_no_map = {"Yes": 1, "No": 0}

        input_data = np.array([
            gender_map[request.form["gender"]], 
            int(request.form["age"]),
            yes_no_map[request.form["fever"]],  
            yes_no_map[request.form["abdominal_pain"]],
            yes_no_map[request.form["dysuria"]],
            yes_no_map[request.form["chronic_renal_failure"]],
            float(request.form["serum_creatinine"]),
            float(request.form["wbc_count"]),
            yes_no_map[request.form["diabetes_mellitus"]]
        ]).reshape(1, -1)

   
        input_data[:, [6, 7]] = scaler.transform(input_data[:, [6, 7]])

        prediction = model.predict(input_data)[0]
        result = "UTI Detected" if prediction == 1 else "No UTI Detected"

        return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
