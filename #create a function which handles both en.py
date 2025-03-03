#create a function which handles both encyption and depcryption. we  used "mod" parameter here.
def encrypt_decrypt(msg, shift, mod='encrypt'):
    result = ""
    # we use for loop to go through each character.
    for char in msg:
        if char.isalpha(): # is a function which checks if letter is alphabet.
            set = ord('A') if char.isupper() else ord('a') # determine uppercase or lowercase letters.
            #shifts the value according to shift value. forward in case of encrypt
            #and back to place in case of decrypt.
            if mod == 'encrypt':
                result += chr((ord(char) - set + shift) % 26 + set)
            elif mod == 'decrypt':
                result += chr((ord(char) - set - shift) % 26 + set)
        else:
            result += char #incase the msg vale is number it will remain as it is.
    return result
# user puts value of msg and shift. to encrypt. shift value is in int form.
msg = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value in integer form: "))
# Encrypt the original message using the given shift value.
encrypted_message = encrypt_decrypt(msg, shift, 'encrypt')
#Decrypt the encrypted message using the same shift value to get back the original message
decrypted_message = encrypt_decrypt(encrypted_message, shift, 'decrypt')
#print the encrypted and decrypted msgs.
print("\nEncrypted message:", encrypted_message)
print("\nDecrypted message:", decrypted_message)
print("\n\n")