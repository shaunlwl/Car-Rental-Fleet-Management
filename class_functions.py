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
            elif customer_input_details[4].lower() not in ["outlet a", "outlet b", "outlet c"]:
                print("ERROR: You have entered an invalid input for Pickup Outlet, Please try again""\n""")
            elif customer_input_details[5].lower() not in ["outlet a", "outlet b", "outlet c"]:
                print("ERROR: You have entered an invalid input for Return Outlet, Please try again""\n""")
            else:
                try:
                    customer_input_details[2] = dt.datetime.strptime(customer_input_details[2], '%d/%m/%y %H:%M')
                    customer_input_details[3] = dt.datetime.strptime(customer_input_details[3], '%d/%m/%y %H:%M')
                except ValueError:
                    print("ERROR: You have entered an invalid date/time format, Please ensure it is entered as dd/mm/yy HH:MM""\n""")
                else:
                    pickup_outlet = customer_input_details[4].lower()
                    return_outlet = customer_input_details[5].lower()
                    pickup_time = customer_input_details[2].time()
                    return_time = customer_input_details[3].time()
                    category = customer_input_details[1].lower()
                    pick_up_time_availability = False
                    return_time_availability = False
                    car_availability = False
                    if pickup_outlet in ["outlet a", "outlet b"]:
                        if pickup_time < dt.time(hour=9) or pickup_time > dt.time(hour=18):
                            print("Car not available at that time")
                            return
                        else:
                            pick_up_time_availability = True
                    elif pickup_outlet in ["outlet c"]:
                        if pickup_time < dt.time(hour=8) or pickup_time > dt.time(hour=20):
                            print("Car not available at that time")
                            return
                        else:
                            pick_up_time_availability = True
                    if return_outlet in ["outlet a", "outlet b"]:
                        if return_time < dt.time(hour=9) or return_time > dt.time(hour=18):
                            print("Car not available at that time")
                            return
                        else:
                            return_time_availability = True
                    elif return_outlet in ["outlet c"]:
                        if return_time < dt.time(hour=8) or return_time > dt.time(hour=20):
                            print("Car not available at that time")
                            return
                        else:
                            return_time_availability = True
                    potential_car_list = []
                    for cars in car_list:
                        if category == cars._category and cars._status.lower() != "maintenance":
                            potential_car_list.append(cars)
                    for cars in potential_car_list:
                        pass #check for which outlet it is at currently and if there are any current reservations?    
                            



                            

                    
                        




        elif len(customer_input)> 6:
            print("ERROR: You have entered more inputs then expected")
        else:
            print("ERROR: You have entered fewer inputs than expected")