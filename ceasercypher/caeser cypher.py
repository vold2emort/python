alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(text,shift,direction):
    if direction=='encode':
        encrypt_text = ""
        for i in range(len(text)):
            char = text[i]
            if char in alphabet:
                index = alphabet.index(char)
                index = index + shift
            if index > 25:
                index = index - 26
            encrypt_text+=alphabet[index]
        print(encrypt_text)
    elif direction=='decode':
        decrypt_text = ""
        for i in range(len(text)):
            char = text[i]
            if char in alphabet:
                index = alphabet.index(char)
                index = index - shift
            if index < 0:
                index = index + 26
            decrypt_text += alphabet[index]
        print(decrypt_text)

    else:
        print('not valid')


caeser(text, shift, direction)