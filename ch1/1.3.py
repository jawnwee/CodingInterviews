def isPermutation(first, second):
    if len(first) != len(second):
        return False
    first_dict = {}
    second_dict = {}
    for c in first:
        first_dict[c] = 0
    for c in first:
        first_dict[c] += 1
    for c in second:
        second_dict[c] = 0
    if len(first_dict) != len(second_dict):
        return False
    for c in second:
        second_dict[c] += 1
    for c in first:
        if c in second_dict:
            if second_dict[c] != first_dict[c]:
                return False
    return True

