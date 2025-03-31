import pygame  # type: ignore
import sys

from const import *
from game import Game

class Main():


    def __init__(self):
        self.game=Game()

        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Chess")


    def mainloop(self):
        
        while True:
            self.game.show_background(self.screen)
            self.game.show_pieces(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()



main=Main()
main.mainloop()


