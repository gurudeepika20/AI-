
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def safe(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3-m == 0 or 3-m >= 3-c))

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()
    m, c, boat = state

    if state == goal:
        for s in path:
            print(s)
        break

    for x, y in moves:
        if boat == 1:
            nm, nc = m-x, c-y
        else:
            nm, nc = m+x, c+y

        ns = (nm, nc, 1-boat)

        if safe(nm, nc) and safe(3-nm, 3-nc):
            if ns not in visited:
                visited.add(ns)
                q.append((ns, path + [ns]))

