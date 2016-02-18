# Google
# Given a sorted array of size N of int32, find an element that repeats > ceil(N / 2) times. Your algo may assume that there will be always such element. Space/time O(1).
# Follow up question: Now element repeats > ceil(N / 4) times. Space/time O(1)
            
# [ 1,1,1,1,1,2,3,4,5 ]

def find_repeat(a):
    return a[(len(a)-1)//2]

if __name__ == "__main__":
    a = [ 1,1,1,1,1,2,3,4,5 ]
    print(find_repeat(a))

# [ 1,2,2,2,3,4,5,6,7 ]
# [ 1,2,2,2,3,3,3,4,4 ]
# [ 1,2,3,4,4,4,5,6,7 ]

def find_repeat(a):
    k = len(a) // 8
    for i in range(k, len(a)-k, k):
        if a[i-k] == a[i] and a[i] == a[i+k]:
            return a[i]
    return None

# (still unsolved)

if __name__ == "__main__":
    a = [ 1,2,2,2,2,2,5,6,7,8,9,10,11,12,13,14 ]
    print(find_repeat(a)) # => 2
    a = [ 1,2,2,2,3,3,3,4,4,8,10,10,10,10,10,14 ]
    print(find_repeat(a)) # => 10
    a = [ 1,1,1,1,1,6,7,7,7,8,9,10,11,12,13,14 ]
    print(find_repeat(a)) # => 1
    a = [ 2,2,2,4,4,4,5,6,7,8,9,9,9,12,12,12 ]
    print(find_repeat(a)) # => None
    a = [ 1,2,3,4,5,6,7,7,7,7,7,10,11,12,13,14 ]
    print(find_repeat(a)) # => 7