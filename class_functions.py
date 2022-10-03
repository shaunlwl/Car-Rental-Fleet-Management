
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

    
    def addCar(self, license_plate_no, make, model, category, status, outlet):
        pass