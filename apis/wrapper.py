import os
from functools import wraps
from flask import request
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("VITE_API_KEY")

def secure(f):
    @wraps(f)
    def check_authorization(*args, **kwargs):
        return f() if request.headers.get("Authorization") == key else "lol no"

    return check_authorization
