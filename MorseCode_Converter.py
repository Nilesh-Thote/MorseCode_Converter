def encrypt(msg):
    encrypted_text = ""
    for i in msg:
        for j in MORSE_CODE_DICT:
            if i == j:
                encrypted_text += MORSE_CODE_DICT[j]
                encrypted_text += "   "
    return encrypted_text


def decrypt(msg):
    character = ""
    space = 0
    decrypted_text = ""
    for i in range(len(msg)):
        if msg[i] != " ":
            character += msg[i]
        else:
            space += 1
            if space >= 7 and msg[i + 1] != " ":
                space = 0
                decrypted_text += " "
            elif space == 3 and (character != ""):
                space = 0
                for key in MORSE_CODE_DICT:
                    if character == MORSE_CODE_DICT[key]:
                        decrypted_text += key
                        character = ""

    if character != "":
        for key in MORSE_CODE_DICT:
            if character == MORSE_CODE_DICT[key]:
                decrypted_text += key
    return decrypted_text


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '       '}

while True:
    option = input("Do you want to encrypt or decrypt? type encrypt/decrypt or 'q' to quit : ")
    if option.lower() == "encrypt":
        text = input(f"Enter the plaintext to {option} into morse code: ")
        print(f"Morse code is: {encrypt(text.upper())}")
    elif option.lower() == "decrypt":
        text = input(f"Enter the morse code to {option}: ")
        print(f"Plaintext is: {decrypt(text)}")
    elif option == "q":
        break
    else:
        print("INVALID CHOICE")
