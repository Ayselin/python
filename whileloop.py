# prompt = "\n What topping would you like?"
# prompt += "\n Enter 'quit' when you finished: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"{topping} were added to your pizza")
#     else: 
#         break
    





# promt = "How old are you? "
# promt += "Enter 'quit when you finish: "


# while True:
#     age = input(promt)
#     if age == 'quit':
#         break
#     age = int(age)
     
#     if age < 3:
#         print(f"The ticket is free")
#     elif age < 13:
#         print("The ticket is $10")
#     else:
#         print("Ticket os $15")






sandwich_orders = ['cheese', 'chicken', 'beef', 'turkey']

finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I made your {sandwiches} sandwich.")
    finished_sandwiches.append(sandwiches)

for sandwich in finished_sandwiches:
    print("Your sandwich is ready")
    




