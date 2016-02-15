import hashlib


def sha1(raw):
    hasher = hashlib.sha1()
    hasher.update(raw)

    return hasher.hexdigest()


def sha256(raw):
    hasher = hashlib.sha256()
    hasher.update(raw)

    return hasher.hexdigest()
