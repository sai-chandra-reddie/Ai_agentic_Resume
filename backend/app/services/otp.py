import hmac
import hashlib
import time
from app.config import settings

OTP_WINDOW_MINUTES = 10

def _get_time_window() -> int:
    """Returns the current 10-minute time window bucket."""
    return int(time.time()) // (OTP_WINDOW_MINUTES * 60)

def generate_otp(email: str) -> str:
    """Generate a 6-digit OTP derived from email + secret + time window."""
    window = _get_time_window()
    message = f"{email}:{window}".encode()
    secret = settings.SECRET_KEY.encode()
    digest = hmac.new(secret, message, hashlib.sha256).hexdigest()
    # Take first 6 digits from the hex digest
    otp = str(int(digest[:8], 16) % 1_000_000).zfill(6)
    return otp

def verify_otp(email: str, otp: str) -> bool:
    """Verify OTP against current and previous time window (handles edge cases)."""
    window = _get_time_window()
    secret = settings.SECRET_KEY.encode()

    for w in [window, window - 1]:  # allow previous window too
        message = f"{email}:{w}".encode()
        digest = hmac.new(secret, message, hashlib.sha256).hexdigest()
        expected = str(int(digest[:8], 16) % 1_000_000).zfill(6)
        if hmac.compare_digest(expected, otp):
            return True
    return False
