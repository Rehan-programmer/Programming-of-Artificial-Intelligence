# N-Queens Problem (Dynamic - Backtracking)

def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i] == col:
            return False

    # check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    board = [-1] * n

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                print(f"Placed Queen at row {row}, col {col}")

                if backtrack(row + 1):
                    return True

                print(f"Backtracking from row {row}, col {col}")
                board[row] = -1

        return False

    if backtrack(0):
        return board
    else:
        return None


def print_board(board):
    n = len(board)
    for i in range(n):
        row = ["Q" if board[i] == j else "." for j in range(n)]
        print(" ".join(row))


# dynamic input
n = int(input("Enter value of N: "))

solution = solve_n_queens(n)

if solution:
    print("\nSolution Found:\n")
    print_board(solution)
else:
    print("No solution exists")
