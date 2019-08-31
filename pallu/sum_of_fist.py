def sum_first_digit(list_1):
    total = 0
    for i in list_1:
        total += int(str(i)[0])
    print (total)

sum_first_digit([23, 64, 55, 764, 987, 1])