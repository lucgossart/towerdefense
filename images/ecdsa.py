from base64 import b64decode, b64encode
from hashlib import sha256


def find_private_key(hash_1, hash_2, r, s_1, s_2):
    byte_key = int.to_bytes((hash_1 * s_2 - hash_2 * s_1) / (r * (s_1 - s_2)), 400, 'big')
    return b64encode(byte_key)


sig_1 = b64decode("MIGGAkFeYtWN7tbePVn9X8zMe8iWmZ6TkGb72wWdppzD8rahU5fHsZDFHyt1ClycERWjdYUSQ5ICxbaXYLwmM07WwjyfrwJBMl3R/ueRVRPpRfLBWEOx5+W6Jeti9WEET+35T66vrHEeCQeKsRxcxgAyOSOb7878ot2GZVuN0T6lLsCJ4/9J8og=")

sig_2 = b64decode("MIGGAkFeYtWN7tbePVn9X8zMe8iWmZ6TkGb72wWdppzD8rahU5fHsZDFHyt1ClycERWjdYUSQ5ICxbaXYLwmM07WwjyfrwJBf4r/LBS+gkEWcx/uhXDfFRLnUxiQIo4xfRsmfNvc2Z5KWuEkq5xRtqKOh6uaKTljTSHAifIRuJDbMXnU97qCCCo=")

pubkey = b64decode('MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQBv/nz0v6nrOmHKBq6SBBvJac3+CDw9p8oyVO6EfTAKpy3uh/KUo+J6mRYIe3yhbhvfHIGsoGdMM7CFW/3Yf7r9zYAUfNC+gdHX3EMIvaYaXf0mohBKgVhMQX2wkciQF2FF3ssmdVXNJidtTq8gQXFkaMDim0oauzpKc1vYkKuwsQ60cM=')

r = b'0\x81\x86\x02A^b\xd5\x8d\xee\xd6\xde=Y\xfd_\xcc\xcc{\xc8\x96\x99\x9e\x93\x90f\xfb\xdb\x05\x9d\xa6\x9c\xc3\xf2\xb6\xa1S\x97\xc7\xb1\x90\xc5\x1f+u\n\\\x9c\x11\x15\xa3u\x85\x12C\x92\x02\xc5\xb6\x97`\xbc&3N\xd6\xc2<\x9f\xaf\x02A'

s_1 = b'2]\xd1\xfe\xe7\x91U\x13\xe9E\xf2\xc1XC\xb1\xe7\xe5\xba%\xebb\xf5a\x04O\xed\xf9O\xae\xaf\xacq\x1e\t\x07\x8a\xb1\x1c\\\xc6\x0029#\x9b\xef\xce\xfc\xa2\xdd\x86e[\x8d\xd1>\xa5.\xc0\x89\xe3\xffI\xf2\x88'
s_2 = b'\x7f\x8a\xff,\x14\xbe\x82A\x16s\x1f\xee\x85p\xdf\x15\x12\xe7S\x18\x90"\x8e1}\x1b&|\xdb\xdc\xd9\x9eJZ\xe1$\xab\x9cQ\xb6\xa2\x8e\x87\xab\x9a)9cM!\xc0\x89\xf2\x11\xb8\x90\xdb1y\xd4\xf7\xba\x82\x08*'
print(len(r))
print(len(s_1))
print(len(s_2))
print(len(pubkey), '\n', pubkey)

chain_1 = b'This implementation failure was used, for example, to extract the signing key used for the PlayStation 3 gaming-console.'
chain_2 = b'Initially, they must agree on the curve parameters (CURVE,G,n).'

hash_1 = sha256(chain_1).digest()
hash_2 = sha256(chain_2).digest()

print(len(hash_2))
print(len(hash_1))

r = int.from_bytes(r, "big")
s_1 = int.from_bytes(s_1, "big")
s_2 = int.from_bytes(s_2, "big")
hash_1 = int.from_bytes(hash_1, 'big')
hash_2 = int.from_bytes(hash_2, 'big')

# find_private_key(hash_1, hash_2, r, s_1, s_2)

# print((hash_1 * s_2 - hash_2 * s_1) / (r * (s_1 - s_2)))
print(hash_1)
print(hash_2)
print(s_1)
print(s_2)
print((hash_1 - hash_2) / (s_1 - s_2))
