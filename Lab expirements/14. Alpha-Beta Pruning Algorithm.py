
def alphabeta(depth, node, alpha, beta,
              maximizing, values):
    if depth == 2:
        return values[node]

    if maximizing:
        best = float("-inf")
        for i in range(2):
            val = alphabeta(
                depth+1, node*2+i, alpha, beta,
                False, values
            )
            best = max(best, val)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best

    else:
        best = float("inf")
        for i in range(2):
            val = alphabeta(
                depth+1, node*2+i, alpha, beta,
                True, values
            )
            best = min(best, val)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best

values = [3, 5, 2, 9]
print("Best Value:", alphabeta(
    0, 0, float("-inf"), float("inf"),
    True, values
))



