# def distance(strand_a, strand_b):
#     a = int(strand_a)
#     b = int(strand_b)

#     result = 0
#     if len(a) == len(b):
#         for i in a:
#             if b[i] != a[i]:
#                 result += 1
#         return result
#     else:
#         raise ValueError('Length is different')
# print(distance("asvfbf","sdcsdd"))




def is_isogram(string):
    string = string.lower()
    string = ''.join(string.split('-'))
    string = ''.join(string.split())
    # Compare number of total letters with number of unique letters
    return string == set(string)


print(is_isogram("a"))


