import datetime as dt

def loadInitialData():
    outlet_data = [{"Outlet Name": "Outlet A", "Opening Hour": "9:00", "Closing Hour": "18:00" },
     {"Outlet Name": "Outlet B", "Opening Hour": "9:00", "Closing Hour": "18:00" }, 
     {"Outlet Name": "Outlet C", "Opening Hour": "8:00", "Closing Hour": "20:00"}]

    car_data = [{"License Plate Number": "SE001A", "Make": "Toyota", "Model": "Corolla", "Category": "Sedan", "Status": "Available", "Outlet": "Outlet A"},
     {"License Plate Number": "SE002A", "Make": "Toyota", "Model": "Corolla", "Category": "Sedan", "Status": "Available", "Outlet": "Outlet A"},
     {"License Plate Number": "SE003A", "Make": "Toyota", "Model": "Corolla", "Category": "Sedan", "Status": "Maintenance", "Outlet": "Outlet A"},
     {"License Plate Number": "SE001B", "Make": "Honda", "Model": "Civic", "Category": "Sedan", "Status": "Available", "Outlet": "Outlet B"},
     {"License Plate Number": "SE002B", "Make": "Honda", "Model": "Civic", "Category": "Sedan", "Status": "Available", "Outlet": "Outlet B"},
     {"License Plate Number": "SE003B", "Make": "Honda", "Model": "Civic", "Category": "Sedan", "Status": "Maintenance", "Outlet": "Outlet B"},
     {"License Plate Number": "SE001C", "Make": "Kia", "Model": "Cerato", "Category": "Sedan", "Status": "Available", "Outlet": "Outlet C"},
     {"License Plate Number": "SU002C", "Make": "Subaru", "Model": "Forrester", "Category": "SUV", "Status": "Available", "Outlet": "Outlet C"},
     {"License Plate Number": "MP003C", "Make": "Honda", "Model": "Odyssey", "Category": "MPV", "Status": "Available", "Outlet": "Outlet C"}]

    return outlet_data, car_data



