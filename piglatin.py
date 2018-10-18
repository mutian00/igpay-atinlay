before = input("Input a string of words, all lowercase, no special characters or punctuation: ")


def isvowel(element):
    first = element[0]
    if first == "a":
        return True
    elif first == "o":
        return True
    elif first == "e":
        return True
    elif first == "i":
        return True
    elif first == "u":
        return True
    else:
        return False


def vowel(word):
    word = word + "yay"
    return word


def consonant(word):
    char = word[0]
    word = word.lstrip(char) + char + "ay"
    return word


temp = before.split()
i = 0
for x in temp:
    if isvowel(x):
        add = vowel(x)
        temp[i] = add
    else:
        add = consonant(x)
        temp[i] = add
    i += 1

for x in temp:
    print(x, " ", end= "")