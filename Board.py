#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:
    def __init__(self):
        self.board = None
                    
    def full(self):
        return False
            
    def won(self, piece):
        return False
            
    def hint(self, piece):             
        return -1, -1
    
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False
