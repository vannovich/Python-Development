import random # imports
print(f"Welcom to the Rock, Paper, Scissors game".upper())

# Variables
choice = ["Rock","Paper","Scissors"]
user_choice = int(input("Make a choice: 1 for Rock, 2 for Paper, 3 for Scissors: ").strip())

final_user_choice = choice[user_choice - 1]

computer_choice = random.choice(choice)

# Win / Loose conditions
if final_user_choice == choice[0] and computer_choice == choice[2]:
    print(f"You Picked : {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print("User Win🥳🥳🥳")
elif final_user_choice == choice[2] and computer_choice == choice[0]:
    print(f"You Picked: {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print("You Lose 😭😭😭")
elif final_user_choice == choice[2] and computer_choice == choice[1]:
    print(f"You Picked: {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print("User Win🥳🥳🥳")
elif final_user_choice == choice[1] and computer_choice == choice[2]:
    print(f"You Picked: {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print("You Lose 😭😭😭")
elif final_user_choice == choice[0] and computer_choice == choice[1]:
    print(f"You Picked: {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print("User Win🥳🥳🥳")
elif final_user_choice == choice[1] and computer_choice == choice[0]:
    print(f"You Picked: {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print("You Lose 😭😭😭")
else:
    print()
    print(f"You Picked: {final_user_choice}")
    print(f"Computer Picked: {computer_choice}")
    print()
    print(f"Draw 🙌🙌. Try again")

    


