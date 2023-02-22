MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(msg):

    output = ''
    for letter in msg:
        # if letter in message is not a space, replace it with the respective morse code
        if letter != ' ':
            output += MORSE_CODE_DICT[letter] + ' '
        # if letter in message is a space, add the space to the cipher
        else:
            output += ' '

    return output


def decrypt(morse):
    # citext is used to form the entire code 'word'

    output = ''
    citext = ''
    morse += ' '
    for code in morse:
        if code != ' ':
            i = 0
            citext += code
        else:
            i += 1
            if i == 2:
                output += ' '
            else:
                output += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return output


e_or_d = input("Would you like to encrypt or decrypt a message? Type 1 for encrypt, 2 for decrypt: ")

if e_or_d == '1':
    message = input("Please input the message you'd like to encrypt: ")
    result = encrypt(message.upper())
    print(f'Your message in morse code: {result}')

elif e_or_d == '2':
    message = input("Please input the morse code you'd like to decrypt: ")
    result = decrypt(message)
    print(f'Your morse code returns this message: {result.lower()}')

else:
    print("That's neither 1 nor 2. ")
