#pass new positions as a tuple (a, b) where a is horizontal and b is vertical
global board

class Rook:
    def __init__(self, position, color):
        self.pos = position
        self.col = color
        self.id = "Rook"

    def move(self, new_pos):
        # new positions are in a valid 8x8 board
        if new_pos[0] < 8 and new_pos[1] < 8:
            # if  new pos is
            if new_pos[0] == new_pos[0] or new_pos[1] == new_pos[1]:
                # make sure no pieces in line of sight
                if self.piece_inbetween(new_pos):
                    # if spot is empty:
                    if board[new_pos[0]][new_pos[1]] == []:
                        print("Rook from", self.pos, "to", new_pos)
                        board[self.pos[0]][self.pos[1]] = []
                        board[new_pos[0]][new_pos[1]] = self
                        self.pos = new_pos
                        return True
                    # if spot is taken by opposing colored piece
                    elif board[new_pos[0]][new_pos[1]] != [] and board[new_pos[0]][new_pos[1]].col != self.col:
                        print("Rook from", self.pos, "takes", board[new_pos[0]][new_pos[1]].id, "on", new_pos)
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
        else:
            self.error(new_pos)

        # function which checks if there are any pieces in between current pos and new pos

    def piece_inbetween(self, new_pos):
        count = abs(self.pos[0] - new_pos[0]) - 1
        # checking direction
        if self.pos[0] < new_pos[0] and self.pos[1] < new_pos[1]:
            # up and to the right
            for i in range(count):
                if board[self.pos[0] + (i + 1)][self.pos[1] + (i + 1)] != []:
                    return False
                return True
        elif self.pos[0] < new_pos[0] and self.pos[1] > new_pos[1]:
            # down and to the right
            for i in range(count):
                if board[self.pos[0] + (i + 1)][self.pos[1] - (i + 1)] != []:
                    return False
                return True

        elif self.pos[0] > new_pos[0] and self.pos[1] < new_pos[1]:
            # up and to the left
            for i in range(count):
                if board[self.pos[0] - (i + 1)][self.pos[1] + (i + 1)] != []:
                    return False
                return True

        elif self.pos[0] > new_pos[0] and self.pos[1] > new_pos[1]:
            # down and to the right
            for i in range(count):
                if board[self.pos[0] - (i + 1)][self.pos[1] - (i + 1)] != []:
                    return False
                return True
        else:
            # given new_pos is same spot
            return False

    def error(self, new_pos):
        print("The new position", new_pos, "is illegal. Please enter a new position.")
        return False