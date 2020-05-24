"""
Unit tests for Proof Of Work module.
"""
from bchain.pow import proof_of_work


def test_proof_of_work():
    previous_hash = b"Some hash"
    text = b"Some text"
    _, hashed = proof_of_work(previous_hash, text)
    assert len(hashed) == 64
    assert hashed.startswith("0")

