letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    
]

# Numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Symbols (common special characters)
symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}','|',
    ';',':',"'",'"',',','.','<','>','/','?','\\'
]
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = letters.index(letter)
        new_position = position + shift_amount
        new_letter = letters[new_position]
        cipher_text += new_letter
    print(f"The encoded message is {cipher_text}")
    
def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = letters.index(letter)
        new_position = position - shift_amount
        new_letter = letters[new_position]
        cipher_text += new_letter
    print(f"The encoded message is {cipher_text}")


while True:
    menu = input("1. Encrypt\n2. Decrypt\n3. Exit\n").strip()
    if menu == '3':
        break
    
    text = input("Type your message:\n").strip().lower()
    shift = int(input("Type the shift number:\n"))
    if menu == '1':
        encrypt(plain_text=text, shift_amount=shift)
    elif menu == '2':
        decrypt(plain_text=text, shift_amount=shift)
    else:
        print("please enter between 1-3")
        

        