import codecs

cipher_string = open('cipher.txt').read().strip()

print(cipher_string)

b64 = codecs.encode(codecs.decode(cipher_string, 'hex'), 'base64').decode()

print(b64)