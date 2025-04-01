import pygame  # type: ignore
import sys

from const import *
from game import Game
from dragger import Dragger

class Main():

    def __init__(self):
        self.game=Game()

        pygame.init()
        self.screen = pygame.display.set_mode((width,height)) #Ouvre une fenetre
        pygame.display.set_caption("Chess") #Donne un titre à la fenetre

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        
        while True:
            game.show_background(screen) #Affiche l'échiquier
            game.show_pieces(screen) #Affiche les pieces

            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = int(dragger.mouseY // square_size)
                    clicked_col = int(dragger.mouseX // square_size)

                    #if clicked square has piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece

                #mouvement de souris
                elif event.type == pygame.MOUSEMOTION:
                    pass

                # dé-click
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass

                #Quitter
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()



main=Main()
main.mainloop()


