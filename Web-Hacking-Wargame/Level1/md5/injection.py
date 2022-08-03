import hashlib

for password in range(1, 111112211) :
    md5_hash = hashlib.md5(str(password).encode()).hexdigest()
    if '273d27' in md5_hash :
        print(password)