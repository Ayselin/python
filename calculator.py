while True:
    number_1 = input("Enter your first number please > ")
    number_2 = input("Enter your second number please > ")
    char = input("Enter any of these chars to calculate +,-,*,/  \nEnter 'quit' to stop calculating. > ")
    
    number_1 = int(number_1)
    number_2 = int(number_2)

    
    if char == '+':
        result = number_1 + number_2
    elif char == '-':
        result = number_1 - number_2
    elif char == '*':
        result = number_1 * number_2
    elif char == '/':
        if number_2 == 0:
            print("You can not devide a number by 0")
        else:
            result = number_1 / number_2
    else:
        break

    print(number_1, char , number_2, "=", result)

