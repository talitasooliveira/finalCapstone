def calculate_cost(num_guests):
    # Define prices for each item in your menu
    prices = {
        'juice': 2.5,
        'tea': 1.5,
        'coffee': 2.0,
        'milk': 1.0,
        'scones': 3.0,
        'bread': 2.0,
        'biscuits': 1.5,
        'cake': 4.0,
        'jelly': 1.5,
        'butter': 1.0,
        'cheese': 2.5,
        'cupcake': 2.0,
    }

    # Calculate the total cost based on the number of guests
    total_cost = sum(prices[item] for item in prices) * num_guests

    return total_cost

# Input the number of guests
num_guests = int(input("Enter the number of guests: "))

# Calculate and print the total cost
total_cost = calculate_cost(num_guests)
print(f'The total cost for {num_guests} guests is: £{total_cost:.2f}')
