# Water Jug Problem using DFS

def dfs(x, y, visited, path):
    # goal check
    if x == 2 or y == 2:
        path.append((x, y))
        return True

    visited.add((x, y))
    path.append((x, y))

    # possible actions
    moves = []

    moves.append((4, y, "Fill Jug1"))
    moves.append((x, 3, "Fill Jug2"))
    moves.append((0, y, "Empty Jug1"))
    moves.append((x, 0, "Empty Jug2"))

    # pour Jug1 -> Jug2
    pour = min(x, 3 - y)
    moves.append((x - pour, y + pour, "Pour Jug1 -> Jug2"))

    # pour Jug2 -> Jug1
    pour = min(y, 4 - x)
    moves.append((x + pour, y - pour, "Pour Jug2 -> Jug1"))

    for new_x, new_y, action in moves:
        if (new_x, new_y) not in visited:
            print(f"Action: {action} -> State: ({new_x}, {new_y})")
            if dfs(new_x, new_y, visited, path):
                return True

    path.pop()
    return False


visited = set()
path = []

print("Starting DFS...\n")

if dfs(0, 0, visited, path):
    print("\nSolution Path:")
    for state in path:
        print(state)
else:
    print("No solution found")
