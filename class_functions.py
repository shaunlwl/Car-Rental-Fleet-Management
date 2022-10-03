
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