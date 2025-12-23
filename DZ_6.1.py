import string

text = input("Enter a range of letters for example a-z: ")
start, end = text.split("-")
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)
result = letters[start_index:end_index + 1]
print(result)
