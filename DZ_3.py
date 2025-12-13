number1 = float(input("Enter a number 1: "))
action = input("Enter a mathematical operation (+, -, *, /): ")
number2 = float(input("Enter a number 2: "))
result = None
if action == "+":
    result = number1 + number2
elif action == "-":
    result = number1 - number2
elif action == "*":
    result = number1 * number2
elif action == "/":
    if number2 == 0:
        print("Error: You cannot divide by 0!")
    else:
        result = number1 / number2
else:
    print("Invalid operation")
# if result >= 0:
#     print(f'Result: {result}')
if result:
    print(f'Result: {result}')
