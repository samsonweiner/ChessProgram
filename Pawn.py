from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight

#pass new positions as a tuple (a, b) where a is horizontal and b is vertical

class Pawn:
    def __init__(self, position, color, board):
        self.pos = position
        self.col = color
        self.id = "Pawn"
        self.move = 0   #hasn't moved, 1 if moved
        self.board = board
        
    def move(self, new_pos):
        #for positions on vertical 2-7 and horizontal 1-8
        if (new_pos[0] < 8 and new_pos[1] < 6):
            #if vertical is 1 more 
            if new_pos[1] == self.pos[1] + 1:
                #if horizontal is the same and new position is empty, move to new_pos
                if new_pos[0] == self.pos[0] and self.board[new_pos[0]][new_pos[1]] == []:
                    print("Pawn from", self.pos, "to", new_pos)
                    self.board[self.pos[0]][self.pos[1]] = []
                    self.board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    self.move = 1
                    return True
                #if horizontal is 1 different and new position is taken by a different color, move to new_pos
                elif new_pos[0] == self.pos[0] - 1 or new_pos[0] == self.pos[0] + 1 and self.board[new_pos[0]][new_pos[1]] != [] and self.board[new_pos[0]][new_pos[1]].col != self.col:
                    print("Pawn from", self.pos, "takes", self.board[new_pos[0]][new_pos[1]].id, "on", new_pos) 
                    self.board[self.pos[0]][self.pos[1]] = []
                    self.board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    self.move = 1
                    return True
                #else illegal move
                else:
                    self.error(new_pos)
            #if horizontal is 2 more, make sure its first move
            if new_pos[1] == self.pos[1] + 2 and self.move == 0:
                #if no pieces occupied in either
                if self.board[new_pos[0]][new_pos[1] - 1] == [] and self.board[new_pos[0]][new_pos[1]]:
                    print("Pawn from", self.pos, "to", new_pos)
                    self.board[self.pos[0]][self.pos[1]] = []
                    self.board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    self.move = 1
                    return True
            else:
                self.error(new_pos)
        #if pawn reaches 8th rank
        elif (new_pos[0] < 8 and new_pos[1] == 7):
            #if vertical is 1 more 
            if new_pos[1] == self.pos[1] + 1:
                #if horizontal is the same and new position is empty, move to new_pos
                if new_pos[0] == self.pos[0] and self.board[new_pos[0]][new_pos[1]] == []:
                    print("Pawn from", self.pos, "to", new_pos)
                    self.board[self.pos[0]][self.pos[1]] = []
                    #need to loop input in case input is an invalid piece
                    while True:
                        piece = raw_input("Type 'Q' for queen, 'R' for rook, 'B' for bishop, or 'K' for knight.\n")
                        if piece == 'Q' or piece == 'R' or piece == 'B' or piece == 'K':
                            break
                        print("Invalid Input.")
                    self.board[new_pos[0]][new_pos[1]] = self.replace_piece(piece, new_pos, self.col)
                    return True
                #if horizontal is 1 different and new position is taken by a different color, move to new_pos
                elif new_pos[0] == self.pos[0] - 1 or new_pos[0] == self.pos[0] + 1 and self.board[new_pos[0]][new_pos[1]] != [] and self.board[new_pos[0]][new_pos[1]].col != self.col:
                    print("Pawn from", self.pos, "takes", self.board[new_pos[0]][new_pos[1]].id, "on", new_pos) 
                    self.board[self.pos[0]][self.pos[1]] = []
                    while True:
                        piece = raw_input("Type 'Q' for queen, 'R' for rook, 'B' for bishop, or 'K' for knight.\n")
                        if piece == 'Q' or piece == 'R' or piece == 'B' or piece == 'K':
                            break
                        print("Invalid Input.")
                    self.board[new_pos[0]][new_pos[1]] = self.replace(piece, new_pos, self.col)
                    return True
                #else illegal move
                else:
                    self.error(new_pos)
            else:
                self.error(new_pos)
        else:
            self.error(new_pos)
        
    
    def replace_piece(self, piece, new_pos, color):
        if piece == 'Q':
            return Queen(new_pos, color)
        if piece == 'R':
            return Rook(new_pos, color)
        if piece == 'B':
            return Bishop(new_pos, color)
        if piece == 'K':
            return Knight(new_pos, color)
                
    def error(self, new_pos):
        print("The new position", new_pos, "is illegal. Please enter a new position.")
        return False
      


