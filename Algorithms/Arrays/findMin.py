def findMin(nums):
    l = 0
    h = len(nums) - 1
    m = 0
    while l < h:
        m = (l + h) // 2
        if nums[m] > nums[h]:
            l = m + 1
        else:
            h = m
        return nums[l]
    
list = [43,4,5,1,2]
findMin(list)