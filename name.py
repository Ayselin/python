def word_count(string):
  new_list = string.split()
  unique = set(new_list)
  my_dict={}

for unique in new_list:
    my_dict[unique]=new_list.count(unique)
        return my_dict


print(word_count("hello olla hello Hi hi yes Yes no no"))