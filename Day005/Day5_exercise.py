import random

print(f"Password Generator".upper())

# Letters (lowercase + uppercase)
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Symbols (common special characters)
symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}','|',
    ';',':',"'",'"',',','.','<','>','/','?','\\'
]

# info gathering
password_size = int(input("Enter Desired password size: ").strip())
num_of_nums = int(input("How many numbers would you like to be present in the password: "))
num_of_chars = int(input("How many speccial characters would you like to be present: "))

num_of_letters = password_size - num_of_chars - num_of_chars

# Randomization
random_password = ""
for i in range(num_of_nums):
    random_password += random.choice(numbers)

for i in range(num_of_chars):
    random_password += random.choice(symbols)
for i in range(num_of_letters):
    random_password += random.choice(letters)
    
temp_pass = random.sample(random_password, len(random_password))
new_password = ''
for i in temp_pass:
    new_password += i

print()
print("Password: ",new_password)
