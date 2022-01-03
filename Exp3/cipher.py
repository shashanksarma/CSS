from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

plain_text = b"This is a top secret."
cipher_hex = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"
result_k = []

file = open('words.txt', 'r')
lines = file.readlines()
words = [str.strip(line) for line in lines]
for word in words:
    if len(word) >= 16:
        continue
    word = word.lower()
    key = word.encode() + b' '*(16-len(word))
    cipher = AES,new(key, AES.MODE_CBC, iv=bytes.fromhex('0'*32))
    ciphertext = cipher.encrypt(pad(plain_text, AES.block_size))
    is_matched = "NOT MATCHED"
    if bytes.hex(ciphertext) == cipher_hex:
        is_matched = "MATCHED"
        result_k.append(word)
    print(word, bytes.hex(ciphertext), is_matched)
print("\n\nThe Resulting Key Is:", result_k)