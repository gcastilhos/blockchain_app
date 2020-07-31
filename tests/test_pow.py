"""
Unit tests for Proof Of Work module.
"""
from bchain.pow import proof_of_work
from bchain.bchain import create_block, create_block_chain


def test_proof_of_work():
    previous_hash = b"Some hash"
    text = b"Some text"
    _, hashed = proof_of_work(previous_hash, text)
    assert len(hashed) == 64
    assert hashed.startswith("0")


def test_create_block_chain():
    previous_hash = ("0000000308e7e0bea95a3e88e4e406c3"
                     "7133f0929c80866bda04bc0bce53a15")
    nonce = '23df'
    hash_list = create_block_chain(previous_hash, nonce)
    assert len(hash_list) == 7
    assert isinstance(hash_list[0], tuple)
