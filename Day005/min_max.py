student_score = [78,65,89,86,55,91,64,89]
max = 0
for i in student_score:
    if max < i:
        max = i

print(f"Maximum value: {max}")