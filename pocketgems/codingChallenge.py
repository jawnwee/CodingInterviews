# Finding longest continguous increasing/decreasing list
# using a slidingwindow
def find_sequence(isIncreasing, scores):
    if scores == []:
        return None
    l_first, l_last = 0, 0
    first, last = 0, 0
    longest_seq = 0
    seq_length = 0
    previous = scores[0]
    for i in xrange(1, len(scores)):
        if isIncreasing:
            if scores[i] > previous:
                last += 1
                seq_length += 1
            else:
                first, last = i, i
                seq_length = 0
        else:
            if scores[i] < previous:
                last += 1
                seq_length += 1
            else:
                first, last = i, i
                seq_length = 0
        if seq_length  > longest_seq:
            longest_seq = seq_length
            l_first, l_last = first, last
        previous = scores[i]
    if seq_length  > longest_seq:
        longest_seq = seq_length
        l_first, l_last = first, last

    return l_first, l_last

# Find the longest contiguous sequence of increasing(for SATs)
# and decreasing(for GPAs). Then see where the overlaps are from the
# tuples and return the pair of SATs and GPAs
def gpa_sat_correlation(sats, gpas):
    longest_increasing_sat = find_sequence(True, sats)
    longest_decreasing_gpa = find_sequence(False, gpas)
    if (longest_decreasing_gpa[0] > longest_increasing_sat[1]) or (longest_decreasing_gpa[1] < longest_increasing_sat[0]):
        return 'No existing counter argument to prove SAT score is indicator of GPA'
    first = 0
    last = 0
    if longest_decreasing_gpa[0] > longest_increasing_sat[0]:
        first = longest_decreasing_gpa[0]
    else:
        first = longest_increasing_sat[0]
    if longest_decreasing_gpa[1] <= longest_increasing_sat[1]:
        last = longest_decreasing_gpa[1]
    else:
        last = longest_increasing_sat[1]
    return (sats[first:last+1], gpas[first:last+1])
