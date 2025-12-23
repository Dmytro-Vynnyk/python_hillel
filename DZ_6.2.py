numbers = input('Enter integer number: ')

while len(numbers) > 1:
    product = 1

    for digit in numbers:
        product *= int(digit)
    numbers = str(product)

print(numbers)
