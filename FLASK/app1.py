#importing the necessary dependencies
import numpy as np
from flask import Flask,request,render_template
import pickle
import os
import pandas as pd
app=Flask(__name__)#initializing a flask app
model=pickle.load(open'cement.pkl','rb')))
@app.route('/')#route to display the home page
def home():
    return render_template("index.html")
@app.route('/predict',methods=['POST','GET'])#route to show the predictions in a web UI
def prediction():
    
return render_template('index1.html')
   @app.route('/predict',methods=['POST','GET'])
   def my_home();
   return render_template('home.html')
   @app.route('/predict',methods=['POST'])#route to show the prediction in aweb UI
  
     def index():
         #reading the input given by the user
    input_features=[float(x) for x in request.form.values()]
    features_value=[np.array(input_features)]
    features_name=['cement','blast furnace slag','fly flash','water','superplasticizer','coarse aggregate','fine aggregate','age']
    def prediction():
        return render_template('index1.html')
    @app.route('/home',methods=['POST','GET'])
    def my_home():
        return render_template('home.html')
        @app.route('/predict',methods=['POST'])
       def index():
           #reading the input given by the user
           input_features=[float(x) for x in request.form.values()]
           features_value=[np.array(input_features)]
           features_name=['cement','blast furnace slag','fly ash','water','superplasticizer','coarse aggregate','fine aggregate','age']
           x=pd.Dataframe(features_value,columns=features_name)
           x_log=np.log(x)#performing log transformation
           #predictions using the loaded model file
           prediction=model.predict(x_log)
           print('prediction is',predition)
           #showing the prediction results in UI
           return render_template('result2.html',prediction_text=prediction)
       if__name__=="__main__":
           #app.run(host='127.0.0.1',port=8001,debug=true)
           #app.run(debug=false)#running the app 
           app.run('0.0.0.0.8080')#local host 8080