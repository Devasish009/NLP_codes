# Morphological Analysis using Add-Delete Table

rules = [
    ("ing", ""),
    ("ed", ""),
    ("es", ""),
    ("s", ""),
    ("ies", "y")
]

word = input("Enter an inflected word: ").lower()

root = word

for delete, add in rules:
    if word.endswith(delete):
        root = word[:-len(delete)] + add
        break

print("\nMorphological Analysis")
print("--------------------------")
print("Input Word :", word)
print("Root Word :", root)

print("\nGenerated Word Forms")
print("--------------------------")
print("Present :", root)
print("Plural :", root + "s")
print("Past :", root + "ed")
print("Continuous :", root + "ing")
print("Agent Noun :", root + "er")
