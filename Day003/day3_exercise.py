print("Welcome to treasure Wizard")
print("your mission is to find the treasure")

direction = input("Choose a direction: 'left' (L) or 'right' (R): ").strip().upper()

if direction=="R":
    print("Game over")
else:
    print("Go left and continue")