import secrets
import string

def create_random_key(length: int = 7) -> str:
    """Generates a random alphanumeric string."""
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_key(length: int = 12) -> str:
    """
    Generates a stronger random string specifically for the secret_key.
    Length is increased to ensure security for admin actions.
    """
    return create_random_key(length=length)
