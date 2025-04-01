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
        self.initial_row = int(position[1]//square_size)
        self.initial_col = int(position[0]//square_size)

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True