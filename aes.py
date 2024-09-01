from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import random

def AESDemo():
    # Parameters for AES
    key_size = 32  # AES-256 uses a 32-byte key
    block_size = AES.block_size  # Typically 16 bytes for AES

    # Generate a random 256-bit key
    key = get_random_bytes(key_size)

    # Generate a random message for X (several blocks and padding)
    m = random.getrandbits(600)  # Random number with up to 600 bits
    m_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')

    # AES Encryption with padding (similar to AESEncrypt in the pseudocode)
    cipher = AES.new(key, AES.MODE_CBC)
    c = cipher.encrypt(pad(m_bytes, block_size))

    print("m =", m)
    print("c =", c.hex())

    # AES Decryption (similar to AESDecrypt in the pseudocode)
    decrypted_m_bytes = unpad(cipher.decrypt(c), block_size)
    decrypted_m = int.from_bytes(decrypted_m_bytes, byteorder='big')

    print("decrypted =", decrypted_m)

    # Generate a smaller random message for Y (only one underfull block)
    y = random.randint(0, 100)
    y_bytes = y.to_bytes((y.bit_length() + 7) // 8 or 1, byteorder='big')

    # AES raw encryption without padding (similar to AESRawEncrypt in the pseudocode)
    cipher_raw = AES.new(key, AES.MODE_ECB)
    c_raw = cipher_raw.encrypt(pad(y_bytes, block_size))

    print("\nm =", y)
    print("c =", c_raw.hex())

    # AES raw decryption (similar to AESRawDecrypt in the pseudocode)
    decrypted_y_bytes = unpad(cipher_raw.decrypt(c_raw), block_size)
    decrypted_y = int.from_bytes(decrypted_y_bytes, byteorder='big')

    print("decrypted =", decrypted_y)

    # Verify that decryption after encryption returns the original value
    test_value = 222
    test_value_bytes = test_value.to_bytes((test_value.bit_length() + 7) // 8 or 1, byteorder='big')

    cipher_test = AES.new(key, AES.MODE_CBC)
    c_test = cipher_test.encrypt(pad(test_value_bytes, block_size))
    decrypted_test_bytes = unpad(cipher_test.decrypt(c_test), block_size)
    decrypted_test = int.from_bytes(decrypted_test_bytes, byteorder='big')

    print("\nverifying decryption after encryption = identity: 222 =", decrypted_test)

    # Attempting raw decryption (note: ECB mode is deterministic, use CBC mode in practice)
    raw_decrypt_test = unpad(cipher_raw.decrypt(c_test[:block_size]), block_size)
    decrypted_raw = int.from_bytes(raw_decrypt_test, byteorder='big')

    print(decrypted_raw)

    # The following would cause an error since padding might be incorrect
    # print(AESDecrypt(222,3,999))  # In the pseudocode, this would throw an exception

if __name__ == "__main__":
    AESDemo()
