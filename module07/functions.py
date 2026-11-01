"""
1. The first bug I spotted was that my loop went past the end of the list. AI helped me figure out what the error message meant and how to fix it. 
This helped me understand how to use error messages to find problems in my code.

2. apply_discount(price, tier) takes a price and a discount tier, calculates the discount, and returns the new price. A colleague could use it without 
reading the code if the function name and inputs were clear.

3. I would add a comment saying that I used AI to help explain errors and understand the code. Using AI helped me understand what went wrong instead 
of just fixing the code without knowing why."""

# Exercise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax:  ${calculate_tax(150, 0.05):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.

""" I asked AI what the error message meant, and the description allowed me to quickly realize that line "while i <= len(sales):" was wrong. 
Instead of <, it was <=, and my codetried to access an integer that was not really there. It was a very simple fix."""

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)