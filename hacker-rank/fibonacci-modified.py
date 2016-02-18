def fib_modified(a, b, n):
    return _fib_modified(a, b, n-1, [ None ] * n)

def _fib_modified(a, b, n, cache):
    if n == 0:
        return a
    if n == 1:
        return b
    if cache[n] is None:
        cache[n] = _fib_modified(a, b, n-1, cache) ** 2 + _fib_modified(a, b, n-2, cache)
    return cache[n]

if __name__ == "__main__":
    a, b, n = ( int(i) for i in input().strip().split(' ') )
    print(fib_modified(a, b, n))