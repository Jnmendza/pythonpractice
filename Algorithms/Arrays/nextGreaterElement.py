def nextGreaterElement(nums1, nums2):
    stack = []
    dic = {}
    for v in nums2:
        while stack and stack[-1] < v:
            k = stack.pop()
            dic[k] = v
        stack.append(v)
    print(dic)
    return [dic.get(v, -1) for v in nums1]


n1 = [4, 1, 2]
n2 = [1, 3, 4, 2]
x = check(n1,n2)
print(x)