def calculator(number_1, number_2, char):
    if char == '+':
        result = number_1 + number_2
    elif char == '-':
        result = number_1 + number_2
    elif char == '*':
        result = number_1 + number_2
    elif char == '/':
        if number_2 == 0:
            # print("You can not devide a number by 0")
            return None
        else:
            result = number_1 / number_2
    return result
        # else:
        #     break
###### main loop
while True:
    number_1 = input("Enter your first number please > ")
    number_2 = input("Enter your second number please > ")
    char = input("Enter any of these chars to calculate +,-,*,/  \nEnter 'quit' to stop calculating. > ")
    number_1 = int(number_1)
    number_2 = int(number_2)

    if number_2 == 0 and char == '/':
        print("you can't divide by zero")
    else:
        res = calculator(number_1, number_2, char)
        print(res)















