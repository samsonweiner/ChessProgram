#pass new positions as a tuple (a, b) where a is horizontal and b is vertical
global board


class Knight:
    def __init__(self, position, color):
        self.pos = position
        self.col = color
        self.id = "Knight"
        
    def move(self, new_pos):
        #new positions are in a valid 8x8 board
        if new_pos[0] < 8 and new_pos[1] < 8:
            #absolute value of difference of hor/ver are 2 and 1. Either way works.
            if (abs(new_pos[0] - self.pos[0]) == 2 and abs(new_pos[0] - self.pos[0]) == 1) or (abs(new_pos[0] - self.pos[0]) == 1 and abs(new_pos[1] - self.pos[1]) == 2):
                #if spot is empty:
                if board[new_pos[0]][new_pos[1]] == []:
                    print("Knight from", self.pos, "to", new_pos)
                    board[self.pos[0]][self.pos[1]] = []
                    board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    return True
                #if spot is taken by opposing colored piece
                elif board[new_pos[0]][new_pos[1]] != [] and board[new_pos[0]][new_pos[1]].col != self.col:
                    print("Knight from", self.pos, "takes", board[new_pos[0]][new_pos[1]].id, "on", new_pos)
                    board[self.pos[0]][self.pos[1]] = []
                    board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    return True
                else:
                    self.error(new_pos)
            else:
                self.error(new_pos)       
        else:
            self.error(new_pos)
                
    def error(self, new_pos):
        print("The new position", new_pos, "is illegal. Please enter a new position.")
        return False
        