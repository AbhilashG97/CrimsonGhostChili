def decode_hex(hex_value):
    return bytes.fromhex(hex_value);

def get_xor(buffer_one, buffer_two):

    byte_buffer_one = decode_hex(buffer_one)
    byte_buffer_two = decode_hex(buffer_two)

    return bytes([x ^ y for x, y in zip(byte_buffer_one, byte_buffer_two)]).hex()

list_cipher_string = [cipher.strip() for cipher in open('cipher.txt').read().split("\n")]

print(get_xor(list_cipher_string[0], list_cipher_string[1]))