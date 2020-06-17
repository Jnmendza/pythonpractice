import unittest

def merge_ranges(meetings):
    # Merge meeting ranges
    """
    [(1,3),(3,4)]
     first  second

     first = index or i
     second = index + 1 or i + 1

     for start_time, end_time in range of len(meetings):

     If end_time of first is >= second.start_time then merge into on range
     merge:
        start_time = first.start_time

        end_time = the max() of end_times for both first and second
        end_time = max(first.end_time, second.end_time)

    Else, leave them seperated

    Compare every meeting to every other meeting. Merge them or leave them

    """

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetins with the earliest meeting
    merge_meetings = [sorted_meetings[0]]

    for curr_meeting_start, curr_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merge_meetings[-1]

        if curr_meeting_start <= last_merged_meeting_end:
            merge_meetings[-1] = (last_merged_meeting_start,
                                  max(last_merged_meeting_end, curr_meeting_end))

        else:
            merge_meetings.append((curr_meeting_start, curr_meeting_end))

    return merge_meetings


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)