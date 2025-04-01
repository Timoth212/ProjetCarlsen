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

        sel_piece = None
        
        while True:

            # Affichage principal
            game.show_background(screen)  # Redessine l'échiquier
            game.show_pieces(screen)  # Redessine toutes les pièces

            # Si une pièce est en cours de déplacement, on l'affiche par-dessus
            if dragger.dragging:
                dragger.show_drag(screen)
            
            for event in pygame.event.get():
                  
                #click
                if event.type == pygame.MOUSEBUTTONDOWN :
                    ##Calcule la position de la case
                    dragger.update_mouse(event.pos)
                    clicked_row = int(dragger.mouseY // square_size)
                    clicked_col = int(dragger.mouseX // square_size)
                    
                    #s'il y a une piece sur la case

                    if dragger.piece != None and event.button == 3 : # Si une piece à déjà été séléctionnée
                        print('test')
                        ###On indique la nouvelle position de la piece à l'échiquier
                        board.new_piece_position(dragger.piece, [dragger.initial_row,dragger.initial_col], [clicked_row,clicked_col]) 

                        dragger.undrag_piece()
                        
                    elif board.squares[clicked_row][clicked_col].has_piece() and event.button == 1:

                        dragger.save_initial((clicked_row, clicked_col)) #On sauvegarde la position initiale
                        dragger.drag_piece(board.squares[clicked_row][clicked_col].piece) #On indique que la piece séléctionnée est en mouvement

                    


                #Souris en mouvement 
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)


                # dé-click
                elif event.type == pygame.MOUSEBUTTONUP:
                    ###Calcule la position de la case
                    dragger.update_mouse(event.pos)
                    declicked_row = int(dragger.mouseY // square_size)
                    declicked_col = int(dragger.mouseX // square_size)

                    if dragger.dragging and (declicked_row,declicked_col) != (dragger.initial_col,dragger.initial_row):
                        ###On indique la nouvelle position de la piece à l'échiquier
                        board.new_piece_position(dragger.piece, [dragger.initial_row,dragger.initial_col], [declicked_row,declicked_col]) 
                        dragger.undrag_piece()


                #Quitter
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()



main=Main()
main.mainloop()


