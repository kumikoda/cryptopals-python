from Crypto.Cipher import AES


def aes_ecb_128(bs: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, mode=AES.MODE_ECB)
    return cipher.decrypt(bs)
