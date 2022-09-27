import json
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import tensorflow as tf

# Initiating app
app = Flask(__name__)
# Loading the model
coffee_model = tf.keras.models.load_model("./saved_model")

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    output = coffee_model.predict(np.array(list(data.values())).reshape(1,-1))
    print(output[0])
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug=True)