"""
Provides functions to calculate the proof of work
and the nonce.
"""
from hashlib import sha256
import logging
logger = logging.getLogger(__name__)
fh = logging.FileHandler(f'{__name__}.log')
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


def proof_of_work(previous_hash, text, prefix="0000"):
    nonce, hash_code = calculate_nonce(previous_hash, text, prefix)
    return nonce, hash_code


def calculate_nonce(previous_hash, text, prefix):

    def valid_hash(hash_code):
        if hash_code:
            return hash_code.startswith(prefix)

        return False

    logger.debug("Input values: %s, %s", previous_hash, text)
    if previous_hash is None or text is None:
        logger.debug("Guard triggered")
        return '', ''
    nonce = -1
    hash_code = None
    while not valid_hash(hash_code):
        nonce += 1
        text_to_encode = previous_hash + text + str(nonce).encode()
        hash_code = sha256(text_to_encode).hexdigest()

    logger.debug("Output values: %s, %s", nonce, hash_code)
    return hex(nonce).replace('0x', ""), hash_code
