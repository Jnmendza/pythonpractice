def countSignals(frequencies, filterRanges):
    small_ranges = []
    big_ranges = []
    for small, big in filterRanges:
        small_ranges.append(small)
        big_ranges.append(big)
    lowest_range = min(small_ranges)
    highest_range = max(big_ranges)

    results = []
    not_in_range = []
    for freq in frequencies:
        if freq >= lowest_range and freq <= highest_range:
            results.append(freq)
        else:
            not_in_range.append(freq)
    return len(results)


freq = [15, 8, 14, 16, 21]
filtersRanges = [[13, 15], [10, 17], [13, 17]]
print(countSignals(freq, filtersRanges))