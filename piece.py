import os

class Piece:

    def __init__(self, name,  color, value,row = 0, col= 0, image=None, image_rect=None):
        self.name=name
        self.color=color

        self.image = image
        self.image_rect = image_rect
        self.set_image()

        self.moves=[]
        self.moved = False

    def set_image(self):
        '''
        Methode pour donner l'image correspondante à la piece
        '''
        self.image = os.path.join(f'images/{self.color}_{self.name}.png')

    def update_position(self,position):
        self.row,self.col = position

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__('pawn',color, 1.0)
    
    def possible_moves(self,board):
        self.moves = []
        directions = [(self.row+self.dir, self.col)]
        if self.moved == False: 
            directions.append((self.row+2*self.dir, self.col))
        if self.col+1 <8 and board.squares[self.row+self.dir][self.col+1].piece != None :
            self.moves.append((self.row+self.dir,self.col+1))
        if self.col-1 >=0  and board.squares[self.row+self.dir][self.col-1].piece != None :
            self.moves.append((self.row+self.dir,self.col-1))

        for direction in directions : 
            if 0 <= direction[0] <= 7 and 0 <= direction[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[direction[0]][direction[1]].piece == None:  # Si la case est vide, déplacement autorisé
                        self.moves.append(direction)

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight',color, 3.0)
    
    def possible_moves(self,board):
        self.moves = []
        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        
        for direction in directions:
                move = (self.row + direction[0], self.col + direction[1])
                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[move[0]][move[1]].piece is None:  # Si la case est vide, déplacement autorisé
                        self.moves.append(move)
                    else:
                        if board.squares[move[0]][move[1]].piece.color != self.color:  # Si une pièce adverse est présente, on peut la capturer
                            self.moves.append(move)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop',color, 3.0)

    def possible_moves(self,board):
        self.moves = []
        directions = [(-1,-1),(-1,1),(1,-1),(1,1)]


        for direction in directions:
            for i in range(1, 8):  # Déplacement jusqu'à 7 cases max
                move = (self.row + direction[0] * i, self.col + direction[1] * i)

                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[move[0]][move[1]].piece is None:  # Si la case est vide, déplacement autorisé
                        self.moves.append(move)
                    else:
                        if board.squares[move[0]][move[1]].piece.color != self.color:  # Si une pièce adverse est présente, on peut la capturer
                            self.moves.append(move)
                        break  # Dans tous les cas, on arrête ici (car obstacle)

                else:
                    break  # Stoppe la boucle si on sort de l'échiquier

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook',color, 5.0)

    def possible_moves(self,board):
        self.moves = []
        directions = [(-1,0),(0,-1),(1,0),(0,1)]


        for direction in directions:
            for i in range(1, 8):  # Déplacement jusqu'à 7 cases max
                move = (self.row + direction[0] * i, self.col + direction[1] * i)

                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[move[0]][move[1]].piece is None:  # Si la case est vide, déplacement autorisé
                        self.moves.append(move)
                    else:
                        if board.squares[move[0]][move[1]].piece.color != self.color:  # Si une pièce adverse est présente, on peut la capturer
                            self.moves.append(move)
                        break  # Dans tous les cas, on arrête ici (car obstacle)

                else:
                    break  # Stoppe la boucle si on sort de l'échiquier

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen',color, 9.0)

    def possible_moves(self,board):
        self.moves = []
        directions = [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(0,-1),(1,0),(0,1)]


        for direction in directions:
            for i in range(1, 8):  # Déplacement jusqu'à 7 cases max
                move = (self.row + direction[0] * i, self.col + direction[1] * i)

                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[move[0]][move[1]].piece is None:  # Si la case est vide, déplacement autorisé
                        self.moves.append(move)
                    else:
                        if board.squares[move[0]][move[1]].piece.color != self.color:  # Si une pièce adverse est présente, on peut la capturer
                            self.moves.append(move)
                        break  # Dans tous les cas, on arrête ici (car obstacle)

                else:
                    break  # Stoppe la boucle si on sort de l'échiquier

class King(Piece):

    def __init__(self, color):
        self.ischeck = False
        super().__init__('king',color, 100000.0)

    def possible_moves(self,board):
        self.moves = []
        directions = [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(0,-1),(1,0),(0,1)]

        #Roques possibles
        if self.moved == False and self.ischeck == False:
            
            #côté droit
            if board.squares[self.row][7].piece != None and board.squares[self.row][7].piece.moved == False:
                
                ennemy_possible_next_moves = board.ennemy_possible_next_moves(self.color)
                king_path = [(self.row,6),(self.row,5)]

                if not (set(ennemy_possible_next_moves) & set(king_path)): ###marche pas encore
                    directions.append((0,2))

            #côté gauche
            if board.squares[self.row][0].piece != None and board.squares[self.row][0].piece.moved == False:
                ennemy_possible_next_moves = board.ennemy_possible_next_moves(self.color)
                king_path = [(self.row,2),(self.row,3)]                  

                if not (set(ennemy_possible_next_moves) & set(king_path)) :
                    directions.append((0,-2))

        for direction in directions:
                move = (self.row + direction[0], self.col + direction[1])
                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[move[0]][move[1]].piece is None:  # Si la case est vide, déplacement autorisé
                        self.moves.append(move)
                    else:
                        if board.squares[move[0]][move[1]].piece.color != self.color:  # Si une pièce adverse est présente, on peut la capturer
                            self.moves.append(move)

        