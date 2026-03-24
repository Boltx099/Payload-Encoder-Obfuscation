import base64
import math
import random
import string
from collections import Counter


# =========================
# ENCODING
# =========================
def base64_encode(data):
    return base64.b64encode(data.encode()).decode()


def xor_encode(data, key):
    if not key:
        key = "default"

    return ''.join(
        chr(ord(c) ^ ord(key[i % len(key)]))
        for i, c in enumerate(data)
    )


# =========================
# OBFUSCATION
# =========================
def random_insertion(data):
    return ''.join(c + random.choice(string.ascii_letters) for c in data)


def split_payload(data):
    return "' + '".join(data)


def html_obfuscation(data):
    return "".join(f"&#{ord(c)};" for c in data)


# =========================
# ENTROPY
# =========================
def calculate_entropy(data):
    if not data:
        return 0

    counter = Counter(data)
    length = len(data)

    entropy = 0
    for count in counter.values():
        p_x = count / length
        entropy -= p_x * math.log2(p_x)

    return round(entropy, 4)