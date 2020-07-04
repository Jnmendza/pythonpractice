"""
Non repeat element
Take a string and return character that never repeats
if multiple uniques then return only the first unique
"""


def non_repeating(s):
    s = s.replace(' ', '').lower()

    char_count = {} # empty dictionary

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    # The first unique char
    # for c in s:
    #     if char_count[c] == 1:
    #         return c
    # return None

    # All unique chars
    all_uniques = []
    y = sorted(char_count.items(), key=lambda x: x[1])

    for item in y:
        if item[1] == y[0][1]:
            all_uniques.append(item)

    return all_uniques


print(non_repeating("aughuajg jjjz;kj;"))