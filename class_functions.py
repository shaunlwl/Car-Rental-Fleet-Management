
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

    
    def addCar(self, car_list):
        while True:
            new_car_input = input("Please input car details in the following format: License Plate No., Make, Model, Category, Status, Outlet""\n""Pls use commas to separate your inputs.""\n""").strip().split(",")
            new_car = []
            license_plate_match = False
            if len(new_car_input) == 6:
                for details in new_car_input:
                    new_car.append(details.strip().lower())
                for cars in car_list:
                    if new_car[0] == cars._license_plate_no:
                        print("ERROR: License Plate number already exists, Please try again")
                        license_plate_match = True
                        break
                if license_plate_match == True:
                    continue
                else:    
                    if new_car[5] in ["outlet a", "outlet b", "outlet c"] and new_car[4] in ["available", "allocated", "pickup", "maintenance"] and new_car[3] in ["sedan", "suv", "mpv"]:
                        car_list.append(car(new_car[0],new_car[1],new_car[2],new_car[3],new_car[4],new_car[5]))
                        print(car_list[9]._license_plate_no)
                        break
                    elif new_car[5] not in ["outlet a", "outlet b", "outlet c"]:
                        print("ERROR: You have entered an invalid input for Outlet, Please try again""\n""")
                        continue
                    elif new_car[4] not in ["available", "allocated", "pickup", "maintenance"]:
                        print("ERROR: You have entered an invalid input for Status, Please try again""\n""")
                        continue
                    elif new_car[3] not in ["sedan", "suv", "mpv"]:
                        print("ERROR: You have entered an invalid input for Category, Please try again""\n""")
                        continue
            elif len(new_car_input) < 6:
                print("ERROR: You have entered fewer car details than expected, Please try again""\n""")
                continue
            else:
                print("ERROR: You have entered more car details than expected, Please try again""\n""")
                continue