def fun_histogram(list1):
    for i in list1:
        output = ''
        pug = i
        while (pug > 0):
            output += "@"
            pug = pug - 1
        print(output)


fun_histogram([2, 3, 4, 8])
