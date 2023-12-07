# import re
# from collections import defaultdict

# list1 = []
# my_dict1 = defaultdict(list)

# key = "key1"
# value1 = "00:11"
# value2 = "12:52"

# print(value1)
# print(type(value1))
# print(my_dict1)
# my_dict1[key].append(value1)
# print(my_dict1[key])


# #my_dict1[key].append(value2)
# history_file = "history.csv"

# for value in (my_dict1[key]):
#     list1.append(value)
#     print(type(value))
# with open(history_file, "w", encoding="utf-8") as file:
#     e = True
#     for i in range(len(list1)):
#         lines = re.sub(r"[\([{})\]]", "", list1[i])
#         while e == True:
#             file.write(key + ",")
#             e = False
#         print(lines)
#         file.write(lines + ",")
# print(list1)

# from itertools import chain

# dictionary1 = {'a': 1, 'b': 2, 'c': 3}
# dictionary2 = {'c': 4, 'd': 5, 'e': 6}

# # Key you want to check
# key_to_check = 'c'

# # Iterate over the dictionaries and check if the key exists
# for dictionary, keys in zip([dictionary1, dictionary2], ['e', 'f']):
#     if key_to_check in dictionary:
#         print(f'The key "{key_to_check}" exists in {keys}.')
#         break
# else:
#     print(f'The key "{key_to_check}" does not exist in either dictionary.')


# from itertools import chain

# dictionary1 = {'a': 1, 'b': 2, 'c': 3}
# dictionary2 = {'c': 4, 'd': 5, 'e': 6}
# key1 = "a"

# # Combine the dictionaries
# combined_dicts = chain([dictionary1], [dictionary2])

# # Iterate over the keys in the combined dictionaries
# for key_to_check in set(chain(dictionary1.keys(), dictionary2.keys())):
#     if key_to_check in dictionary1:
#         print(f'The key "{key_to_check}" exists in {dictionary1}.')
#         # Do your thing here
#     else:
#         print(f'The key "{key_to_check}" exists in {dictionary2}.')
# print(dictionary1[key1])


time1_list = [1, 2, 3]
time2_list = ['a', 'b', 'c']

for time1, time2 in zip(time1_list, time2_list):
    print(time1, time2)
