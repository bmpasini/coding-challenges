# Google
# How many Fibonacci numbers exists less than a given number n. Can you find a function in
# terms of n, to get the number of fibonacci number less than n.
# Answer: 6 as (0, 1, 1, 2, 3, 5)

def fib_count(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    prev = 0
    x = 1
    cnt = 2
    while prev + x < n:
        x, prev = prev + x, x
        cnt += 1
    return cnt

if __name__ == "__main__":
    print(fib_count(0)) # 0
    print(fib_count(1)) # 1
    print(fib_count(2)) # 3
    print(fib_count(3)) # 4
    print(fib_count(4)) # 5
    print(fib_count(5)) # 5
    print(fib_count(6)) # 6
    print(fib_count(7)) # 6
    print(fib_count(8)) # 6
    print(fib_count(9)) # 7