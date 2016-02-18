def friendCircles(friends):
    if friends is None or len(friends) == 0:
        return 0
    queue = [ 0 ]
    visited = { 0 }
    result = 0
    while len(queue) != 0:
        x = queue.pop(0)
        for i, is_friend in enumerate(friends[x]):
            if is_friend == 'Y' and i not in visited and i != x:
                queue.append(i)
                visited.add(i)
        if len(queue) == 0:
            result += 1
            for i in range(len(friends)):
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                    break
    return result

if __name__ == "__main__":
    friends = ["YYNN","YYYN","NYYN","NNNY"];
    print(friendCircles(friends))