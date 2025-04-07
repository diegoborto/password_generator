import random
import string

lenght = 16
out = ''
password = ''

def generate_random_letter():
    # Choose from uppercase and lowercase letters
    letters = string.ascii_letters
    # Generate random string
    random_letter = random.choice(letters)
    return random_letter

def generate_random_integer():
    n = random.randint(0,9)
    return n

def generate_random_symbol():
    symbols = ['_', '!', '?','%', '$', ':']
    random_symbol = random.choice(symbols)
    return random_symbol

def case_selector():
    case = random.randint(1,3)
    if case == 1:
        out = generate_random_letter()
    elif case == 2:
        out = str(generate_random_integer())
    else:
        out = generate_random_symbol()
    return out

for _ in range(lenght):
    password += case_selector()

print(password)
