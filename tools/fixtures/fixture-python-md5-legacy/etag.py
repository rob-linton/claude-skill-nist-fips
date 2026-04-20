"""Fixture: Python using hashlib.md5 — one legacy-ok, one security-relevant."""
import hashlib


def etag_for_cache(data: bytes) -> str:
    """Non-security: cache-busting ETag. Uses usedforsecurity=False."""
    return hashlib.md5(data, usedforsecurity=False).hexdigest()


def password_fingerprint(password: bytes) -> str:
    """SECURITY-RELEVANT: using MD5 on a password is wrong and this use
    case should fail the scanner."""
    return hashlib.md5(password).hexdigest()
