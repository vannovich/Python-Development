import os

print("Welcome to the silent bitter")
print()

bidders = {}

def enter_bitter():
    name = input("Enter your name: ").strip()
    bid = float(input("Enter bit amount: $").strip())
    bidders[name] = bid
    os.system('cls' if os.name == 'nt' else 'clear')
    

def print_winner():
    os.system('cls' if os.name == 'nt' else 'clear')
    max_bit = 0
    winner = ''
    for key,value in bidders.items():
        if max_bit < value:
            max_bit = value
            winner = key
            print(f"{max_bit}")
    print(f"Winning bid is {winner}, with a bid of ${max_bit}")

enter_bitter()
while True:
    menu = input("Are there Any other bidders?: 'Yes' or 'No'").capitalize()
    if menu == 'Yes':
        enter_bitter()
    elif menu == 'No':
        print("Bid is over")
        print()
        break
    
print_winner()
        
    