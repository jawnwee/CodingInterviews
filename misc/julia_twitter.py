def solution(array):
    n = len(array)
    even = 0
    odd = 0
    for i in array:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    oddAnswers = (odd(odd + 1)) / 2
    evenAnswers = (even(even + 1)) / 2

    return oddAnswers + evenAnswers
