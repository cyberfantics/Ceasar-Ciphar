from operator import index


alphabat = ['B','l','m','p','D','q','R','S','T','A','V','j','k','W','7','8','$','%','^','&','*','(',')','_','+','u','v','w','x','r','s','t','.','/',';','\\',',',']','"','|','?','>','<','~','@','#','2','Q','E','3','P','9',' ','0','-','X','Y','Z','1','F','G','U','L','n','o','M','5','I','C','H','4','J','K','6','=',"`",',','a','[',':','b','c','d','N','O','e','h','i','y','f','g','z','a^a','b^b','c^c','d^d','e^e','f^f','g^g','h^h','i^i','j^j','h^h','i^i','j^j','k^k','l^l','m^m','n^n''o^o','p^p','q^q','r^r','s^s','t^t','u^u','v^v','w^w','x^x','y^y','z^z','A^A']

def encrypt(plain_text, shift_amount):
    shift_amount = (shift_amount % 91)
    if shift_amount > 21:
        shift_amount = shift_amount - 20
    cipher = ''
    for letter in plain_text:
        position = alphabat.index(letter)
        if shift_amount > position:
            new_letter = alphabat[position]
            
        new_position = position + shift_amount
        new_letter = alphabat[new_position]
        cipher += new_letter
    print(f"The encoded text is {cipher}")

def decrypt(cipher , shift_amount):
    shift_amount = (shift_amount % 91)
    if shift_amount > 21:
        shift_amount = shift_amount - 20
    plain_text = ''
    for letter in cipher:
        if alphabat[letter] == alphabat[letter+2] and alphabat[letter+1]=='^':
            new_alphabat = alphabat[letter]+alphabat[letter+1]+alphabat[letter+2]
            position = alphabat.index(new_alphabat)

        position = alphabat.index(letter)
        
        position = alphabat.index(letter)
        new_position = position - shift_amount
        new_letter = alphabat[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")
input()``````````````````````````