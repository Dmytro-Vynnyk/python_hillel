lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0, 1]
no_zero = []
zero_count = 0

for num in lst:
    zero_count += 1 if num == 0 else 0
    no_zero.append(num) if num != 0 else None

print(no_zero + [0] * zero_count)
