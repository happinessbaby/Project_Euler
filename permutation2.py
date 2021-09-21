
memo = {}
def permutations(string):
    if len(string) == 2:
        memo[string] = set([string, string[::-1]])
        return memo[string]
    memo.setdefault(string, set())
    for i in string:
        s = string.replace(i, '', 1)
        memo[string].update([i + p for p in permutations(s)])
    return sorted(memo[string])


list = permutations('0123456789')
print(list[1000000])
