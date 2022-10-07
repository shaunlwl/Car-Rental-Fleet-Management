import datetime as dt
import class_functions as cf #own user-defined module


def main():

    #Initial data is loaded through the function below:
    outlet_data, car_data = cf.loadInitialData()
    car_list = []
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
            while True:
                new_car_input = input("Please input car details in the following format: License Plate No., Make, Model, Category, Status, Outlet""\n""Pls use commas to separate your inputs.""\n""").strip().split(",")
                new_car = []
                if len(new_car_input) == 6:
                    for details in new_car_input:
                        new_car.append(details.strip().lower())
                    if new_car[5] in ["outlet a", "outlet b", "outlet c"] and new_car[4] in ["available", "allocated", "pickup", "maintenance"] and new_car[3] in ["sedan", "suv", "mpv"]:
                        car_list.append(cf.car(new_car[0],new_car[1],new_car[2],new_car[3],new_car[4],new_car[5]))
                        print(car_list[9]._license_plate_no)
                        break
                    else:
                        print("ERROR: You have entered an invalid input for either Category, Status or Outlet, Please try again""\n""")
                        continue
                elif len(new_car_input) < 6:
                    print("ERROR: You have entered fewer car details than expected, Please try again""\n""")
                    continue
                else:
                    print("ERROR: You have entered more car details than expected, Please try again""\n""")
                    continue
                

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