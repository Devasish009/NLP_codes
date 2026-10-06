# Porter Stemming Algorithm - Basic Implementation

def porter_stem(word):

    if word.endswith("sses"):
        word = word[:-2]

    elif word.endswith("ies"):
        word = word[:-2]

    elif word.endswith("ss"):
        pass

    elif word.endswith("s"):
        word = word[:-1]

    if word.endswith("eed"):
        if len(word) > 3:
            word = word[:-1]

    elif word.endswith("ed") and "e" in word[:-2]:
        word = word[:-2]

    elif word.endswith("ing") and "e" in word[:-3]:
        word = word[:-3]

    if word.endswith("y") and len(word) > 2:
        word = word[:-1] + "i"

    return word


words = input("Enter words separated by spaces: ").lower().split()

print("\nOriginal Word -> Stem")
print("---------------------")

for word in words:
    stem = porter_stem(word)
    print(f"{word:15} -> {stem}")
