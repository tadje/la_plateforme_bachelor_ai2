class Solver:
    def __init__(self, board):
        self.board = board
        self.status = []
        for i in range(9):
            temp =[]
            for j in range(9):
                if self.board[i][j] =="_":
                    temp.append(0)
                else:
                    temp.append(1)
            self.status.append(temp)

    #
    def find_empty(self):
        #trouve une case vide 
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == "_":
                    return i, j
        return None

    def is_valid(self, num, pos):
        #verifie que num en valide en pos(ligne, colone)
        for i in range(9):
            if  self.board[pos[0]][i] == num and pos[1] != i:
                return False
        
        for j in range(9):
            if self.board[j][pos[1]] == num and pos[0] != j:
                return False
        

        #verifie le carre
        box_x = pos[0]//3
        box_y = pos[1]//3
        for i in range(box_x*3, box_x*3 + 3):
            for j in range(box_y*3, box_y*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False
        
        return True

    def solve(self):
        #resout le sudoku en utilisant le backtracking
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if self.is_valid(str(i),(row, col)):
                self.board[row][col] = str(i)

                if self.solve():
                    return True
                
                self.board[row][col] = "_"
        return False