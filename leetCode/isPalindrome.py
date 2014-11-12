def isPalindrome(x):
    if x < 0:
        return False
    input_factor = 1
    input_number = x
    while input_number >= 10:
        input_factor *= 10
        input_number /= 10
    first_half = x
    while x >= 10:
        beginning = first_half/input_factor
        end = x%10
        print 'beginning', beginning, 'end', end
        if beginning != end:
            return False
        first_half = first_half % input_factor
        input_factor /= 10
        x /= 10
    return True
