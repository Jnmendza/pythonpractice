"""
Given 2 arrays (assume no duplicates)
is 1 array a rotation of another - return True/False
same size and elements but start index is different

BigO(n) we are going through each array 2x but O(2n) = O(n) since infinite sized lists,
constants means nothing

select an indexed position in list1 and get its value. Find same element in list2 and
check index for index from there
If any variation then we know its false.
Getting to last item without a false means true.
"""


def rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_index = 0

    # This finds the index in list2 that matches the key (index 0 in list1 - first num)
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break

    if key_index == 0:
        return False

    # loop thru list1 now, range gets you the position in the array
    for x in range(len(list1)):
        l2index = (key_index + x) % len(list1)

        if list1[x]!= list2[l2index]:
            return False
    return True


print(rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))