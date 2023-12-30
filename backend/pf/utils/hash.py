import hashlib


def compute_hash(text):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the text
    sha256_hash.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hash_value = sha256_hash.hexdigest()

    return hash_value
