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
        for x in range(0, len(self.board[row])-2):
            if self.board[row][x]==piece and self.board[row][x+1]==piece:
                if self.board[row][x+2]==piece:
                    return True
        return False

    def winInCol(self, column, piece):
        for i in range(len(self.board)-2):
            if self.board[i][column]==piece and self.board[i+1][column]==piece:
                if self.board[i+2][column]==piece:
                    return True
        return False
        
    def winInDiag(self, piece):
        for x in range(0,len(self.board)-2):
        # Column Length 
            for i in range(0, len(self.board[0])-2):
            # Row Length
                if self.board[x][i]==piece and self.board[x+1][i+1]==piece:
                    if self.board[x+2][i+2]==piece:
                        return True
        for x in range(0,len(self.board)-2):
        # Column Length 
            for i in range(len(self.board[0])-1, 1,-1):
            # Row Length
                if self.board[x][i]==piece and self.board[x+1][i-1]==piece:
                    if self.board[x+2][i-2]==piece:
                        return True     
        return False

    def won(self, piece):
        for row in range(0, len(self.board)):
        # Checking rows
            if self.winInRow(row, piece)==True:
                return True
        for column in range(0, len(self.board)):
            if self.winInCol(column, piece)==True:
                return True
        if self.winInDiag(piece)==True:
            return True
        return False
            
    def hint(self, piece): 
        for x in range(0, len(self.board)):
            for i in range(0, len(self.board[0])):
                if self.board[x][i]==EMPTY:
                    self.board[x][i]=piece
                    if self.won(piece)==True:
                        self.board[x][i]=EMPTY
                        return x , i    
                    else:
                        self.board[x][i]=EMPTY        
        return -1, -1
    
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False
