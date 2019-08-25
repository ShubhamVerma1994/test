str_1 = str(input("Enter a string = "))
dict_str = {}
for i in str_1:
    keys = dict_str.keys()
    if i in keys:
        dict_str[i] += 1
    else:
        dict_str[i] = 1
print(dict_str)
