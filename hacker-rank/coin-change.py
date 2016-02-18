def make_change(coins, n):
    cache = [ [ None for _ in range(len(coins)) ] for _ in range(n+1) ]
    coins.sort(reverse=True)
    return _make_change(coins, n, 0, cache)

def _make_change(coins, n, i, cache):
    if cache[n][i] is not None:
        return cache[n][i]
    if i >= len(coins)-1:
        return 1
    ways = 0
    possibilities = n // coins[i]
    for j in range(possibilities+1):
        ways += _make_change(coins, n - j * coins[i], i+1, cache)
    cache[n][i] = ways
    return ways

if __name__ == "__main__":
    n, m = ( int(i) for i in input().strip().split(' ') )
    coins = [ int(i) for i in input().strip().split(' ') ]
    print(make_change(coins, n))