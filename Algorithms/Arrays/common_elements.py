"""
Common Elements in Two sorted arrays
return the common elements (as an array) between two sorted arrays of integers
Example:
    The common elements between [1,3,4,6,7,9] and [1,2,4,5,9,10] are [1,4,9]
"""


def common_elements(arr1, arr2):
    p1 = 0
    p2 = 0

    result = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1

        else:
            p1 += 1
    return result


print(common_elements([1, 2, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10, 11]))