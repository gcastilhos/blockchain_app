"""
Unit tests for Proof Of Work module.
"""
from hashlib import sha256


def test_proof_of_work():
    previous_hash = b"Some hash"
    text = b"Some text"
    hashed = proof_of_work(previous_hash, text)
    assert len(hashed) == 64


def proof_of_work(previous_hash, text):
    nonce = calculate_nonce(previous_hash, text)
    return sha256(previous_hash + text + nonce).hexdigest()
 

def calculate_nonce(previous_hash, text):

    def valid_nonce(nonce):
        if nonce:
            return nonce[0] == "0"
        return False

    nonce = ""
    counter = 0
    while not valid_nonce(nonce):
       nonce = sha256(previous_hash + text + str(counter).encode()).hexdigest()
       counter += 1

    return nonce.encode()
