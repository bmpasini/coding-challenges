# Find the n-th smallest multiple given a set of numbers. For example, set = {4, 6}, n = 6: 
# The sequence is: 
# 4, 6, 8, 12, 16, 18, etc... 
# Answer is 18

def find_nth_multiple(nums, n):
    multiples = set()
    i = 1
    while len(multiples) < n:
        for k in nums:
            multiples.add(i*k)
        i += 1
    sorted_multiples = sorted(multiples)
    print(sorted_multiples)
    return sorted_multiples[-1]

if __name__ == "__main__":
    _set = set()
    _set.add(4)
    _set.add(6)
    print(find_nth_multiple(_set, 6))
