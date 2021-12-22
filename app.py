import logging
from flask.wrappers import Request
from flask import request
import pandas as pd
import numpy as np
import pickle

from flask import Flask, render_template,url_for,redirect

app = Flask(__name__)
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index2')

def index2():
     return render_template('index2.html')


@app.route('/predict',methods=['POST'])


def home():


    text1=request.form['country']
    text2=request.form['edlevel']
    text3=request.form['exper']



    X = np.array([[text1,text2,text3]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)

    salary = regressor.predict(X)
    formatted_float = "${:,.2f}".format(float(salary))
 
    return render_template('index2.html',pred=formatted_float)   

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)