import string

text = input("Enter a text: ").title()
result = "#"

for ch in text:
    if ch not in string.punctuation and ch != ' ':
        result += ch

print(result[:140])
print(len(result[:140]))
