#pass new positions as a tuple (a, b) where a is horizontal and b is vertical

class Queen:
    def __init__(self, position, color, board):
        self.pos = position
        self.col = color
        self.id = "Queen"
        self.board = board
    
    def move(self, new_pos):
        #new positions are in a valid 8x8 board
        if new_pos[0] < 8 and new_pos[1] < 8:
            #DIAGONAL
            #if new position on diagonal
            if abs(self.pos[0] - new_pos[0]) == abs(self.pos[1] - new_pos[1]):
                #make sure no pieces in line of sight on diagonal
                if self.diag_piece_inbetween(new_pos):
                    #if spot is empty:
                    if self.board[new_pos[0]][new_pos[1]] == []:
                        print("Queen from", self.pos, "to", new_pos)
                        self.board[self.pos[0]][self.pos[1]] = []
                        self.board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    #if spot is taken by opposing colored piece
                    elif self.board[new_pos[0]][new_pos[1]] != [] and self.board[new_pos[0]][new_pos[1]].col != self.col:
                        print("Queen from", self.pos, "takes", self.board[new_pos[0]][new_pos[1]].id, "on", new_pos)
                        self.board[self.pos[0]][self.pos[1]] = []
                        self.board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    else:
                        self.error(new_pos)
                else:
                    self.error(new_pos)
            #FILE            
            #if new position on same file
            elif self.pos[0] == new_pos[0] or self.pos[1] == new_pos[1] and not abs(self.pos[0] - new_pos[0]) == abs(self.pos[1] - new_pos[1]):
                #make sure no pieces in line of sight on file
                if self.file_piece_inbetween(new_pos):
                    # if spot is empty:
                    if self.board[new_pos[0]][new_pos[1]] == []:
                        print("Queen from", self.pos, "to", new_pos)
                        self.board[self.pos[0]][self.pos[1]] = []
                        self.board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    # if spot is taken by opposing colored piece
                    elif self.board[new_pos[0]][new_pos[1]] != [] and self.board[new_pos[0]][new_pos[1]].col != self.col:
                        print("Queen from", self.pos, "takes", self.board[new_pos[0]][new_pos[1]].id, "on", new_pos)
                        self.board[self.pos[0]][self.pos[1]] = []
                        self.board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    else:
                        self.error(new_pos)
                else:
                    self.error(new_pos)    
            else:
                self.error(new_pos)
        else:
            self.error(new_pos)
    
    
    def diag_piece_inbetween(self, new_pos):
        count = abs(self.pos[0] - new_pos[0]) - 1
        #checking direction
        if self.pos[0] < new_pos[0] and self.pos[1] < new_pos[1]:
        #up and to the right
            for i in range(count):
                if self.board[self.pos[0] + (i + 1)][self.pos[1] + (i + 1)] != []:
                    return False
                return True
        elif self.pos[0] < new_pos[0] and self.pos[1] > new_pos[1]:
        #down and to the right
            for i in range(count):
                if self.board[self.pos[0] + (i + 1)][self.pos[1] - (i + 1)] != []:
                    return False
                return True
        
        elif  self.pos[0] > new_pos[0] and self.pos[1] < new_pos[1]:
        #up and to the left
            for i in range(count):
                if self.board[self.pos[0] - (i + 1)][self.pos[1] + (i + 1)] != []:
                    return False
                return True
        
        elif self.pos[0] > new_pos[0] and self.pos[1] > new_pos[1]:
        #down and to the right
            for i in range(count):
                if self.board[self.pos[0] - (i + 1)][self.pos[1] - (i + 1)] != []:
                    return False
                return True
        else:
        #given new_pos is same spot
            return False


    def file_piece_inbetween(self, new_pos):
        count = abs(self.pos[0] - new_pos[0]) - 1
        # checking direction
        #Moving Right
        if self.pos[0] < new_pos[0]:
            for i in range(count):
                if self.board[self.pos[0] + (i + 1)][self.pos[1]] != []:
                    return False
            return True
        #Moving Left
        elif self.pos[0] > new_pos[0]:
            for i in range(count):
                if self.board[self.pos[0] - (i + 1)][self.pos[1]] != []:
                    return False
            return True
        #Moving Up
        elif self.pos[1] < new_pos[1]:
            for i in range(count):
                if self.board[self.pos[1] + (i + 1)][self.pos[0]] != []:
                    return False
            return True
        #Moving Down
        elif self.pos[1] > new_pos[1]:
            for i in range(count):
                if self.board[self.pos[1] - (i + 1)][self.pos[0]] != []:
                    return False
            return True
        else:
            # given new_pos is same spot
            return False
        
    
    def error(self, new_pos):
        print("The new position", new_pos, "is illegal. Please enter a new position.")
        return False        