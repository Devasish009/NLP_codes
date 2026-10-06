# N-Gram Language Model

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab")

sentence = input("Enter a sentence: ")
n = int(input("Enter the value of N: "))

words = word_tokenize(sentence)

result = list(ngrams(words, n))

print("\nN-grams:")
for gram in result:
    print(gram)
