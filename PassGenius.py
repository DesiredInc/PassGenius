from cgi import print_arguments
import random
import colorama
print(colorama.Fore.GREEN + 'PassGenius | Grade-collab')
print(colorama.Fore.RESET)
CHARS, SPECIALS, NUMBERS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz', '+-/*!&$#?=w@<>', '1234567890'

includes = int(input("1: symbols + numbers\n2: symbols + special characters\n3: special characters + symbols + numbers\nType:"))
length = int(input("password length:\n"))

alphabet = CHARS
if includes == 1:
    alphabet += NUMBERS
elif includes == 2:
    alphabet += SPECIALS
elif includes == 3:
    alphabet += NUMBERS + SPECIALS

password = ''
for i in range(length):
    password += random.choice(alphabet)
print(password)