#The if statement in Python is used for conditional execution of code blocks based on whether a specified condition evaluates to True or False.
#An if statement evaluates a condition is true, the code block within the if statement is executed. If the condition is false, the code block is skipped.
temperature = 15
if temperature > 20:
    print('Its warm outside!')
else:
    print('Its cold outside!')

score = 75
if score >= 90:
    Grade ='A'
elif score >= 80:
    Grade ='B'
elif score >= 70:
    Grade ='C'
elif score >= 60:
    Grade ='D'
else:
    Grade ='F'

print(f'Your grade is: {Grade}')

# write a program that checks if a number is positive, negative, or zero
number = int("10:")
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is zero.")
else:
    print(f"{number} is negative.")

