
from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()

    if state == goal:
        print("Solved in", len(path) - 1, "moves")

        for step_no, step in enumerate(path):
            print("Step", step_no)
            for i in range(0, 9, 3):
                row = step[i:i+3]
                print(" ".join(
                    "_" if x == 0 else str(x) for x in row
                ))
            print()
        break

    z = state.index(0)
    row, col = divmod(z, 3)

    moves = []
    if row > 0:
        moves.append(z - 3)
    if row < 2:
        moves.append(z + 3)
    if col > 0:
        moves.append(z - 1)
    if col < 2:
        moves.append(z + 1)

    for n in moves:
        new_state = list(state)
        new_state[z], new_state[n] = new_state[n], new_state[z]
        new_state = tuple(new_state)

        if new_state not in visited:
            visited.add(new_state)
            q.append((new_state, path + [new_state]))
