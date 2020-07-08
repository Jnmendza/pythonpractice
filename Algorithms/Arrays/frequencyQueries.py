def freqQuery(queries):
    frequency = {}
    collection = []
    freqValues = {}
    for opt, value in queries:
        freq = frequency.get(value, 0)
        if opt == 1:
            frequency[value] = frequency.get(value, 0) + 1
            freqValues[freq] = freqValues.get(freq, 0) + 1
            freqValues[freq - 1] = freqValues.get(freq - 1, 1) - 1
        elif opt == 2:
            if value in frequency.keys():
                frequency[value] += - 1
                if frequency[value] < 0:
                    frequency[value] = 0
                freq = frequency[value]
                freqValues[freq + 1] = freqValues.get(freq + 1, 1) - 1
                freqValues[freq] = freqValues.get(freq, 1) + 1
        elif opt == 3:
            if value in freqValues.keys():
                if freqValues[value] > 0:
                    collection.append(1)
                else:
                    collection.append(0)
            else:
                collection.append(0)

    return collection


queries = [[1, 1], [3, 3], [2, 2], [3, -1], [1, 1], [1, 1], [2, 1], [1, 2], [3, 2]]
print(freqQuery(queries))


'''
collection = []
    for query in queries:
        opt = query[0]
        value = query[1]
        if q == 1:
            pass
        if q == 2:
            pass
        if q = 3:
            pass

    return collection
'''
