def true_and_love_test(name):
    countLove = 0
    countTrue = 0
    for i in name.lower():
        if i in 'love':
            countLove+=1
        if i in 'true':
            countTrue+=1
    count = f"{countTrue}{countLove}"
    return int(count)
            
        

print("Welcome to the Love Calculator!")
name1 = input("What is your name?: ")
name2 = input("What is their name: ")

full_name = name1 + name2

if true_and_love_test(full_name)< 10 or true_and_love_test(full_name) > 90:
    print(f"Your score is {true_and_love_test(full_name)}, you go together like coke and mentos")
elif true_and_love_test(full_name) >= 40 and true_and_love_test(full_name) <= 50:
    print(f"Your score is {true_and_love_test(full_name)}, you are alright together") 
else:
    print(f"Your score is {true_and_love_test(full_name)}")

