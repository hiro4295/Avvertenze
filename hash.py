from hashlib import sha256
h = sha256()
h.update(b'ILoveDiscord666')
hash = h.hexdigest()
print(hash)