# access_control.py

def audit_log(func):
    """Decorator to log authorization start and completion."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper


def compute_access_level(control):
    """Compute access level based on control number and favorite artist length."""
    # Example logic: CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    # We'll assume FAVORITE_ARTIST length = 13
    return control * 3 + 13


@audit_log
def validate_access(level):
    """Validate if the access level is above threshold."""
    # Example threshold: CONTROL_NUM * 5
    threshold = 69 * 5  # You can replace 69 with CONTROL_NUM if dynamic
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"