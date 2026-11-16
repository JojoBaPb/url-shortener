import string

from app import keygen

ALLOWED = set(string.ascii_letters + string.digits)


def test_random_key_has_requested_length_and_safe_characters():
    key = keygen.create_random_key(length=9)
    assert len(key) == 9
    assert set(key) <= ALLOWED


def test_keys_are_not_repeated():
    keys = {keygen.create_random_key() for _ in range(1000)}
    assert len(keys) == 1000


def test_secret_key_is_longer_than_short_key():
    assert len(keygen.create_unique_random_key()) > len(keygen.create_random_key())
