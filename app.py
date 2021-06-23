import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import dill as pickle
import jsonify
import requests
import sklearn


app = Flask(__name__)
model = pickle.load(open('Cartest_Model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
     if request.method == 'POST':
         
         Year = int(request.form['Year'])
         Present_Price=float(request.form['Present_Price'])
         Kms_Driven=int(request.form['Kms_Driven'])
         Owner=int(request.form['Owner'])
         Fuel_Type=request.form['Fuel_Type']
         Seller_Type=request.form['Seller_Type']
         Transmission=request.form['Transmission']
         
         d = {'Year': Year,'Present_Price' : Present_Price,'Kms_Driven': Kms_Driven,'Fuel_Type' : Fuel_Type,
              'Seller_Type' : Seller_Type,'Transmission' : Transmission,'Owner' : Owner}
         
         data = pd.DataFrame(d,index = [0])
         
         prediction=model.predict(data)
         output=round(prediction[0],2)
         if output<0:
             
             return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
         else:
             
             return render_template('index.html',prediction_text="Predicted Selling Price is  {} Lakhs".format(output))
         
     else:
         
        
         return render_template('index.html')
    
if __name__=="__main__":
    
    app.run(debug=True)


