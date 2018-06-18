from Default_Board import *

board = generate_board()


#pass new positions as a tuple (a, b) where a is horizontal and b is vertical

class Pawn:
    def __init__(self, position, color):
        self.pos = position
        self.col = color
        self.id = "Pawn"
        
    def move(self, new_pos):
        #for positions on vertical 2-7 and horizontal 1-8
        if (new_pos[0] < 7 and new_pos[1] < 6):
            #if vertical is 1 more 
            if new_pos[1] == self.pos[1] + 1:
                #if horizontal is the same and new position is empty, move to new_pos
                if new_pos[0] == self.pos[0] and board[new_pos[0]][new_pos[1]] == []:
                    print("Pawn from", self.pos, "to", new_pos)
                    board[self.pos[0]][self.pos[1]] = []
                    board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    return True
                #if horizontal is 1 different and new position is taken by a different color, move to new_pos
                elif new_pos[0] == self.pos[0] - 1 or new_pos[0] == self.pos[0] + 1 and board[new_pos[0]][new_pos[1]] != [] and board[new_pos[0]][new_pos[1]].col != self.col:
                    print("Pawn from", self.pos, "takes", board[new_pos[0]][new_pos[1]].id, "on", new_pos) 
                    board[self.pos[0]][self.pos[1]] = []
                    board[new_pos[0]][new_pos[1]] = self
                    self.pos = new_pos
                    return True
                #else illegal move
                else:
                    self.error(new_pos)
            else:
                self.error(new_pos)
        else:
		self.error(new_pos)
        #if pawn reaches 8th rank
    
    
    
    
            
            
    def error(self, new_pos):
        print("The new position", new_pos, "is illegal. Please enter a new position.")
        return False
      


s1 = Pawn((0, 1), "white")
s2 = Pawn((1, 3), "black")

board[0][1] = s1
board[1][3] = s2

print(s1.pos)

s1.move((0, 2))

print(s1.pos, board[0][2])

s1.move((1, 3))
