#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:
    def __init__(self, rows=3, columns=3):
        self.board = []
        for i in range(0, rows):
            colum=[]
            for i in range (0, columns):
                colum.append(EMPTY)
            self.board.append(colum)
    
    def canPlay(self, row, column):
        if self.board[row][column]==EMPTY:
            return True
        else:
            return False
    
    def play(self, row, column, piece):
        self.board[row][column]=piece

    def cols(self):
        return len(self.board[0])

    def rows(self):
        return len(self.board)
                    
    def full(self):
        for x in range(0,len(self.board)):
            for i in self.board[x]:
                if i==EMPTY:
                    return False
        return True
            
    def winInRow(self, row, piece):
        for x in self.board[row]:
            if x[i]==piece and x[i+1]==piece:
                if x[i+2]==piece:
                    return True

    def winInCol(self, column, piece):
        for i in range(len(self.board)):
            for x in self.board:
                if x[i]==piece and x[i+1]==piece:
                    if x[i+2]==piece:
                        return True

    def won(self, piece):
        return False
            
    def hint(self, piece):             
        return -1, -1
    
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False
