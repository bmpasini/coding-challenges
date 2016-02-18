from math import factorial as fact

n, i = (int(i) for i in input().strip().split(' '))
groups = list()
for _ in range(i):
    a, b = (int(i) for i in input().strip().split(' '))
    new = True
    for group in groups:
        if a in group or b in group:
            group.add(a)
            group.add(b)
            new = False
            break
    if new:
        group = set()
        group.add(a)
        group.add(b)
        groups.append(group)

if n == 1:
    total = 1
else:    
    total = fact(n) / (fact(2) * fact(n-2))
    for group in groups:
        ng = len(group)
        total -= fact(ng) / (fact(2) * fact(ng-2))

print(int(total))