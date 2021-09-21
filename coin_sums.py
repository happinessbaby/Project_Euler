#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

coins = [1, 2, 5, 10, 20, 50, 100, 200]
memo = {}
def combination(n, coins):
    memo[0] = 1
    for i in range(1, n+1):
        memo[i] = 0
    for i in range(len(coins)):
        for j in range(coins[i], n+1):
            memo[j] += memo[j-coins[i]]
    return memo[n]

print(combination(200, coins))
