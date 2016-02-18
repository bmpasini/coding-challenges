def knapsack(a, k):
    m = [ 0 ] * (k+1)
    for i in range(len(a)):
        for j in range(1, k+1):
            if a[i] <= j:
                m[j] = max(m[j], a[i] + m[j-a[i]])
    return m[-1]

for _ in range(int(input())):
    n, k = ( int(i) for i in input().split(' ') )
    a = [ int(i) for i in input().split(' ') ]
    print(knapsack(a, k))
    