from flask import Flask, render_template, url_for, request, jsonify, redirect
from joblib import dump, load
import numpy as np
from flask import Flask, render_template

model = load('model.joblib') 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])

def prediction():
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        if "input" in data:
            value = data['input']
            prediction = model.predict(value)
            response =  {
            "Predictions": str(prediction)}                 
            for i in range(len(value)):
                print(f'Our predictions for {str(value[i])} wine characteristics is {prediction[i]} ')
            return jsonify(response), 200
        else: 
            return jsonify("Your Data doesn't match the right format. You should read our documentation.")
    
    else:
        return jsonify("We need JSON data to make predictions")
    
@app.route("/estimator", methods=["GET" , "POST"])
def form():   
    if request.method == "POST":
        user_data = { "input" : [[request.form.getlist('entry')][0]]
        }
#Get estimations from user input
        user_value = user_data["input"]
        prediction = model.predict(user_value)#This is the prediction for user inputs, to display
        return render_template("estimation.html", est=str(prediction).replace('[', '').replace(']','')) #Get clean estimation
    else:
        return render_template('form.html')

'''@app.route("/estimation") #user estimations page
def estimation(result)):
    return render_template("estimation.html", est=est)'''


if __name__ == "__main__":
    app.run(debug=True)