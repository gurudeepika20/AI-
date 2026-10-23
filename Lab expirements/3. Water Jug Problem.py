
from collections import deque

start = (0, 0)
q = deque([(start, [start])])
visited = {start}

while q:
    (a, b), path = q.popleft()

    if a == 2 or b == 2:
        for s in path:
            print(s)
        print("Goal Reached")
        break

    x = min(a, 3 - b)
    y = min(b, 4 - a)

    states = [
        (4, b), (a, 3), (0, b), (a, 0),
        (a - x, b + x), (a + y, b - y)
    ]

    for s in states:
        if s not in visited:
            visited.add(s)
            q.append((s, path + [s]))
