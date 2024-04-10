import string

CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + ' '

def encrypt(message, key):
    encrypted_message = ""
    for chracter in message:
        chracter_index = CHARACTERS.index(chracter)
        
        new_index = chracter_index + key

        if new_index >= len(CHARACTERS):
            new_index = new_index % len(CHARACTERS)

        encrypted_message += CHARACTERS[new_index]

    return encrypted_message

def decrypt(message, key):

    decrypted_message = ""

    for chracter in message:
        chracter_index = CHARACTERS.index(chracter)
        new_index = chracter_index - key

        if new_index < 0:
            new_index = new_index % len(CHARACTERS)

        decrypted_message += CHARACTERS[new_index]

    return decrypted_message

key = 3
message = "Hello World!"
print(message)

encrypted_message = encrypt(message, key)

print(encrypted_message)

decrypted_message = decrypt(encrypted_message, key)

print(decrypted_message)
