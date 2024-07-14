import alpha
from logo import logo
import os
repeat = True


def ask(question):
    if question == 'encode':
        alpha.encrypt(plain_text=text, shift_amount=int(shift))
    elif question == 'decode':
        alpha.decrypt(cipher=text, shift_amount=int(shift))
    else:
        print('error')


while repeat:
    os.system('cls')
    print(logo)
    print('\nGive shift less than 30 and more than 0')
    direction = input(
        "Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text = input('Type your message ')
    shift = input("Type the shift number\n")
    ask(question=direction)
    asked = input("Type 'yes' if you want to go again..otherwise type 'no'")
    os.system('cls')
    if asked == 'no':
        repeat = False
        print("Bye Bye")

input()
