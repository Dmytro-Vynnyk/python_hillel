lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0, 1]
no_zero = []
zero_count = 0

for num in lst:
    if num == 0:
        zero_count += 1
    else:
        no_zero.append(num)

print(no_zero + [0] * zero_count)
