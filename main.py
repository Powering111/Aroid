import pygame
from pygame.locals import *
from pygame.color import Color
from pygame.surface import Surface
from pygame.sprite import Sprite
import sys
import stageselect
pygame.init()
screen= pygame.display.set_mode([1024,720],DOUBLEBUF)
pygame.display.set_caption("Aroid InDev 0.0.3")
pygame.font.init()
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
class Button(Sprite):
    def __init__(self,imgindex1,imgindex2,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.i1,self.i2=imgindex1,imgindex2
        self.image=btnimg[self.i1]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    def update(self,mouse):
        if self.rect.collidepoint(mouse):
            self.image=btnimg[self.i2]
        else:
            self.image=btnimg[self.i1]
    def click(self,mouse):
        global screen
        if self.rect.collidepoint(mouse):
            if self.i1==0:
                stageselect.run(screen)
            elif self.i1==2:
                save()
                pygame.quit()
                sys.exit()
def main():
    global btnimg,mouse
    Terminate=False
    Titleimg=pygame.image.load('images/Title.png').convert_alpha()
    btnimg=[]
    for x in range(4):
        btnimg.append(pygame.image.load('images/btn_'+str(x+1)+'.png').convert_alpha())
    btn1=Button(0,1,420,350)
    btn2=Button(2,3,420,450)
    while not Terminate:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Terminate=True
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                btn1.click(pygame.mouse.get_pos())
                btn2.click(pygame.mouse.get_pos())
        screen.fill(GREEN)
        screen.blit(Titleimg,(230,60))
        btn1.update(pygame.mouse.get_pos())
        btn2.update(pygame.mouse.get_pos())
        btn1.draw()
        btn2.draw()
        pygame.display.flip()
#print(game.run('Tutorial_1',screen))
def save():
    print("saved")
main()
save()
pygame.quit()
sys.exit()
