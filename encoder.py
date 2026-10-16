import base64
import codecs


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()


def rot13(text):
    return codecs.encode(text, "rot_13")


def xor_encode(text, key):
    return bytes([ord(c) ^ key for c in text]).hex()


def xor_decode(hex_data, key):
    return ''.join(chr(b ^ key) for b in bytes.fromhex(hex_data))
