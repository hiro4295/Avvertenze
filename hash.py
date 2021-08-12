import json
from hashlib import sha256
h = sha256()
h.update(b'ILoveDiscord666')
with open("data.json", "r") as f: 
    data = json.load(f)

hash = h.hexdigest()
print(hash)