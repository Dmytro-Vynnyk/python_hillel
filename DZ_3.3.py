list = [1, 2, 3, 4, 5, 6]
number = len(list)
mid = (number + 1) // 2
first_part = list[:mid]
second_part = list[mid:]
result = [first_part, second_part]
print(result)
