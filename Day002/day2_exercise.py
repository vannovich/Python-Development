print("Welcom to the tip calculator")

total_bill = float(input("What was the total bill: $"))
number_of_people = int(input("How amny people to split the bill: "))
tip_percentage = float(input("What percentage tip woul you like to give? 10, 12 or 15: "))

percentage_increased = total_bill * (tip_percentage/100)
new_bill = percentage_increased + total_bill

bill_per_person = new_bill / number_of_people

print(f"Each person should pay: ${round(bill_per_person, 2)}")