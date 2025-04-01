import pygame

from const import *

class Dragger():

    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

        self.piece = None
        self.dragging = False


    def update_mouse(self,position):
        (self.mouseX, self.mouseY) = position

    def save_initial(self,position):
        self.initial_row = position[1]
        self.initial_col = position[0]

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def show_drag(self,surface):

        img = pygame.image.load(self.piece.image)
        self.piece.image_rect = img.get_rect(center = (self.mouseX,self.mouseY)) 
        surface.blit(img, self.piece.image_rect) #affiche l'image

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
