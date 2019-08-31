def func_count(list_1):
    d = {}
    for i in list_1:
        keys = d.keys()
        if i in keys:
            d[i]+= 1
        else:
            d[i] = 1
    return d

res = func_count([2, 3, 4, 5, 7, 9,2 , 3, 4, 7])
print(res)
