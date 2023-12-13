import random
import math
import numpy as np

def initial_solution(board):
    for i in range(9):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for j in range(9):
            if board[i][j] == 0:
                for num in numbers:
                    if num not in board[i]:
                        board[i][j] = num
                        break
    return board

def compute_violations(board):
    violations = 0
    for i in range(9):
        row_violations = 9 - len(set(board[i]))
        col_violations = 9 - len(set(board[j][i] for j in range(9)))
        violations += row_violations + col_violations

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            block_violations = 9 - len(set(block))
            violations += block_violations

    return violations

def simulated_annealing(board):
    temperature = 1.0
    cooling_rate = 0.99
    current_solution = initial_solution(board.copy())
    current_violations = compute_violations(current_solution)

    while temperature > 0.01:
        new_solution = current_solution.copy()
        row = random.randint(0, 8)
        col1, col2 = random.sample(range(9), 2)
        new_solution[row][col1], new_solution[row][col2] = new_solution[row][col2], new_solution[row][col1]

        new_violations = compute_violations(new_solution)
        if new_violations < current_violations or random.random() < math.exp((current_violations - new_violations) / temperature):
            current_solution = new_solution
            current_violations = new_violations

        temperature *= cooling_rate

    return current_solution

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_board = simulated_annealing(board)
for row in solved_board:
    print(row)
