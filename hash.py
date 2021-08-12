import json
from hashlib import sha256
h = sha256()
h.update(b'Hiro')
hash = h.hexdigest()
print(hash)