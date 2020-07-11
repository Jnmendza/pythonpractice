def sort_scores(unsorted_scores, highest_possible_score):
    data = {}
    # Sort the scores in O(n) time
    for score in unsorted_scores:
        diff = highest_possible_score - score
        if len(unsorted_scores) <= 1:
            return unsorted_scores
        elif score not in data:
            data[score] = 0
        data[score] = diff
    sorted_scores = sorted(data.items(), key=lambda x: x[1])

    return [i[0] for i in sorted_scores]


sort_scores([30, 60], 100)