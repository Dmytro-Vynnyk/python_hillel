import string, keyword

text = input("Enter a text: ")
is_valid = True

if text == "":
    is_valid = False
elif set(text) == {"_"}:
    is_valid = (len(text) == 1)
else:
    if text[0].isdigit():
        is_valid = False
if text != text.lower():
    is_valid = False
if text in keyword.kwlist:
    is_valid = False
for ch in text:
    if ch == ' ' or ch in string.punctuation and ch != '_':
        is_valid = False
        break

print(is_valid)
