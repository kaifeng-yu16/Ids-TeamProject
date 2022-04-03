# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

import mlflow
import pandas as pd
from pydantic import BaseModel
from flask import Flask, request, render_template

class Story(BaseModel):
    text: str

def predict(caffeine, calories, volume):
    my_data = {
        "volume": {0: volume},
        "calories": {0: calories},
        "caffeine": {0: caffeine},
    }
    data = pd.DataFrame(data=my_data)
    data["volume"] = pd.to_numeric(data["volume"]).astype(float, errors = 'raise')
    data["calories"] = pd.to_numeric(data["calories"]).astype('int32', errors = 'raise')
    data["caffeine"] = pd.to_numeric(data["caffeine"]).astype('int32', errors = 'raise')
    result = loaded_model.predict(pd.DataFrame(data))
    return result

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')
app = Flask(__name__)

@app.route("/predict", methods=["GET", "POST"])
def do_predict():
    if request.method == "POST":
        volume = request.form["volume"]
        calories = request.form["calories"]
        caffeine = request.form["caffeine"]
        res = predict(caffeine, calories, volume)
        return render_template("predict.html", name=1, res=res)
    return render_template("predict.html", name=0)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
