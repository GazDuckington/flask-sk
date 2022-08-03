from functools import wraps
import os

from dotenv import load_dotenv
from flask import request

load_dotenv()

key = os.environ.get("VITE_API_KEY")

def secure(f):
    @wraps(f)
    def check_authorization(*args, **kwargs):
        return f() if request.headers.get("Authorization") == key else "you are not authorized"

    return check_authorization
