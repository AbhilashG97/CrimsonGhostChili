cipher_string = open('cipher.txt').read().strip()

plain_text = bytes.fromhex(cipher_string)

print(plain_text)
