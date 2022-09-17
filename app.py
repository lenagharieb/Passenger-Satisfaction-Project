import joblib
from flask import Flask, render_template, request
import preprocess
import numpy as np 

app=Flask(__name__)



model=joblib.load('models/rffmodel.h5')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods= ['POST','GET'])
def get_prediction():
    if request.method=='POST':
        Flight_Distance= request.form['Flight Distance']
        Inflight_wifi_service=request.form['Inflight wifi service']
        Departure_Arrival_time_convenient=request.form['Departure/Arrival time convenient']
        Ease_of_Online_booking=request.form['Ease of Online booking']
        Gate_location=request.form['Gate location']
        Food_drink=request.form['Food and drink']
        Online_boarding=request.form['Online boarding']
        Seat_comfort=request.form['Seat comfort']
        Inflight_entertainment=request.form['Inflight entertainment']
        Onboard_service=request.form['On-board service']
        Legroom_service=request.form['Leg room service']
        Baggage_handling=request.form['Baggage handling']
        Checkin_service=request.form['Checkin service']
        Inflight_service=request.form['Inflight service']
        Cleanliness=request.form['Cleanliness']
        Departure_Delay_Minutes=request.form['Departure Delay in Minutes']
        Age_category=request.form['Age_category']
        CustomerType=request.form['CustomerType']
        Class_new=request.form['Class_new']
        Type_of_travel=request.form['Type of travel']
    
    data={'Flight Distance':Flight_Distance, 'Inflight wifi service':Inflight_wifi_service,'Departure/Arrival time convenient':Departure_Arrival_time_convenient,'Ease of Online booking':Ease_of_Online_booking, 'Gate location':Gate_location,'Food and drink':Food_drink,'Online boarding':Online_boarding,'Seat comfort':Seat_comfort,'Inflight entertainment':Inflight_entertainment,'On-board service':Onboard_service,'Leg room service':Legroom_service,'Baggage handling':Baggage_handling,'Checkin service':Checkin_service,'Inflight service':Inflight_service,'Cleanliness':Cleanliness,'Departure Delay in Minutes':Departure_Delay_Minutes, 'age' :int(Age_category),'customer':CustomerType,'customerclass':Class_new,'traveltype':Type_of_travel }
    print(data)
    
    final_data= preprocess.preprocess_data(data)
    print(final_data)
   




    prediction=model.predict([final_data])

    d={'0':'Unsatisfied','1':'satisfied' }

    print(prediction, prediction.dtype, prediction[0])

    return render_template('prediction.html',satisfaction=d[ str(prediction[0]) ]  ) 



if __name__=='__main__':
    app.run(debug= True)



