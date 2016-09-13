import string

alphabet = string.ascii_lowercase
reverse_alphabet = alphabet[::-1]

# Key as dictionary
key = {}
for i, letter in enumerate(alphabet):
    key[letter] = reverse_alphabet[i]

def encode(text):
    """
    Encodes a string using the Atbash cipher.
    Encoded text is written out in groups of 5 characters, and punctuation is excluded.
    """
    result = ""
    for char in text.lower():
        if char.isalpha():
            result += key[char]
        elif char.isdigit():
            result += char
    encoded_words = []
    count = 0
    curr = ""
    while count < len(result):
        if count % 5 == 0:
            encoded_words.append(curr)
            curr = result[count]
        else:
            curr += result[count]
        count += 1
    encoded_words.append(curr)
    return string.lstrip(" ".join(encoded_words))
    
def decode(text):
    """
    Decodes encoded Atbash ciphertext.
    """
    text = text.replace(" ", "")
    result = ""
    for char in text:
        if char.isalpha():
            result += key[char]
        else:
            result += char
    return result