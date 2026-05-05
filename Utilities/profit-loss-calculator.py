# Program to calculate profit or loss by a merchant

# Input cost price, expenditure, and selling price
cost_price = float(input("Enter the cost price of the item: "))
transportation_cost = float(input("Enter the total transportation cost: "))
rent = float(input("Enter the total rent: "))
rent_days = int(input("Enter the number of days the rent is for: "))
other_expenditures = float(input("Enter other total expenditures: "))
number_of_items = int(input("Enter the number of items: "))
selling_price = float(input("Enter the selling price of the item: "))

# Calculate per-item cost for transportation and other expenditures
per_item_transportation_cost = transportation_cost / number_of_items
per_item_other_expenditures = other_expenditures / number_of_items

# Calculate total cost per item
total_cost_per_item = cost_price + per_item_transportation_cost + per_item_other_expenditures

# Add rent cost per item based on the number of days
rent_per_day = rent / rent_days
total_cost_per_item += rent_per_day / number_of_items

# Calculate profit or loss
if selling_price > total_cost_per_item:
    profit = selling_price - total_cost_per_item
    print(f"The merchant made a profit of {profit:.2f} per item")
elif total_cost_per_item > selling_price:
    loss = total_cost_per_item - selling_price
    print(f"The merchant incurred a loss of {loss:.2f} per item")
else:
    print("There is no profit or loss per item.")
