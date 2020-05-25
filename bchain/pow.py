""":w
Provides functions to calculate the proof of work
and the nonce.
"""
from hashlib import sha256


def proof_of_work(previous_hash, text):
    nonce, hash_code = calculate_nonce(previous_hash, text)
    return nonce, hash_code


def calculate_nonce(previous_hash, text, prefix="0000"):

    def valid_hash(hash_code):
        if hash_code:
            return hash_code.startswith(prefix)

        return False

    nonce = -1
    hash_code = None
    while not valid_hash(hash_code):
        nonce += 1
        text_to_encode = previous_hash + text + str(nonce).encode()
        hash_code = sha256(text_to_encode).hexdigest()

    return nonce, hash_code
