divisible_by_3_and_5 = 0
divisible_by_3_only = 0
divisible_by_5_only = 0
for i in range(1, 101):
    if ( i % 3 == 0 and i % 5 == 0):
        divisible_by_3_and_5 += 1
        print("FizzBuzz")
        continue
    elif ( i % 3 == 0):
        divisible_by_3_only += 1
        print("Fizz")
        continue
    elif (i % 5 == 0):
        divisible_by_5_only += 1
        print("Buzz")
        continue
    else:
        print(i)

print(f"Number of numbers divisible by 3 and 5: {divisible_by_3_and_5}")
print(f"Number of numbers divisible by 3 only: {divisible_by_3_only}")
print(f"Number of numbers divisible by 5 only: {divisible_by_5_only}")

    