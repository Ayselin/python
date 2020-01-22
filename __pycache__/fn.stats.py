import math

user_list = input("Enter in numbers separated by a space: ")
split_variable = user_list.split()

list_numbers = []
for numbstring in split_variable:
    integer = int(numbstring)
    list_numbers.append(integer)

n = len(list_numbers)

print("Your list of numbers is: "  ,list_numbers)
mmm = input("Would you like the find the mean, median, or mode? ")


def mean(list_numbers):
    return sum(list_numbers)/n
    
# re = mean(list_numbers)
# print(re)


def median(list_numbers):
    x = sorted(list_numbers)
    y = len(x)
    if y % 2 == 0:
        r = math.floor(y / 2)
        w = math.ceil( y / 2)
        s = (r+w) / 2
        return s
    else:
        z = math.floor(y / 2)
        return  x[z]
   
# er = median(list_numbers)
# print(er)


def mode(list_numbers):
    d = {}
    for key in list_numbers:
        if key in d:
            d[key] += 1
        else: 
            d[key] = 1
    greatest_value =  0 
    greatest_key = None
    for key in d:
        if d[key] > greatest_value:
            greatest_key = key
            greatest_value = d[key]
            return greatest_key

# fuu = mode(list_numbers)
# print(fuu)
if mmm == 'mean':
     print(mean(list_numbers))
elif mmm == 'median':
    print(median(list_numbers))
elif mmm == 'mode':
    print(mode(list_numbers))
                                                        

