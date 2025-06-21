"""
Set a secret password.
Ask the user to guess the password.
If the guess is incorrect, it asks again.
If correct, print Access Granted.
"""

password="python@123"
guess=input('Guess the password ')
while guess!=password:
    guess=input('Guess again ')
else:
    print('Access granted')
