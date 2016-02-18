# find the no of possible patterns in android lock screen. write a program to count them.

from copy import deepcopy

def count_possibilities():
    cnt = 0
    keys = [[ False, False, False ],
            [ False, False, False ],
            [ False, False, False ]]
    for num_of_patterns in range(4,10):
        for i in range(3):
            for j in range(3):
                keys_cp = deepcopy(keys)
                keys_cp[i][j] = True
                cnt += _count_possibilities(keys_cp, 0, i, j, num_of_patterns)
    return cnt

def _count_possibilities(keys, cnt, i, j, num_of_patterns):
    if check_complete(keys, num_of_patterns):
        return 1
    for x in range(3):
        for y in range(3):
            if is_valid(keys, i, j, x, y) and not keys[x][y]:
                keys_cp = deepcopy(keys)
                keys_cp[x][y] = True
                cnt += _count_possibilities(keys_cp, 0, x, y, num_of_patterns)
    return cnt

def is_valid(keys, i, j, x, y):
    if (i == x+1 or i == x-1) and (j == y+1 or j == y-1 or j == y):
        return True
    if (i == x+1 or i == x-1 or i == x) and (j == y+1 or j == y-1):
        return True
    if (i == x+2 or i == x-2) and (j == y+1 or j == y-1):
        return True
    if (i == x+1 or i == x-1) and (j == y+2 or j == y-2):
        return True
    if is_middle_valid(keys, i, j, x, y):
        return True
    return False

def is_middle_valid(keys, i, j, x, y):
    if abs(i-x) == 2 and abs(j-y) == 2:
        return keys[1][1]
    elif abs(i-x) == 2 and j == y:
        return keys[1][j]
    elif abs(j-y) == 2 and i == x:
        return keys[i][1]
    else:
        return False

def check_complete(keys, num_of_patterns):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if keys[i][j]:
                cnt += 1
    return cnt == num_of_patterns

if __name__ == "__main__":
    print(count_possibilities()) # => 389112



