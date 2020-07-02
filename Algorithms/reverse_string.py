"""
Given a string of words, reverse all the words

start = "This is the best"
finish = "best the is This"
"""


def reverse(str):
    length = len(str) 
    spaces = [' ']
    words = []
    i = 0
    while i < length:
        if str[i] not in spaces:
            word_start = i
            while i < length and str[i] not in spaces:
                i += 1
            words.append(str[word_start:i])
        i += 1
    return " ".join(reversed(str))


print(reverse("This is the best"))