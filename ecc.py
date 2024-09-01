from tinyec import registry
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import os

def compress_point(point):
    """Compress an elliptic curve point to make it shorter."""
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_encrypt(msg, pubKey):
    """Encrypt a message using ECIES."""
    curve = registry.get_curve('brainpoolP256r1')  # Using the brainpoolP256r1 curve
    privKey = os.urandom(32)  # Generate a random private key (32 bytes for 256 bits)
    pubKeyPt = privKey * curve.g  # Generate the corresponding public key point
    sharedECCKey = privKey * pubKey  # Generate the shared ECC key
    secret = SHA256.new(compress_point(sharedECCKey).encode()).digest()  # Derive an AES key from the shared ECC key
    cipher = AES.new(secret, AES.MODE_CBC)  # Initialize AES in CBC mode
    ciphertext = cipher.encrypt(pad(msg.encode(), AES.block_size))  # Encrypt and pad the message
    return (ciphertext, pubKeyPt, cipher.iv)  # Return the ciphertext, public key point, and AES IV

def ecc_decrypt(encMsg, privKey):
    """Decrypt a message using ECIES."""
    (ciphertext, pubKeyPt, iv) = encMsg  # Unpack the encrypted message components
    sharedECCKey = privKey * pubKeyPt  # Generate the shared ECC key
    secret = SHA256.new(compress_point(sharedECCKey).encode()).digest()  # Derive the AES key from the shared ECC key
    cipher = AES.new(secret, AES.MODE_CBC, iv)  # Initialize AES in CBC mode with the given IV
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt and unpad the message
    return plaintext.decode()  # Return the decrypted message as a string

# Example usage:
msg = "HELLO ECIES"  # The message to be encrypted
curve = registry.get_curve('brainpoolP256r1')  # Define the elliptic curve
privKey = os.urandom(32)  # Generate a random private key
pubKey = privKey * curve.g  # Generate the corresponding public key

# Encrypt the message
encMsg = ecc_encrypt(msg, pubKey)
print("Encrypted message:", encMsg[0].hex())  # Print the encrypted message in hexadecimal format

# Decrypt the message
decMsg = ecc_decrypt(encMsg, privKey)
print("Decrypted message:", decMsg)  # Print the decrypted message


