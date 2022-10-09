import datetime as dt
from multiprocessing.sharedctypes import Value
import class_functions as cf #own user-defined module


def main():

    #Initial data is loaded through the function below:
    outlet_data, car_data = cf.loadInitialData()
    car_list = [] # to store all the cars that the business owns
    reservations_list = {}
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
            reserved_car, rental_days, pickup_date, return_date, pickup_outlet, return_outlet = cf.car.reserveCarCheck(car_list)
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
                    list_of_dates = []
                    pickup_date_loop = pickup_date
                    
                    while pickup_date_loop <= return_date:
                        list_of_dates.append(pickup_date_loop)
                        pickup_date_loop = pickup_date_loop + dt.timedelta(days=1)
                    reserved_car.setReservedDates(list_of_dates)
                    if pickup_date in reservations_list.keys():
                        reservations_list[pickup_date].append({"Reservation no" : "#" + str(reservation_number), "Pickup Location":pickup_outlet, "License Plate": reserved_car.getLicensePlateNo(), "Source Outlet": reserved_car.getOutlet()})
                        reservation_number += 1
                    else:
                        reservations_list[pickup_date] = [{"Reservation no" : "#" + str(reservation_number), "Pickup Location":pickup_outlet, "License Plate": reserved_car.getLicensePlateNo(), "Source Outlet": reserved_car.getOutlet()}]
                        reservation_number += 1
                    print(reservations_list)
                if user_confirmation == "No":
                    print("Reservation not confirmed")

        if user_choice_1 == "3": # Allocate Car
            try:
                reservation_date = dt.datetime.strptime(input("Please input reservation date in this format: dd/mm/yy""\n"""), '%d/%m/%y').date()
            except ValueError:
                print("ERROR: You have entered an invalid date/time format, Please ensure it is entered as dd/mm/yy""\n""")
            else:
                print(reservation_date)


        if user_choice_1 == "4": # Pickup Car
            reservation_number = input("Please input reservation number""\n""")


        if user_choice_1 == "5": # Return Car
            reservation_number = input("Please input reservation number""\n""")
        
        
        
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