"""
Given a string, are all characters unique?
should give a True or False return

Uses python built in structures
"""


def unique(string):
    string = string.replace(' ', '')
    char = set()

    for letter in string:
        if letter in char:
            return False
        else:
            char.add(letter)
    return True


print(unique('a b cdef'))