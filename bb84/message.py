def input_message():

    is_ascii = False

    while not is_ascii:

        message = str(input("Enter message to send to Bob: "))
        # Message must be ASCII to convert to binary.
        is_ascii = all(ord(char) < 128 for char in message)

        if not is_ascii:
            print("All characters must be ASCII")

    # Convert each character to its 8 bit binary representation.
    return ''.join(format(ord(char), '08b') for char in message)

def encrypt_message(message, key):

    ciphertext = []

    # The key may be shorter than the message, so only encrypt as many complete characters as the key allows.
    # Floor to the nearest byte to avoid partial characters.
    usable_bits = (min(len(message), len(key)) // 8) * 8

    # XOR each message bit against the corresponding key bit.
    for i in range(usable_bits):
        bit = int(message[i])
        encrypted = bit ^ key[i]
        ciphertext.append(encrypted)

    return ciphertext, usable_bits

def decrypt_message(ciphertext, key):

    plaintext_bits = []
    chars = []

    # XOR each ciphertext bit against the key bit to reverse the encryption.
    for i in range(len(ciphertext)):
        decrypted_bit = ciphertext[i] ^ key[i]
        plaintext_bits.append(decrypted_bit)

    # Regroup the bits into bytes and convert each byte back to a character.
    for i in range(0, len(plaintext_bits) - 7, 8):
        byte = plaintext_bits[i:i+8]
        char_code = int(''.join(str(b) for b in byte), 2)
        chars.append(chr(char_code))

    return ''.join(chars)