from random import choice

random_list = ['1','3','5','7','a','s','d', 'n', 'm']

winning_list = []
print(f"Any ticket matching these four numbers or letters wins a prize!")
while len(winning_list) < 4:
    choosen_item = choice(random_list)
    # Only add the pulled item to the winning list if it hasn't
    #   already been pulled.
    if choosen_item not in winning_list:
        print(f"{choosen_item}")
        winning_list.append(choosen_item)
