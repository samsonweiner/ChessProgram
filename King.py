#pass new positions as a tuple (a, b) where a is horizontal and b is vertical

class King:
    def __init__(self, position, color, board):
        self.pos = position
        self.col = color
        self.id = "King"
        self.board = board

    def move(self, new_pos):
        #new positions are in a valid 8x8 board
        if new_pos[0] < 8 and new_pos[1] < 8:
            #hor and ver both less than 1
            if abs(self.pos[0] - new_pos[0]) <= 1 and abs(self.pos[1] - new_pos[1]) <= 1:
                #if spot is empty:
                if self.board[new_pos[0]][new_pos[1]] == []:
                    print("King from", self.pos, "to", new_pos)
                    self.board[self.pos[0]][self.pos[1]] = []
                    self.board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    return True
                #if spot is taken by opposing colored piece
                elif self.board[new_pos[0]][new_pos[1]] != [] and self.board[new_pos[0]][new_pos[1]].col != self.col:
                    print("King from", self.pos, "takes", self.board[new_pos[0]][new_pos[1]].id, "on", new_pos)
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

    def error(self, new_pos):
        print("The new position", new_pos, "is illegal. Please enter a new position.")
        return False