import base64
import random
import string
import math
from collections import Counter


# =========================
# ENCODING
# =========================
def base64_encode(data):
    return base64.b64encode(data.encode()).decode()


def xor_encode(data, key):
    return ''.join(
        chr(ord(c) ^ ord(key[i % len(key)]))
        for i, c in enumerate(data)
    )


# =========================
# OBFUSCATION
# =========================
def random_insertion(data):
    return ''.join(c + random.choice(string.ascii_letters) for c in data)


def html_obfuscation(data):
    return "".join(f"&#{ord(c)};" for c in data)


def strong_obfuscation(data):
    return ''.join(chr(ord(c) + 5) for c in data[::-1])


def multi_layer_obfuscation(data, key):
    step1 = xor_encode(data, key)
    step2 = base64_encode(step1)
    step3 = strong_obfuscation(step2)
    return step3


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


# =========================
# MAIN PROGRAM
# =========================
def main():
    print("\n=== Payload Obfuscation Tool ===\n")

    payload = input("Enter Payload: ")
    key = input("Enter XOR Key (default: key): ") or "key"

    print("\n[+] Generating...\n")

    # Encoding
    b64 = base64_encode(payload)
    xor = base64_encode(xor_encode(payload, key))

    # Obfuscation
    rand = random_insertion(payload)
    html = html_obfuscation(payload)
    strong = strong_obfuscation(payload)
    multi = multi_layer_obfuscation(payload, key)

    # Entropy
    print("Entropy Analysis:")
    print("Original :", calculate_entropy(payload))
    print("Base64   :", calculate_entropy(b64))
    print("XOR      :", calculate_entropy(xor))
    print("Strong   :", calculate_entropy(strong))
    print("Multi    :", calculate_entropy(multi))

    print("\n=== RESULTS ===\n")

    print("[Original]")
    print(payload)

    print("\n[Base64]")
    print(b64)

    print("\n[XOR + Base64]")
    print(xor)

    print("\n[Random Obfuscation]")
    print(rand)

    print("\n[HTML Encoding]")
    print(html)

    print("\n[Strong Obfuscation]")
    print(strong)

    print("\n[Multi-layer Obfuscation]")
    print(multi)


if __name__ == "__main__":
    main()
    main()
