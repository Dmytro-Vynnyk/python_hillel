import string, keyword

text = input("Enter a text: ")
is_valid = True

if text[0].isdigit():
    is_valid = False
if text != text.lower():
    is_valid = False
if text.count('_') > 1:
    is_valid = False
if text in keyword.kwlist:
    is_valid = False
for ch in text:
    if ch in string.punctuation and ch != '_':
        is_valid = False
    if ch == ' ':
        is_valid = False

print(is_valid)
