number_1 = input("Enter your first number please: ")
number_2 = input("Enter your second number please: ")
char = input("Enter any of these chars to calculate +,-,*,/: ")
number_1 = int(number_1)
number_2 = int(number_2)



if char== '+':
     result = number_1 + number_2
elif char == '-':
    result = number_1 - number_2
elif char == '*':
    result = number_1 * number_2
elif char == '/':
    result = number_1 / number_2
else:
    print("Input character is not recognized! Try again please.")

print(number_1, char , number_2, "=", result)

