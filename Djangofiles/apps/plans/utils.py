import base64
import json

def decrypt_string(encoded):
    decoded = base64.b64decode(encoded).decode("utf-8")
    return json.loads(decoded)
