from resolve_sudoku import Solver

def print_board(solver):
    for i in range(9):
        for j in range(9):
            if solver.status[i][j] == 1:
                print(board[i][j], end="")
            else:
                print("\033[31m"+board[i][j]+"\033[0m", end="")
        print()

if __name__ == "__main__":
    board = []
    with open('sudoku.txt','r') as file:
        for line in file:
            row = list(line.strip())
            board.append(row)
    solver = Solver(board)
    
    if solver.solve():
        print("sudoku resolu")
        print_board(solver)
    else:
        print("pas de solution ")
