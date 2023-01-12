import nltk
import re
from nltk.corpus import words, names

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)


known_words = words.words()
known_names = names.words()
capital_words = []
lower_names = []
for _ in known_names:
    lower_names.append(_.lower())
for _ in known_words:
    capital_words.append(_.capitalize())
all_known = known_names + known_words + capital_words + lower_names


def encrypt(plaintext, shift):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char
    return result


def decrypt(ciphertext, shift):
    return encrypt(ciphertext, shift*(-1))


def crack(string):
    for i in range(1, 26):
        guess = encrypt(string, i)
        word_list = guess.split()
        count = 0
        for x in word_list:
            x = re.sub(r"[^A-Za-z]+", "", x)
            # if x.lower() in known_words or x in known_names:
            if x in all_known:
                count += 1
        if count / len(word_list) > 0.75:
            return guess
    return ""
