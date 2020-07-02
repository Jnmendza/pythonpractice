"""
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be
written using the exact same letters(so you can just rearrange the letters to get a different
phrase or word).

For Example:
"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" & "o d g"
"""


def anagram(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Check if same you have same number of letters
    if len(s1) != len(s2):
        return False
    # Count frequency of each letter
    count = {}

    for letter in s1:  # for every letter in the first string
        if letter in count:  # if letter is already in my dict, then
            count[letter] += 1  # add 1 to that letter key
        else:
            count[letter] = 1

            # do reverse for second string
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


x = anagram('Clint Eastwood', "old WEST action")
print(x)
