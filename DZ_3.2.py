numbers = [12, 3, 4, 10, 8]
if len(numbers) > 1:
    last_number = numbers.pop()
    numbers.insert(0, last_number)
print(numbers)
