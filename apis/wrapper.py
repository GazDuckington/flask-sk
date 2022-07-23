from functools import wraps

from flask import request

key = "ya29.bwLu0ruxXdXe_RMOSYgfiCPORNMHLkf9rCDmV1rKtWu90TuF1d8B2SmdUlrjeOWNYThkgMM"


def secure(f):
    @wraps(f)
    def check_authorization(*args, **kwargs):
        return f() if request.headers.get("Authorization") == key else "lol no"

    return check_authorization
