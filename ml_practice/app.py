import pandas as pd
import numpy as np
from flask import Flask,request
from flask_cors import CORS
application = Flask(__name__)
CORS(application)
import json
import pickle

with open('logistic_regression_model.pkl', 'rb') as f:
    model=pickle.load( f)

@application.route('/', methods=['GET'])
def welcome():
    return "welcome to test api"

@application.route('/locality', methods=['POST'])
def locality():
    p = request.get_json(force=True)
    value_input=np.array([p['gender'],p['age'],p['education'],p['currentSmoker'],p['cigsPerDay'],p['BPMeds']
    ,p['prevalentStroke'],p['prevalentHyp'],p['diabetes'],p['totChol'],p['sysBP'],p['diaBP'],p['BMI']
    ,p['heartRate'],p['glucose']]).reshape(1,-1)
    x=model.predict_proba(value_input)[0][1]
    return {'probability of getting heart disease is %== : ':int(x)*100}
        
if __name__ == '__main__':
    application.run(host="0.0.0.0",port=4005,debug=True)