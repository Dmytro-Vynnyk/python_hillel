seconds = int(input('Enter the number of seconds from 0 to 8639999: '))

while seconds < 0 or seconds >= 8640000:
    print('Error! Enter a number from 0 to 8639999.')
    seconds = int(input('Enter the number of seconds from 0 to 8639999: '))

SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60

days, seconds = divmod(seconds, SECONDS_IN_DAY)
hours, seconds = divmod(seconds, SECONDS_IN_HOUR)
minutes, seconds = divmod(seconds, SECONDS_IN_MINUTE)

if days % 100 in (11, 12, 13, 14):
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif days % 10 in (2, 3, 4):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
