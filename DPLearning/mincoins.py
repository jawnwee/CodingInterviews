memo = [-1] * 128
denominations = [1, 2, 3, 4, 5]

def min_coin(n):
    if n < 0: return 1000000000
    if n == 0: return 0
    if memo[n] != -1: return memo[n]

    ans = 1000000000
    for i in range(5):
        ans = min(ans, min_coin(n - denominations[i]))
    memo[n] = ans + 1

    return memo[n]
