"""
Course: ISM 2411
Lab: Week 10
Student Name: Joshua Eisenberg

Reflection Questions:
1. The most surprising thing about Python lists is how flexible and dynamic they are compared to static data storage. Coming in, 
I expected lists to have fixed sizes, but built-in methods like .append() and zero-indexed slicing make it remarkably easy to 
manipulate, reorder, and access elements on the fly.

2. When tracking daily sales transactions and operating expenses for my small business, logging and categorizing every record 
manually in Excel was tedious and time-consuming. Using Python lists to store sales and expense figures allows me to calculate 
total revenue, net profit, and high-value transactions automatically with short loops, saving significant time and reducing 
formula errors.
"""

print("---Exercise 1: Build the list---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: Index practice---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

print("---Exercise 3: Slicing practice---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("---Exercise 4: Modifying the list---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
inventory.sort()
print(inventory)

print("---Exercise 5: tuple comparison---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TuypeError caught:", error)
    print("Tuples protect coordinates: a location should never be by accident")

print(coords)

print("---Exercise 6: Average list of sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = (len(sales))
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


print("---Exercise 7: Accumulator pattern---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounts:", discount)

print("---Exercise 8: Filter abover a threshold---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print()
