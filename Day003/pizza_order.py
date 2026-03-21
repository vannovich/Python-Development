size = input("Enter desired pizza size (Small (S), Medium (M), Large (M)): ").strip().upper()
add_pepperoni = input("Extra peperoni? ('Y' or 'N'): ").strip().upper()
extra_cheese = input("Extra chease? ('Y' or 'N'): ").strip().upper()

total_price = 0

# Price calculation
# Price based on size
if size=='S':
    total_price += 15
elif size == 'M':
    total_price += 20
elif size == 'L':
    total_price +=25

# peroni Logic
if size == 'S' and add_pepperoni == 'Y':
    total_price += 2
elif (size == 'M' or size=='L') and add_pepperoni == 'Y':
    total_price += 3
    
# Extra cheese
if extra_cheese == 'Y':
    total_price += 1
    
print()
print(f"Your final bill is ${total_price}")