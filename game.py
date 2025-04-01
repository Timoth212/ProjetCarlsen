import pygame  # type: ignore

from const import *
from board import Board
from dragger import Dragger

class Game():

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    def show_background(self, surface):
        '''
        Méthode pour créer les cases de l'échiquier graphique

        input: 
            -surface : la taille de la fenetre à remplir 

        output:
            -Creation des cases de l'échiquier
        '''
        for row in range(rows):
            for col in range (cols):
                if (row + col)%2 == 0:
                    color=(234,235,200) 
                else:
                    color=(119,154,88)
                
                square = (col*square_size,row*square_size,square_size,square_size)
                pygame.draw.rect(surface,color,square)
                          
    def show_pieces(self,surface):
        for row in range(rows):
            for col in range (cols):

                if self.board.squares[row][col].has_piece(): #Il y a t-il une piece sur la case? Si oui je l'affiche
                    piece = self.board.squares[row][col].piece
                    
                    if piece != self.dragger.piece:
                        img = pygame.image.load(piece.image) #je charge l'image de la piece
                        img_center = col*square_size + square_size//2, row*square_size + square_size//2
                        piece.image_rect = img.get_rect(center = img_center) # je centre l'image sur le centre de la case occupée
                    
                        surface.blit(img, piece.image_rect) #affiche l'image
    