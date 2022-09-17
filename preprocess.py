def AgeCategory(age):
    if age in range(0,21):
        return 1
    elif age in range(21,31):
        return 2
    elif age in range(31,41):
        return 3
    elif age in range(41,51):
        return 4
    elif age in range(51,61):
        return 5
    elif age in range(61,71):
        return 6
    else:
        return 7
  


    
def customerType(customer):
    if customer =='Loyal Customer':
        return 1
    else:
        return 0

def classcategory(customerclass):
    if customerclass =='Business':
        return 1
    elif customerclass=='Eco':
        return 2
    else:
        return 0

def TypeofTravel(traveltype):
    if traveltype =='Business travel':
        return 1
    else:
        return 0

def preprocess_data(data) :
    Flight_Distance = data['Flight Distance']
    Inflight_wifi_service = data['Inflight wifi service']
    Departure_Arrival_time_convenient = data['Departure/Arrival time convenient']
    Ease_of_Online_booking = data['Ease of Online booking']
    Gate_location = data['Gate location']
    Food_drink= data['Food and drink']
    Online_boarding=data['Online boarding']
    Seat_comfort=data['Seat comfort']
    Inflight_entertainment=data['Inflight entertainment']
    Onboard_service=data['On-board service']
    Legroom_service=data['Leg room service']
    Baggage_handling=data['Baggage handling']
    Checkin_service=data['Checkin service']
    Inflight_service=data['Inflight service']
    Cleanliness=data['Cleanliness']
    Departure_Delay_Minutes=data['Departure Delay in Minutes']
    Age_category=AgeCategory(data['age'])
    CustomerType=customerType(data['customer'])
    Class_new=classcategory(data['customerclass'])
    Type_of_travel=TypeofTravel(data['traveltype'])
    
    final_data = [Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient, Ease_of_Online_booking, Gate_location, Food_drink, Online_boarding, Seat_comfort, Inflight_entertainment, Onboard_service, Legroom_service, Baggage_handling, Checkin_service,Inflight_service,Cleanliness,Departure_Delay_Minutes,Age_category,CustomerType,Class_new,Type_of_travel]
    return final_data


