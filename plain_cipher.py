import random
import string

character = " " + string.ascii_letters + string.digits + string.punctuation
character = list(character)
key = character.copy()
random.shuffle(key)

plain_text = input("Enter the plain Text: ")
cipher_text = " "
for letter in plain_text:
    index = character.index(letter)
    cipher_text += key[index]
print(f"Original Message is: {plain_text}")
print(f"Encrypted text is: {cipher_text}")

cipher_text = input("Enter the encrypted Text: ")
plain_text = " "

for letter in cipher_text:
    index = key.index(letter)
    plain_text += character[index]
print(f"Encrypted text: {cipher_text}")
print(f"Your plain text is: {plain_text}")