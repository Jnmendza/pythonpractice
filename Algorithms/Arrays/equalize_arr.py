def equalizeArray(arr):
    # count = 0
    # G = {}
    # for i in arr:
    #     if i not in G:
    #         for j in arr:
    #             if i == j:
    #                 count += 1
    #         G[i] = count
    #         count = 0
    #
    # max_val = max(G, key=G.get)
    # return len(arr) - G[max_val]

    frequent_num = max(set(arr), key = arr.count)
    total_ele = len(arr)

    count = 0
    for ele in arr:
        if ele == frequent_num:
            count += 1

        return total_ele - count


array = [3, 3, 2, 1, 3]
print(equalizeArray(array))
