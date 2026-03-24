# Dynamic calculator App
import os
print("Calculator App")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def operation(symbol,num1,num2):
    if symbol == '+':
        return addition(num1, num2)
    elif symbol == '-':
        return subtraction(num1, num2)
    elif symbol == '*':
        return multiply(num1, num2)
    elif symbol == '/':
        if (num2 == 0):
            print("Division by zero error")
        return division(num1, num2)
    else:
        print("Please Enter value Between 1-4")

while True:
    num1 = float(input("Enter first number: ").strip())
    num2 = float(input("Enter second number: ").strip())
    operator = input("Enter operator: ")
    results = operation(operator, num1,num2)
    print()
    print(f"Result: {results}")
    
    while True:
        continue_with_results = input(f"Continue with {results} as first value? 'yes' or 'no': ").strip().lower()
        if continue_with_results == 'no':
            print(f"Final answer: {results}")
            break
        elif continue_with_results == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            num2 = float(input("Enter second value: ").strip())
            operator = input("Enter operator: ")
            results = operation(operator, results, num2)
        
    another_operation = input("Another operation? 'yes' or 'no' ").strip().lower()
    if another_operation == 'no':
        break
    elif another_operation == 'yes':
        continue

os.system('cls' if os.name == 'nt' else 'clear')
print("Thank you for using our calculator App See you soon 😁")
    
    