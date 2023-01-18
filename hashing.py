import hashlib
import base64

def hash_password(password):
  m = hashlib.sha256()
  m.update(password.encode('utf-8'))
  m.update(b"SECRET SALT TODO: CHANGE THIS")
  result = base64.urlsafe_b64encode(m.digest())
  return result
