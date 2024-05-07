def caeser_cipher(shift, text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result


def encrypt_text():
    shift = int(input("Shift: "))
    text = input("Text: ")
    encrypted_text = caeser_cipher(shift, text)
    print("'" + encrypted_text + "'" + ", your text is also in a file in the same directory called 'Encrypted Text.txt.'")
    file = open("Encrypted Text.txt", "w")
    file.write(encrypted_text)
    file.close()



def decrypt_text():
    shift = int(input("Shift: "))
    text = input("Text: ")
    decrypted_text = caeser_cipher(-shift, text)
    print("'" + decrypted_text + "'" + ", your text is also in a file in the same directory called 'Decrypted Text.txt.'")
    file = open("Decrypted Text.txt", "w")
    file.write(decrypted_text)
    file.close()


def main():
    while True:
        user_input = input("Would you like to encrypt, decrypt, or exit?: ")
        if user_input.lower() == "encrypt":
            encrypt_text()
        elif user_input.lower() == "decrypt":
            decrypt_text()
        elif user_input.lower() == "exit":
            break
        else:
            print("Please enter either 'encrypt', 'decrypt', or 'exit.'")


main()
