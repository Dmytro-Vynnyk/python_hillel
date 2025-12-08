# Квадрат числа.
square = float(input("Enter a number: "))
print(f"The square of your number {square ** 2}")

# Середнє трьох чисел
average = float(input("Enter three number 1: "))
average1 = float(input("Enter three number 2: "))
average2 = float(input("Enter three number 3: "))
print(f"The average of your number {(average + average1 + average2) / 3}")

# Перетворення хвилин у години
min = int(input("Enter minutes: "))
hours = min // 60
remainder = min % 60
print(f"{hours} hours {remainder} minutes")

# Розрахунок знижки
prise = float(input("Enter the prise of the product: "))
discount = float(input("Enter the discount in percentage: "))
discount_amount = prise * discount / 100
final_price = prise - discount_amount
print(f"Discounted price: {final_price} UAN")

# Остання цифра числа
int_number = int(input('Enter an integer: '))
print(f"Last digit: {int_number % 10}")

# Периметр прямокутника
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))
print(f"Perimeter {2 * (length + width)} cm")

# Виведення числа в стовпчик
number = int(input("Enter a 4-digit integer: "))
thousands = (number // 1000)
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10
print(thousands)
print(hundreds)
print(tens)
print(ones)
