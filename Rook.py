#pass new positions as a tuple (a, b) where a is horizontal and b is vertical

class Rook:
    def __init__(self, position, color):
        self.pos = position
        self.col = color
        self.id = "Rook"

    def move(self, new_pos):
        # new positions are in a valid 8x8 board
        if new_pos[0] < 8 and new_pos[1] < 8:
            # if  new pos is
            if self.pos[0] == new_pos[0] or self.pos[1] == new_pos[1]:
                # make sure no pieces in line of sight
                #if self.piece_inbetween(new_pos):
                    # if spot is empty:
                    if self.board[new_pos[0]][new_pos[1]] == []:
                        print("Rook from", self.pos, "to", new_pos)
                        self.board[self.pos[0]][self.pos[1]] = []
                        self.board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    # if spot is taken by opposing colored piece
                    elif self.board[new_pos[0]][new_pos[1]] != [] and self.board[new_pos[0]][new_pos[1]].col != self.col:
                        print("Rook from", self.pos, "takes", self.board[new_pos[0]][new_pos[1]].id, "on", new_pos)
                        self.board[self.pos[0]][self.pos[1]] = []
                        self.board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    else:
                        self.error(new_pos)
                #else:
                    
                    #print("here")
                    #self.error(new_pos)
            else:
                #print("here")
                self.error(new_pos)
        else:
            #print("here")
            self.error(new_pos)

        # function which checks if there are any pieces in between current pos and new pos

    def piece_inbetween(self, new_pos):
        count = abs(self.pos[1] - new_pos[1]) - 1
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