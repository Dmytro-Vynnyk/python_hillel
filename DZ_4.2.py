lst = []

total = 0
for i in range(0, len(lst), 2):
    total += lst[i]

result = 0 if not lst else total * lst[-1]
print(result)
