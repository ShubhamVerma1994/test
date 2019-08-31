def sum_last_digit(list_1):
    total = 0
    for i in list_1:
        total += (i%10)
    print(total)

sum_last_digit([23, 435, 987, 6239, 5555, 934])