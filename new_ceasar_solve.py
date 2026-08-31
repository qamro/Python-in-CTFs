import string

ALPHABET = string.ascii_lowercase[:16]

def unshift(c, k):
    t1 = ord(c) - ord('a')
    t2 = ord(k) - ord('a')

    return ALPHABET[(t1 - t2) % 16]


def b16_decode(enc):
    plain = ""

    for i in range(0, len(enc), 2):
        first = ALPHABET.index(enc[i])
        second = ALPHABET.index(enc[i + 1])

        binary = (first << 4) | second

        plain += chr(binary)

    return plain


ciphertext = "fegdeogdgecoeocgcgchcfcffccfca"

for key in ALPHABET:
    decoded = ""

    for c in ciphertext:
        decoded += unshift(c, key)

    try:
        plaintext = b16_decode(decoded)
        print(key, repr(plaintext))
    except:
        pass
    
    
"""

1. The cipher uses a custom alphabet of only 16 characters:
    ALPHABET = "abcdefghijklmnop"

2. b16_encode() converts each character into 8-bit binary,
    splits it into two 4-bit parts, and maps each part to a-p.
    This is basically Base16 with a custom alphabet.

3. shift() applies a Caesar cipher, but modulo 16 instead of 26.

4. The key has exactly ONE character and must be in a-p:
    assert len(key) == 1
    Therefore, there are only 16 possible keys.

5. Brute-force all keys from a to p.
    For each key:
    - Reverse the Caesar shift (subtract the key).
    - Decode the resulting custom Base16.
    - Check which result is readable.

6. The correct key is 'p', giving:
    et_tu?_77866c61

7. Final flag:
    picoCTF{et_tu?_77866c61}


"""    