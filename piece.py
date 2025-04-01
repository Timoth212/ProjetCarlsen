import os

class Piece:

    def __init__(self, name, color, value, image=None, image_rect=None):
        self.name=name
        self.color=color

        value_sign = 1 if color == "white" else -1
        self.value=value*value_sign

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

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__('pawn',color, 1.0)
    
    def possible_moves(self,dragger,board):
        self.moves = []
        self.moves =[(dragger.initial_row+self.dir, dragger.initial_col)]

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight',color, 3.0)
    
    def possible_moves(self,dragger,board):
        self.moves = []
        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        
        for direction in directions:
            move = dragger.initial_row + direction[0],dragger.initial_col + direction[1]
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                self.moves.append(move)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop',color, 3.0)

    def possible_moves(self,dragger,board):
        self.moves = []
        directions = [(-1,-1),(-1,1),(1,-1),(1,1)]

        moves_théoriques = []

        for direction in directions:
            for i in range(1, 8):  # Déplacement jusqu'à 7 cases max
                move = (dragger.initial_row + direction[0] * i, dragger.initial_col + direction[1] * i)

                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:  # Vérifie qu'on reste dans l'échiquier

                    if board.squares[move[0]][move[1]].piece is None:  # Si la case est vide, déplacement autorisé
                        moves_théoriques.append(move)
                    else:
                        if board.squares[move[0]][move[1]].piece.color != dragger.piece.color:  # Si une pièce adverse est présente, on peut la capturer
                            moves_théoriques.append(move)
                        break  # Dans tous les cas, on arrête ici (car obstacle)

                else:
                    break  # Stoppe la boucle si on sort de l'échiquier

        self.moves = moves_théoriques


        
        




class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook',color, 5.0)

    def possible_moves(self):
        moves =[]
        return moves

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen',color, 9.0)

    def possible_moves(self):
        moves =[]
        return moves

class King(Piece):

    def __init__(self, color):
        super().__init__('king',color, 100000.0)

    def possible_moves(self):
        moves =[]
        return moves
