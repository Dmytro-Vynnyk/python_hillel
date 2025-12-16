lst = []

if len(lst) == 0:
    print(0)
else:
    sum = 0

    for i in range(1, len(lst), 2):
        sum += lst[i]

    print(sum * lst[-1])
