from django.test import TestCase
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice, shuffle
# Create your tests here.
def test():
    checkLowercase = False
    checkUppercase = False
    checkNumbers = False
    checkSpecial = False
    charList = list(ascii_lowercase + ascii_uppercase + digits + '!@#$%^&*()')
    thePassword = "3rwxMXNmkGiY"
    
    while not(checkLowercase and checkUppercase and checkNumbers and checkSpecial):

        # for _ in range(12):
        #     thePassword.append(choice(charList))

        for x in thePassword:
            if x in ascii_lowercase:
                checkLowercase = True
            elif x in ascii_uppercase:
                checkUppercase = True
            elif x in digits:
                checkNumbers = True
            elif x in '!@#$%^&*()':
                checkSpecial = True
        print(0)
        
test()