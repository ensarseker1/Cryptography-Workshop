import math

def gcd(a, b):
    """Compute the greatest common divisor (GCD) of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Find the multiplicative inverse of e modulo phi."""
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2, x1 = x1, x
        d, y1 = y1, y
    
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
    """Generate the public and private keys."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Compute the private key
    d = multiplicative_inverse(e, phi)

    # Return the public and private keys
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    """Encrypt the plaintext with the public key."""
    e, n = pk
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    """Decrypt the ciphertext with the private key."""
    d, n = pk
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Example usage:
p = 61  # first prime number
q = 53  # second prime number

# Generate public and private keys
public, private = generate_keypair(p, q)
print(f"Public key: {public}")
print(f"Private key: {private}")

message = "HELLO"
print(f"Original message: {message}")

# Encrypt the message
encrypted_msg = encrypt(public, message)
print(f"Encrypted message: {encrypted_msg}")

# Decrypt the message
decrypted_msg = decrypt(private, encrypted_msg)
print(f"Decrypted message: {decrypted_msg}")
