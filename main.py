import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
new_list = []
new_list1 = []

pattern = r"(\+7|8)(\s?\(?)(\d{3})(\)?\s?|\-?)(\d{3})\-?(\d{2})\-?(\d{2})(\s?)\(?(\w*\.?)\s*(\d*)\)?"
sub_pattern = r"+7(\3)\5-\6-\7\8\9\10"
for el in contacts_list:
    text = ','.join(el)
    res = re.sub(pattern, sub_pattern, text)
    res = res.split(',')
    new_list.append(res)

pattern1 = r"^(\w+)\s?\,?(\w+)\s?\,?(\w*)\W+"
sub_pattern1 = r"\1,\2,\3,"
for i in new_list:
    text1 = ','.join(i)
    res2 = re.sub(pattern1, sub_pattern1, text1)
    res2 = res2.split(',')
    new_list1.append(res2)


my_dict = {}
for element in new_list1:
    new_set = (element[0], element[1])
    if new_set in my_dict:
        inf = element[2:]
        for info in inf:
            if info in my_dict[new_set]:
                pass
            else:
                if len(info) > 30:
                    if my_dict[new_set][2] == '':
                        my_dict[new_set][2] = info
                    else:
                        my_dict[new_set].insert(2, info)
                else:
                    if my_dict[new_set][-1] == '':
                        my_dict[new_set][-1] = info
                    else:
                        my_dict[new_set].append(info)

    else:
        my_dict[new_set] = element[2:]

my_list2 = []
for element in my_dict:
    dop_list = []
    dop_list.extend(element)
    dop_list.extend(my_dict[element])
    my_list2.append(dop_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(my_list2)