class car:

    def __init__(self, license_plate_no, make, model, category, status, outlet) -> None:
        self._license_plate_no = license_plate_no
        self._make = make
        self._model = model
        self._category = category
        self._status = status
        self._outlet = outlet
        self._requires_transit = {}


    def getLicensePlateNo(self):
        return self._license_plate_no
    
    def setLicensePlateNo(self, license_plate_no):
        self._license_plate_no = license_plate_no
    
    def getMake(self):
        return self._make
    
    def setMake(self, make):
        self._make = make

    def getModel(self):
        return self._model
    
    def setModel(self, model):
        self._model = model

    def getCategory(self):
        return self._category
    
    def setCategory(self, category):
        self._category = category

    def getStatus(self):
        return self._status
    
    def setStatus(self, status):
        self._status = status
    
    def getOutlet(self):
        return self._outlet
    
    def setOutlet(self, outlet):
        self._outlet = outlet
    
    def setReservedDates(self, list_of_dates):
        for dates in list_of_dates:
            self._reserved_dates.append(dates) 

    def getTransitStatus(self):
        return self._requires_transit

    
    def addCar(car_list):
        while True:
            new_car_input = input("Please input car details in the following format: License Plate No., Make, Model, Category, Status, Outlet""\n""Pls use commas to separate your inputs.""\n""").strip().split(",")
            new_car = []
            license_match = False
            if len(new_car_input) == 6:
                for details in new_car_input:
                    new_car.append(details.strip())
                for cars in car_list:
                    if new_car[0].lower() == cars._license_plate_no.lower():
                        license_match = True
                        print("ERROR: License Plate number already exists")
                        break
                if license_match == True:
                    while True:
                        user_choice = input("Do you want to re-input car details? Y/N""\n""")
                        if user_choice in ["Y", "N"]:
                            break
                        else:
                            print("ERROR: you have entered an invalid input, Please try again ""\n""")
                            continue
                    if user_choice == "Y":
                        continue
                    else:
                        return  

                elif license_match == False:
                    if new_car[5].lower() in ["outlet a", "outlet b", "outlet c"] and new_car[4].lower() in ["available", "allocated", "pickup", "maintenance"] and new_car[3].lower() in ["sedan", "suv", "mpv"]:
                        car_list.append(car(new_car[0],new_car[1],new_car[2],new_car[3],new_car[4],new_car[5]))
                        print("Car successfully added to database""\n""")
                        break
                    elif new_car[5].lower() not in ["outlet a", "outlet b", "outlet c"]:
                        print("ERROR: You have entered an invalid input for Outlet, Please try again""\n""")
                        break
                    elif new_car[4].lower() not in ["available", "allocated", "pickup", "maintenance"]:
                        print("ERROR: You have entered an invalid input for Status, Please try again""\n""")
                        break
                    elif new_car[3].lower() not in ["sedan", "suv", "mpv"]:
                        print("ERROR: You have entered an invalid input for Category, Please try again""\n""")
                        break
            elif len(new_car_input) < 6:
                print("ERROR: You have entered fewer car details than expected, Please try again""\n""")
                continue
            else:
                print("ERROR: You have entered more car details than expected, Please try again""\n""")
                continue

    def reserveCarCheck(car_list, reservations_list):
        customer_input = input("Please input the following details (with commas separating each detail): Name, Car Category, Pickup date/time, Return date/time, Pickup Outlet, Return Outlet""\n""").strip().split(",")
        customer_input_details = []
        if len(customer_input) == 6:
            for details in customer_input:
                customer_input_details.append(details.strip())
            if customer_input_details[1].lower() not in ["sedan", "suv", "mpv"]:
                print("ERROR: You have entered an invalid input for Category, Please try again""\n""")
                return None, None, None, None , None, None,None,None 
            elif customer_input_details[4].lower() not in ["outlet a", "outlet b", "outlet c"]:
                print("ERROR: You have entered an invalid input for Pickup Outlet, Please try again""\n""")
                return None, None, None, None , None, None,None,None 
            elif customer_input_details[5].lower() not in ["outlet a", "outlet b", "outlet c"]:
                print("ERROR: You have entered an invalid input for Return Outlet, Please try again""\n""")
                return None, None, None, None , None, None,None,None 
            else:
                try:
                    customer_input_details[2] = dt.datetime.strptime(customer_input_details[2], '%d/%m/%y %H:%M')
                    customer_input_details[3] = dt.datetime.strptime(customer_input_details[3], '%d/%m/%y %H:%M')
                except ValueError:
                    print("ERROR: You have entered an invalid date/time format, Please ensure it is entered as dd/mm/yy HH:MM""\n""")
                    return None, None, None, None , None, None,None,None 
                else:
                    pickup_outlet = customer_input_details[4].lower()
                    return_outlet = customer_input_details[5].lower()
                    pickup_time = customer_input_details[2].time()
                    pickup_datetime = customer_input_details[2]
                    return_datetime = customer_input_details[3]
                    return_time = customer_input_details[3].time()
                    category = customer_input_details[1].lower()

                    if pickup_outlet in ["outlet a", "outlet b"]:
                        if pickup_time < dt.time(hour=9) or pickup_time > dt.time(hour=18):
                            print("Not Available (Outside Outlet Operating Hours)")
                            return None, None, None, None , None, None,None,None    

                    elif pickup_outlet in ["outlet c"]:
                        if pickup_time < dt.time(hour=8) or pickup_time > dt.time(hour=20):
                            print("Not Available (Outside Outlet Operating Hours)")
                            return None, None, None, None , None, None,None,None 

                    if return_outlet in ["outlet a", "outlet b"]:
                        if return_time < dt.time(hour=9) or return_time > dt.time(hour=18):
                            print("Not Available (Outside Outlet Operating Hours)")
                            return None, None, None, None , None, None,None,None 

                    elif return_outlet in ["outlet c"]:
                        if return_time < dt.time(hour=8) or return_time > dt.time(hour=20):
                            print("Not Available (Outside Outlet Operating Hours)")
                            return None, None, None, None , None, None,None,None 

                    potential_car_list = []
                    for cars in car_list:
                        if category == cars._category.lower() and cars._status.lower() != "maintenance":
                            potential_car_list.append(cars)
                    if len(potential_car_list) == 0:
                        print("Car not available")
                        return None, None, None, None , None, None,None, None 
                    else:
                        cars_available_same_outlet = []
                        cars_available_another_outlet = []
                        
                        if len(reservations_list) == 0:
                            for cars in potential_car_list:
                                if cars._outlet.lower() == pickup_outlet:
                                    cars_available_same_outlet.append(cars)
                                else:
                                    cars_available_another_outlet.append(cars)
                            if len(cars_available_same_outlet) != 0:
                                reserved_car = cars_available_same_outlet[0]
                                rental_days = return_datetime - pickup_datetime
                                return reserved_car, rental_days.total_seconds()/86400, pickup_datetime.date(), return_datetime.date(), pickup_outlet, return_outlet, pickup_time, return_time
                            
                            elif len(cars_available_another_outlet) != 0:
                                reserved_car = cars_available_another_outlet[0]
                                rental_days = return_datetime - pickup_datetime
                                return reserved_car, rental_days.total_seconds()/86400, pickup_datetime.date(), return_datetime.date(), pickup_outlet, return_outlet, pickup_time, return_time

 
                        else:
                            final_car_list = []
                            
                            for cars in potential_car_list:
                                car_available = True
                                for reservations in reservations_list:
                                    if cars._license_plate_no.lower() != reservations["License Plate"].lower():
                                        
                                        continue
                                    else:
                                        if pickup_datetime.date() > reservations["Return Date"]:
                                            
                                            continue
                                        elif pickup_datetime.date() == reservations["Return Date"]:
                                            if pickup_outlet == reservations["Return Outlet"].lower() and pickup_time >= reservations["Return Time"]:
                                                continue
                                            elif pickup_outlet != reservations["Return Outlet"].lower() and (pickup_datetime - dt.timedelta(hours=2)).time() >= reservations["Return Time"]:
                                                cars._requires_transit[pickup_datetime.date()] = reservations["Return Outlet"]
                                                continue
                                            else:
                                                car_available = False

                                        elif pickup_datetime.date() < reservations["Return Date"] and pickup_datetime.date() >= reservations["Pickup Date"]:
                                            car_available = False
                                        elif pickup_datetime.date() < reservations["Pickup Date"] and return_datetime.date() > reservations["Pickup Date"]:
                                            car_available = False
                                        elif pickup_datetime.date() < reservations["Pickup Date"] and return_datetime.date() == reservations["Pickup Date"]:
                                            if return_outlet == reservations["Pickup Outlet"].lower() and return_time <= reservations["Pickup Time"]:
                                                continue
                                            elif return_outlet != reservations["Pickup Outlet"].lower() and (return_datetime + dt.timedelta(hours=2)).time() <= reservations["Pickup Time"]:
                                                continue
                                            else:
                                               car_available = False
                                        else:
                                            continue 
                                if car_available == True:
                                    final_car_list.append(cars)
                            
                            if len(final_car_list) == 0:
                               print("Car not available")
                               return None, None, None, None , None, None, None, None
                            else:
                                for cars in final_car_list:
                                    if cars._outlet.lower() == pickup_outlet:
                                        cars_available_same_outlet.append(cars)
                                    else:
                                        cars_available_another_outlet.append(cars)
                                if len(cars_available_same_outlet) != 0:
                                    reserved_car = cars_available_same_outlet[0]
                                    rental_days = return_datetime - pickup_datetime
                                    return reserved_car, rental_days.total_seconds()/86400, pickup_datetime.date(), return_datetime.date(), pickup_outlet, return_outlet, pickup_time, return_time
                            
                                elif len(cars_available_another_outlet) != 0:
                                    reserved_car = cars_available_another_outlet[0]
                                    rental_days = return_datetime - pickup_datetime
                                    return reserved_car, rental_days.total_seconds()/86400, pickup_datetime.date(), return_datetime.date(), pickup_outlet, return_outlet, pickup_time, return_time


        elif len(customer_input)> 6:
            print("ERROR: You have entered more inputs then expected")
            return None, None, None, None , None, None,None, None 
        else:
            print("ERROR: You have entered fewer inputs than expected")
            return None, None, None, None , None, None,None, None 