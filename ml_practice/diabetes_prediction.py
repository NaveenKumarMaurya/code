import pandas as pd
import numpy as np
from flask import Flask,request
from flask_cors import CORS
application = Flask(__name__)
CORS(application)
import json
import pickle

with open('diabetes_prediction_model.pkl','rb') as f:
    ml=pickle.load(f)

@application.route('/', methods=['GET'])
def welcome():
    return "welcome to diabetes prediction api"

@application.route('/predict', methods=['POST'])
def model_predict():
    p = request.get_json(force=True)
    value_input=np.array([p['Pregnancies'],p['Glucose'],p['BloodPressure'],p['SkinThickness'],p['Insulin'],p['BMI']
    ,p['DiabetesPedigreeFunction'],p['Age']]).reshape(1,-1)
   
    x=ml.predict(value_input)[0]
   
    if int(x)==0:
        return 'you are less prone to have diabetes'
    else:
        return 'you are more prone to get/have diabetes'
if __name__ == '__main__':
    application.run(host="0.0.0.0",port=4005,debug=True)