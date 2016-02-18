from math import factorial as fact

def count_pairs(a):
    a.sort()
    cnt = 0
    repeat = 1
    for i in range(1, len(a)):
        if a[i-1] == a[i]:
            repeat += 1
        else:
            if repeat > 1:
                cnt += fact(repeat) / fact(repeat-2) # permutation (n 2)
            repeat = 1
    if repeat > 1:
        cnt += fact(repeat) / fact(repeat-2)
    return int(cnt)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [ int(i) for i in input().strip().split(' ') ]
        print(count_pairs(a))