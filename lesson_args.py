def avg(*ns):
    sum = 0
    for n in ns:
        sum = sum + n
    print(sum/len(ns))

avg(3,4)
avg(1, 4, -1, -8)
avg(3, 6 , 7, 4)