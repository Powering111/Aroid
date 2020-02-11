import pygame
from pygame.locals import *
import game
pygame.init()
#def main():
    #while True:

screen= pygame.display.set_mode([1024,720],DOUBLEBUF)
print(game.run('Tutorial_1',screen))

pygame.quit()
