import datetime as dt
import class_functions as cf #own user-defined module


def main():

    #Initial data is loaded through the function below:
    outlet_data, car_data = cf.loadInitialData()
    car_list = [] # to store all the cars that the business owns
    for items in car_data:
        car_list.append(cf.car(items["License Plate Number"],items["Make"],items["Model"],items["Category"],items["Status"],items["Outlet"]))
 
    while True:

        while True:    
            user_choice_1 = input("Please select one of the available options (1, 2, 3, 4 or 5):""\n""1: Add Car""\n""2: Reserve Car""\n""3: Allocate Car""\n""4: Pickup Car""\n""5: Return Car""\n""")
            if user_choice_1 in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, please try again""\n""")

        if user_choice_1 == "1": # Add Car
            cf.car.addCar(car_list)
            print(len(car_list))
            print(car_list)                

        if user_choice_1 == "2": # Reserve Car
            pass

        if user_choice_1 == "3": # Allocate Car
            pass

        if user_choice_1 == "4": # Pickup Car
            pass

        if user_choice_1 == "5": # Return Car
            pass
        
        
        
        while True:
            user_choice_3 = input("Do you want to proceed with another action? Please input Y or N""\n""")
            if user_choice_3 in ["Y", "N"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, please try again""\n""")
                continue
        if user_choice_3 == "Y":
            continue
        elif user_choice_3 == "N":
            break
            

    













if __name__ == "__main__":
    main()