# Bigram Language Model and Sentence Probability

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import Counter

nltk.download("punkt")
nltk.download("punkt_tab")

corpus = [
    "I love natural language processing",
    "I love machine learning",
    "I enjoy machine learning",
    "Natural language processing is interesting"
]

unigram_counts = Counter()
bigram_counts = Counter()

for sentence in corpus:
    words = word_tokenize(sentence.lower())
    unigram_counts.update(words)
    sentence_bigrams = list(bigrams(words))
    bigram_counts.update(sentence_bigrams)

print("BIGRAM FREQUENCIES")
print("-" * 30)

for bigram, count in bigram_counts.items():
    print(f"{bigram}: {count}")


def bigram_probability(previous_word, current_word):
    bigram = (previous_word, current_word)
    bigram_count = bigram_counts[bigram]
    previous_word_count = unigram_counts[previous_word]

    if previous_word_count == 0:
        return 0

    return bigram_count / previous_word_count


def sentence_probability(sentence):
    words = word_tokenize(sentence.lower())
    probability = 1.0

    print("\nBIGRAM PROBABILITIES")
    print("-" * 35)

    for previous_word, current_word in bigrams(words):
        prob = bigram_probability(previous_word, current_word)

        print(f"P({current_word}|{previous_word}) = {prob:.4f}")

        probability *= prob

    return probability


test_sentence = input("\nEnter test sentence: ")
probability = sentence_probability(test_sentence)

print("\nSentence:", test_sentence)
print("Probability:", probability)
