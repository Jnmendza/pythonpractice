"""
Given a string of words, reverse all the words

start = "This is the best"
finish = "best the is This"
"""


def reverse(string):
    length = len(string)
    spaces = [' ']
    words = []
    i = 0
    while i < length:
        if string[i] not in spaces:
            word_start = i
            while i < length and string[i] not in spaces:
                i += 1
            words.append(string[word_start:i])
        i += 1
    return " ".join(reversed(string))


print(reverse("This is the best"))