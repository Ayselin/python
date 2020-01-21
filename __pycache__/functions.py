# def display_message():
#     print("I am learning python")
# display_message() 


# def favorite_book(title):
#     print(f"{title} is my favorite book")
# favorite_book("Alice in Wonderland")


# def make_shirt(size='large', text = 'Hi'):
#     print(f"The size of the shirt is {size} and it says {text}")
# make_shirt(size = 'big', text = 'Cool')
# make_shirt()
# make_shirt('small', 'Bye')



# def describe_city(name = 'Baku', country = 'Azerbaijan'):
#     print(f"{name} is in {country}")
# describe_city()
# describe_city(name = 'London', country = 'England')



# def make_album(name, title, number=None):
#     music_album = {
#         'name': name.title(),
#         'title': title.title(),
#     }
#     if number:
#         music_album['number'] = number
#     return music_album

# musician = make_album('alex', 'freedom'),
# musician = make_album('nick', 'hard rock', number=6)
# print(musician)

# new_name = "\nPlease enter an artist: "
# new_title = "\nPlease enter the title: "
# print("enter 'q' to finish")


# while True:
#     # new_name = print("\nPlease add new artist: ")
#     name = input(new_name)
#     if name == 'q':
#         break
    
#     # new_title = print("\nPlease add the title: ")
#     title = input(new_title)
#     if title == 'q':
#         break

#     album = make_album(name, title)
#     print(album)





# def show_messages(messages):
#     for message in messages:
#         print(f"first {message}")



# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop()
#         sent_messages.append(current_message)
#         print(f"second {current_message}")
        

# messages = ['hello', 'hi', 'how are you', 'welcome']
# show_messages(messages)


# sent_messages = []
# send_messages(messages[:], sent_messages)

# print(messages)
# print(sent_messages)







def sandwiches(*items):
    sandwich_items = items[0]

    for item in items[1:]:
        sandwich_items = sandwich_items + ', ' +item
    print(f"Your sandwich has: {sandwich_items} on it")

sandwiches('cheese', 'ham', 'chicken')



def build_profile(first, last, gender, **my_info):
    print(f"My info starts as ", my_info)
    my_info['first_name'] = first
    my_info['last_name'] = last
    my_info['gender'] = gender
    print(f"My info finishes as ", my_info)
    return my_info


my_profile = build_profile('Aysel', 'Rzayeva', 'female', type = 'cool girl', location = 'London')

print(my_profile)






