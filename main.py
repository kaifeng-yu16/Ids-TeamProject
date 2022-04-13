# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

import mlflow
import pandas as pd
from flask import Flask, request, render_template

def predict(BMI, Smoking, AlcoholDrinking, Stroke,
            PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
            Diabetic, PhysicalActivity, GenHealth, SleepTime,
            Asthma, KidneyDisease, SkinCancer):
    my_data = {
        "BMI": {0: BMI},
        "Smoking": {0: Smoking},
        "AlcoholDrinking": {0: AlcoholDrinking},
        "Stroke": {0: Stroke},
        "PhysicalHealth": {0: PhysicalHealth},
        "MentalHealth": {0: MentalHealth},
        "DiffWalking": {0: DiffWalking},
        "Sex": {0: Sex},
        "AgeCategory": {0: AgeCategory},
        "Diabetic": {0: Diabetic},
        "PhysicalActivity": {0: PhysicalActivity},
        "GenHealth": {0: GenHealth},
        "SleepTime": {0: SleepTime},
        "Asthma": {0: Asthma},
        "KidneyDisease": {0: KidneyDisease},
        "SkinCancer": {0: SkinCancer},
    }
    
    data = pd.DataFrame(data=my_data)
    data["BMI"] = pd.to_numeric(data["BMI"]).astype(float, errors = 'raise')
    data["Smoking"] = pd.to_numeric(data["Smoking"]).astype('int32', errors = 'raise')
    data["AlcoholDrinking"] = pd.to_numeric(data["AlcoholDrinking"]).astype('int32', errors = 'raise')
    data["Stroke"] = pd.to_numeric(data["Stroke"]).astype('int32', errors = 'raise')
    data["PhysicalHealth"] = pd.to_numeric(data["PhysicalHealth"]).astype('int32', errors = 'raise')
    data["MentalHealth"] = pd.to_numeric(data["MentalHealth"]).astype('int32', errors = 'raise')
    data["DiffWalking"] = pd.to_numeric(data["DiffWalking"]).astype('int32', errors = 'raise')
    data["Sex"] = pd.to_numeric(data["Sex"]).astype('int32', errors = 'raise')
    data["AgeCategory"] = pd.to_numeric(data["AgeCategory"]).astype('int32', errors = 'raise')
    data["Diabetic"] = pd.to_numeric(data["Diabetic"]).astype('int32', errors = 'raise')
    data["PhysicalActivity"] = pd.to_numeric(data["PhysicalActivity"]).astype('int32', errors = 'raise')
    data["GenHealth"] = pd.to_numeric(data["GenHealth"]).astype('int32', errors = 'raise')
    data["SleepTime"] = pd.to_numeric(data["SleepTime"]).astype('float', errors = 'raise')
    data["Smoking"] = pd.to_numeric(data["Smoking"]).astype('int32', errors = 'raise')
    data["Asthma"] = pd.to_numeric(data["Asthma"]).astype('int32', errors = 'raise')
    data["KidneyDisease"] = pd.to_numeric(data["KidneyDisease"]).astype('int32', errors = 'raise')
    data["SkinCancer"] = pd.to_numeric(data["SkinCancer"]).astype('int32', errors = 'raise')
    result = loaded_model.predict(pd.DataFrame(data))
    return result

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')
app = Flask(__name__)

@app.route("/predict", methods=["GET", "POST"])
def do_predict():
    if request.method == "POST":
        BMI = request.form["BMI"]
        Smoking = request.form["Smoking"]
        AlcoholDrinking = request.form["AlcoholDrinking"]
        Stroke = request.form["Stroke"]
        PhysicalHealth = request.form["PhysicalHealth"]
        MentalHealth = request.form["MentalHealth"]
        DiffWalking = request.form["DiffWalking"]
        Sex = request.form["Sex"]
        AgeCategory = request.form["AgeCategory"]
        Diabetic = request.form["Diabetic"]
        PhysicalActivity = request.form["PhysicalActivity"]
        GenHealth = request.form["GenHealth"]
        SleepTime = request.form["SleepTime"]
        Asthma = request.form["Asthma"]
        KidneyDisease = request.form["KidneyDisease"]
        SkinCancer = request.form["SkinCancer"]
        res = predict(BMI, Smoking, AlcoholDrinking, Stroke,
                      PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
                      Diabetic, PhysicalActivity, GenHealth, SleepTime,
                      Asthma, KidneyDisease, SkinCancer)
        if (res == 0):
            res = "You are not likely to have a heart attack!"
        else:
            res = "High risk of a heart attack!"
        return render_template("predict.html", name=1, res=res)
    return render_template("predict.html", name=0)
    
@app.route("/")
def main_menu():
    return render_template("main_menu.html", name=0)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
