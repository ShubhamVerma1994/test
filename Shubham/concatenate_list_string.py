def concatenate_list_string(list1):
    string = ""
    for i in list1:
        string += str(i)
    return string


print(concatenate_list_string(['my', 'apple', 'orange']))