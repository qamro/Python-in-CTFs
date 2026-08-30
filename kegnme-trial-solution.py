import hashlib

username = b"BENNETT"
h = hashlib.sha256(username).hexdigest()

print(h)