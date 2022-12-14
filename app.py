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
    prediction = coffee_model.predict(np.array(list(data.values())).reshape(1,-1))
    print(prediction)
    if prediction >= 0.5:
        return "Good Roast"
    else:
        return "Bad Roast"

@app.route('/predict_roast', methods=['POST'])

def predict_roast():
    data = [float(x) for x in request.form.values()]
    print(data)
    prediction = coffee_model.predict(np.array(data).reshape(1,-1))
    print(prediction)
    if prediction >= 0.5:
        return render_template("home.html", predicted_roast = "The coffee will be roasted nicely")
    else:
        return render_template("home.html", predicted_roast = "Not a properly roasted coffee")

if __name__ == '__main__':
    app.run(debug=True)