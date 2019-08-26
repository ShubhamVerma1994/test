def fibonacci_series(num):
    a = 0
    b = 2
    if num < 0:
        print("Invalid Input")
    elif num == 0:
        print(a)
    elif num == 1:
        print(b)
    else:
        for i in range(2,num):
            c = a+b
            print(c)
            a = b
            b = c

fibonacci_series(9)

