import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
#print(chars)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#ENCRYPT

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"original message : {plain_text}")
print(f"encrypted message : {cipher_text}")

#DECRYPT

cipher_text = input("Enter a message to decrypt: ")
plain_text= ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"encrypted message : {cipher_text}")
print(f"original  message : {plain_text}")

'''
import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
#print(chars)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:              # ← guard added
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter        # unsupported chars passed through unchanged

print(f"original message : {plain_text}")    # ← typo fixed
print(f"encrypted message : {cipher_text}")  # ← typo fixed

# DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    if letter in key:                # ← guard added
        index = key.index(letter)
        plain_text += chars[index]
    else:
        plain_text += letter         # unsupported chars passed through unchanged

print(f"original message : {cipher_text}")
print(f"encrypted message : {plain_text}")'''