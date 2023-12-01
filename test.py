from collections import defaultdict
import re

key = "key1"

my_dict1 = defaultdict(list)
my_dict1[key].append("00:11")
my_dict1[key].append("12:52")

list1 = []

history_file = "history.csv"

for value in (my_dict1[key]):
    list1.append(value)
with open(history_file, "w", encoding="utf-8") as file:
    e = True
    for i in range(len(list1)):
        lines = re.sub(r"[\([{})\]]", "", list1[i])
        while e == True:
            file.write(key + ",")
            e = False
        print(lines)
        file.write(lines + ",")
print(list1)