# O(n)

def first_unique_character(txt):
    letters = {}

    for letter in txt:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1

    for letter in letters:
        if letters[letter] == 1:
            return letter

    return "_"

txt = "aaabcccdeeef"

print(first_unique_character(txt))
