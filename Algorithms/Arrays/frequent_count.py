"""
Given an array what is the most frequently occuring element
"""


def frequent_count(arr):
    count = {}
    max_count = 0
    max_item = None

    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item


print(frequent_count([1, 3, 3, 3, 2, 1, 1, 1]))
