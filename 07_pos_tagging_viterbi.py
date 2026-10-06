# POS Tagging using Emission Probability,
# Transition Probability and Viterbi Algorithm

from collections import Counter
import pandas as pd

# POS-tagged training corpus
corpus = [
    [("The", "DT"), ("dog", "NN"), ("eats", "VBZ"), ("food", "NN")],
    [("The", "DT"), ("cat", "NN"), ("eats", "VBZ"), ("fish", "NN")],
    [("A", "DT"), ("dog", "NN"), ("likes", "VBZ"), ("the", "DT"), ("cat", "NN")],
    [("She", "PRP"), ("reads", "VBZ"), ("the", "DT"), ("book", "NN")],
    [("I", "PRP"), ("like", "VB"), ("the", "DT"), ("book", "NN")],
    [("The", "DT"), ("book", "NN"), ("is", "VBZ"), ("good", "JJ")]
]

tag_counts = Counter()
word_tag_counts = Counter()
transition_counts = Counter()
previous_tag_counts = Counter()

for sentence in corpus:
    previous_tag = "START"

    for word, tag in sentence:
        word = word.lower()

        tag_counts[tag] += 1
        word_tag_counts[(word, tag)] += 1

        transition_counts[(previous_tag, tag)] += 1
        previous_tag_counts[previous_tag] += 1

        previous_tag = tag

# Emission probabilities: P(word | tag)
emission_prob = {}

for (word, tag), count in word_tag_counts.items():
    emission_prob[(word, tag)] = count / tag_counts[tag]

# Transition probabilities: P(current_tag | previous_tag)
transition_prob = {}

for (previous_tag, current_tag), count in transition_counts.items():
    transition_prob[(previous_tag, current_tag)] = (
        count / previous_tag_counts[previous_tag]
    )

# Emission probability matrix
tags = sorted(tag_counts.keys())
words = sorted(set(word for word, tag in word_tag_counts.keys()))

emission_matrix = pd.DataFrame(
    0.0,
    index=tags,
    columns=words
)

for (word, tag), probability in emission_prob.items():
    emission_matrix.loc[tag, word] = probability

print("\n========================================")
print("EMISSION PROBABILITY MATRIX")
print("P(word | tag)")
print("========================================")
print(emission_matrix.round(3))

# Transition probability matrix
transition_matrix = pd.DataFrame(
    0.0,
    index=tags,
    columns=tags
)

for (previous_tag, current_tag), probability in transition_prob.items():
    if previous_tag in tags:
        transition_matrix.loc[previous_tag, current_tag] = probability

print("\n========================================")
print("TRANSITION PROBABILITY MATRIX")
print("P(current tag | previous tag)")
print("========================================")
print(transition_matrix.round(3))


# Viterbi algorithm
def viterbi(sentence):
    sentence = [word.lower() for word in sentence]

    V = [{}]
    path = {}

    # Initialization
    for tag in tags:
        transition = transition_prob.get(("START", tag), 0)
        emission = emission_prob.get((sentence[0], tag), 0)

        V[0][tag] = transition * emission
        path[tag] = [tag]

    # Recursion
    for position in range(1, len(sentence)):
        V.append({})
        new_path = {}

        for current_tag in tags:
            emission = emission_prob.get(
                (sentence[position], current_tag), 0
            )

            best_probability = 0
            best_previous_tag = None

            for previous_tag in tags:
                transition = transition_prob.get(
                    (previous_tag, current_tag), 0
                )

                probability = (
                    V[position - 1][previous_tag]
                    * transition
                    * emission
                )

                if probability > best_probability:
                    best_probability = probability
                    best_previous_tag = previous_tag

            V[position][current_tag] = best_probability

            if best_previous_tag is not None:
                new_path[current_tag] = (
                    path[best_previous_tag] + [current_tag]
                )

        path = new_path

    # Find best final tag
    best_tag = max(V[-1], key=V[-1].get)

    return path[best_tag], V[-1][best_tag]


test_sentence = ["The", "dog", "eats", "the", "fish"]

predicted_tags, probability = viterbi(test_sentence)

print("\n========================================")
print("POS TAGGING RESULT")
print("========================================")

for word, tag in zip(test_sentence, predicted_tags):
    print(f"{word:10} -> {tag}")

print("\nBest Sequence Probability:", probability)
