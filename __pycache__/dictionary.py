# admin = {
#     'first_name': 'Kevin',
#     'last_name': 'Olu',
#     'age': 20,
#     'cily': 'London',
# }
# admin_name = admin['first_name']

# print(admin_name)



# favorite_numbers = {
#     'alice': 3,
#     'nick': 4,
#     'jeff': 8,
# }

# number = favorite_numbers['nick']
# print(f"Nick's favorite number is {number}")




# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
# }

# word = 'string',
# word = 'comment',
# word = 'list',
# word = 'loop',

# for word, sentence in glossary.items():
#     print(f"\n{word} : {glossary[word]}")




# rivers = {
#     'nile': 'egypt',
#     'volga': 'russia',
# }
# for river, country in rivers.items():
#     print(f"The river {river.title()} runs through {country.title()}")

# for river in rivers.keys():
#     print(f"I like {river.title()}")

# for country in rivers.values():
#     print(f"{county.title()}")



# favorite_languages = {
#     'nick': 'css',
#     'john': 'html',
#     'ira': 'js',
#     'tana': 'python',
# }
# names = ['ola', 'ira', 'tana', 'lena']

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favourite language is {language.upper()}'") 

# for name in names:
#     if name in favorite_languages.keys():
#         print(f" {name.title()} thank you")
#     else:
#         print(f"Welcome {name.title()}")



# people =[]

# person_one = {
#     'name': 'Eric',
#     'surname': 'Adam',
#     'age': 33,
# }
# people.append(person_one)

# person_two = {
#     'name': 'Eda',
#     'surname': 'Dan',
#     'age': 22,
# }
# people.append(person_two)

# for person in people:
#     name = person['name']
#     surname = person['surname']
#     age =str(person['age'])

#     print(f" {name.title()} {surname.title()} is {age} years old")








favorite_places = {
    'alina': ['malta', 'paris', 'valencia'],
    'ola': ['spain', 'china'],
    'tanya': ['italy', 'georgia', 'turkey'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes this places:")
    for place in places:
        print(f"{place.title()}.")








  














