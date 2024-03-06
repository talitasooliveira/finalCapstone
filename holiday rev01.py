# Task 14 - Program to calculate a travel 

print("This program will help you to know the costs of your travel!")

## Plane Cost ##

def plane_cost(city):
    
    """
    This is a function to define the cost of the plane after the user insert a city.
    The user needs to choose between three cities (Paris, Rome, Lisbon) to travel with different costs.
    """
    
# If the city choosed is Paris, the price defined is £180.
    if city == "PARIS":
        plane_cost=180
        return plane_cost
   
# If the city choosed is Rome, the price defined is £240.
    elif city == "ROME":
        plane_cost=240
        return plane_cost
   
# If the city choosed is Lisbon, the price defined is £310.
    elif city == "LISBON":
        plane_cost=310
        return plane_cost
 
# If the user don't input a valid option, the program will ask again.
    else:
        print("There are only the three options above, try again.")
        return 0

while True:
    c_flight=input("Please, choose the city will be flying to - between 3 cities: Paris, Rome or Lisbon: ") 
    city_flight=c_flight.upper()

# The cost plane is defined using the function above (plane_cost) with user's input.
    plane_cost_final = plane_cost(city_flight)
    if plane_cost_final>0:
        break


## Hotel Cost ##

def get_valid_input():
    
    """
    This is a function using to guarantee that the user will insert a valid number (integer).
    """

    while True:
        try:
            user_input = int(input("Please, enter the number of nights they will be staying at a hotel: "))
            if user_input <0:
                raise ValueError("Number of nights should be a positive integer.")
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

# This is a variable used below with a valid user's input.
num_nights = get_valid_input()

def hotel_cost(num_nights):

    """
    This is a function to define the cost of the hotel after the user insert a number of nights.
    The price per night was a average between the good hotels at cities (Paris, Rome, Lisbon).
    """

# It was defined that £120 is the price per night
    y = 120 * num_nights  
    return y


## Rental Car Cost ##

def get_valid_input():

    """
    This is a function using to guarantee that the user will insert a valid number (integer).
    """

    while True:
        try:
            user_input = int(input("Please, enter the number of days for which they will be hiring a car: "))
            if user_input <0:
                raise ValueError("Number of days should be a positive integer.")
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

rental_days = get_valid_input ()

# It was defined that £24 is the daily car rental
def car_rental(rental_days):

    """
    This is a function to define the cost of the rental car after the user insert a number of days.
    The price per day was a average between the good car rentals at cities (Paris, Rome, Lisbon).
    """

    y = 24 * rental_days 
    return y


## Total Cost ##

def holiday_cost (x, y, z):
    
    """
    This is a function to define the cost total based on the user's inputs.
    """    
    holiday_cost = x + y + z
    return holiday_cost

holiday_total_cost = holiday_cost(plane_cost_final, hotel_cost(num_nights), car_rental(rental_days))

# This print shows to the user the total cost and separate costs: plane cost, hotel cost and car rental cost.
print(f"The total cost of your travel is: £{holiday_total_cost}" + "\n" + "Of wich: " + "\n" + f"Plane cost: £{plane_cost_final}" +"\n" + f"Hotel cost: £{hotel_cost(num_nights)}" + "\n" + f"Car rental: £{car_rental(rental_days)}")
