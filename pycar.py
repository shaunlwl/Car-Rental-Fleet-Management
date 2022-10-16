import datetime as dt
import class_functions as cf #own user-defined module


def main():

    #Initial data is loaded through the function below:
    outlet_data, car_data = cf.loadInitialData()
    car_list = [] # to store all the cars that the business owns
    reservations_list = []
    allocation_dict = {}
    reservation_number = 1
    for items in car_data:
        car_list.append(cf.car(items["License Plate Number"],items["Make"],items["Model"],items["Category"],items["Status"],items["Outlet"]))
 
    while True:

        while True:    
            user_choice_1 = input("Please select one of the available options (1, 2, 3, 4 or 5):""\n""1: Add Car""\n""2: Reserve Car""\n""3: Allocate Car""\n""4: Pickup Car""\n""5: Return Car""\n""")
            if user_choice_1 in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, Please try again""\n""")

        if user_choice_1 == "1": # Add Car
            cf.car.addCar(car_list)
            

        if user_choice_1 == "2": # Reserve Car
            reserved_car, rental_days, pickup_date, return_date, pickup_outlet, return_outlet, pickup_time, return_time = cf.car.reserveCarCheck(car_list, reservations_list)
            if isinstance(reserved_car, cf.car):
                if rental_days % 1 == 0:
                    rental_days_rounded = rental_days
                else: 
                    rental_days_rounded = round(rental_days + 1)
                if reserved_car.getCategory().lower() == "suv":
                    total_rent = rental_days_rounded * 150
                elif reserved_car.getCategory().lower() == "sedan":
                    total_rent = rental_days_rounded * 100
                else:
                    total_rent = rental_days_rounded * 200
            
            
                print(f"Car available, Rental fee:${total_rent}")
                while True:
                    user_confirmation = input("Do you want to confirm reservation? Yes/No""\n""")
                    if user_confirmation in ["Yes", "No"]:
                        break
                    else:
                        print("ERROR: You have entered an invalid options, Please try again""\n""")
                if user_confirmation == "Yes":
                    reservations_list.append({"Reservation Number": "#"+ str(reservation_number),"License Plate": reserved_car.getLicensePlateNo(), "Pickup Date": pickup_date, "Return Date": return_date,"Pickup Outlet": pickup_outlet ,"Return Outlet": return_outlet, "Pickup Time": pickup_time, "Return Time": return_time })
                    reservation_number += 1
                    print("Reservation Successful:""\n""")
                    print("Reservation Number: " + reservations_list[-1]["Reservation Number"] + "\n","Pickup Outlet: " + reservations_list[-1]["Pickup Outlet"].upper() +"\n","Pickup Date: "+ str(reservations_list[-1]["Pickup Date"]) + "\n", "Pickup Time: " + str(reservations_list[-1]["Pickup Time"]) + "\n", sep="" )
                if user_confirmation == "No":
                    print("Reservation not confirmed""\n""")

        
        
        if user_choice_1 == "3": # Allocate Car
            
            try:
                reservation_date = dt.datetime.strptime(input("Please input reservation date in this format: dd/mm/yy""\n"""), '%d/%m/%y').date()
            except ValueError:
                print("ERROR: You have entered an invalid date format, Please ensure it is entered as dd/mm/yy""\n""")
            else:
                if len(reservations_list) == 0:
                    print("No allocation is required""\n""")
                else:
                    for reservations in reservations_list:
                        if reservations["Pickup Date"] == reservation_date:
                            for car in car_list:
                                if car.getLicensePlateNo().lower() == reservations["License Plate"].lower():
                                    if car.getStatus().lower() == "pickup":
                                        car.setStatus("Pickup and Allocated") 
                                    else:
                                        car.setStatus("Allocated") 
                            if reservation_date not in allocation_dict.keys():
                                allocation_dict[reservation_date] = [[reservations["Reservation Number"],reservations["Pickup Outlet"].upper(), reservations["License Plate"]]]
                            else:
                                allocation_dict[reservation_date].append([reservations["Reservation Number"],reservations["Pickup Outlet"].upper(), reservations["License Plate"]])  
                    
                    if reservation_date in allocation_dict.keys():                      
                        print("Allocated cars for " + str(reservation_date) + ":" +"\n")
                        for items in allocation_dict[reservation_date]:
                            print(items)
                    else:
                        print("No allocation is required")

        
        
        if user_choice_1 == "4": # Pickup Car
            reservation_number_input = input("Please input reservation number""\n""")
            reservation_number_valid = False
            for reservations in reservations_list:
                if reservations["Reservation Number"] == reservation_number_input:
                    reserved_car_plate_no = reservations["License Plate"].lower()
                    reservation_number_valid = True
                    break
            if reservation_number_valid == True:
                for car in car_list:
                    if car.getLicensePlateNo().lower() == reserved_car_plate_no:
                        if car.getStatus().lower() == "allocated":
                            print(reserved_car_plate_no.upper())
                            car.setStatus("Pickup")
                        else:
                            print("ERROR: Car has not been allocated")
            else:
                print("Error, Reservation number does not exist")

            
        

        
        
        if user_choice_1 == "5": # Return Car
            reservation_number_input = input("Please input reservation number""\n""")
            reservation_number_valid = False
            for reservations in reservations_list:
                if reservations["Reservation Number"] == reservation_number_input:
                    reserved_car_plate_no = reservations["License Plate"].lower()
                    reservation_number_valid = True
                    break
            if reservation_number_valid == True:
                for car in car_list:
                    if car.getLicensePlateNo().lower() == reserved_car_plate_no:
                        if car.getStatus().lower() == "allocated" or car.getStatus().lower() == "pickup":
                            print(reserved_car_plate_no.upper())
                            car.setStatus("Available")
                        else:
                            print("ERROR: Car has not been set to Allocated or Pickup")
            else:
                print("Error, Reservation number does not exist")
        



        
        while True:
            user_choice_3 = input("Do you want to proceed with another action? Please input Yes or No""\n""")
            if user_choice_3 in ["Yes", "No"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, please try again""\n""")
                continue
        if user_choice_3 == "Yes":
            continue
        elif user_choice_3 == "No":
            break
            


if __name__ == "__main__":
    main()