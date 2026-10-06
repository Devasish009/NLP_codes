# Word Analysis using Morphological Features

prefixes = ["un", "re", "pre", "dis", "in"]
suffixes = ["ing", "ed", "er", "ly", "s"]

word = input("Enter a word: ")

root = word
prefix = "None"
suffix = "None"

for p in prefixes:
    if word.startswith(p):
        prefix = p
        root = word[len(p):]
        break

for s in suffixes:
    if root.endswith(s):
        suffix = s
        root = root[:-len(s)]
        break

print("\nMorphological Analysis")
print("------------------------")
print("Word :", word)
print("Prefix :", prefix)
print("Root Word :", root)
print("Suffix :", suffix)
print("Length :", len(word))
print("Is Upper :", word.isupper())
print("Is Lower :", word.islower())
print("Is Alpha :", word.isalpha())
