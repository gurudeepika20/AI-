
from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_cost = float("inf")
best_path = None

for p in permutations([1, 2, 3]):
    path = (0,) + p + (0,)
    total = sum(
        cost[path[i]][path[i+1]]
        for i in range(len(path)-1)
    )

    if total < best_cost:
        best_cost = total
        best_path = path

print("Best Path:", best_path)
print("Minimum Cost:", best_cost)




