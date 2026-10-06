# Word Generation using Root Word and Suffix

root = input("Enter the root word: ").lower()
suffix = input("Enter the suffix (ing/ed/es/s): ").lower()

if suffix == "ing":
    if root.endswith("ie"):
        word = root[:-2] + "ying"
    elif root.endswith("e") and root != "be":
        word = root[:-1] + "ing"
    else:
        word = root + "ing"

elif suffix == "ed":
    if root.endswith("e"):
        word = root + "d"
    elif root.endswith("y") and root[-2] not in "aeiou":
        word = root[:-1] + "ied"
    else:
        word = root + "ed"

elif suffix == "es":
    if root.endswith(("s", "sh", "ch", "x", "z", "o")):
        word = root + "es"
    elif root.endswith("y") and root[-2] not in "aeiou":
        word = root[:-1] + "ies"
    else:
        word = root + "s"

else:
    word = root + suffix

print("\nRoot Word :", root)
print("Suffix :", suffix)
print("Generated Word :", word)
