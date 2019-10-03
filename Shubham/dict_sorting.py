import operator
d =  {1: 2, 9:6, 4: 5, 3: 98, 2: 3}
print("Given dictionary: ", d)
sorted_d = dict(sorted(d.items(), key = operator.itemgetter(0)))
print("Increasing order: ", sorted_d)
sorted_d = dict(sorted(d.items(), key = operator.itemgetter(0), reverse = True))
print("Decreasing order: ", sorted_d)
