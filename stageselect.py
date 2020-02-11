import pygame
from pygame.sprite import Sprite
import game
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
pygame.font.init()
packs=['TUTORIAL','NAKG','EASY','MEDIUM','HARD','INSANE','EXTREME','CHAOS','HIDDEN']
stages=[2,0,0,0,0,0,0,0,0]
stage_name=[['Tutorial_1','Tutorial_2'],[],[],[],[],[],[],[],[]]
def stage(a):
    global screen
    Terminate=False
    font=pygame.font.Font('./NanumGothic.ttf',40)
    txt=font.render(packs[a-1],True,(0,0,0))
    font2=pygame.font.Font('./NanumGothic.ttf',20)
    txt2=font2.render('ESC to go back',True,(0,0,0))
    while not Terminate:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                kk=True
                for i in range(stages[a-1]):
                    if kk==True:
                        if pygame.Rect(10,100*i+100,1000,80).collidepoint(pygame.mouse.get_pos()):
                            game.run(stage_name[a-1][i],screen)
                            kk=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                return
        screen.fill(GREEN)
        screen.blit(txt,(10,20))
        for i in range(stages[a-1]):
            pygame.draw.rect(screen,WHITE,[10,100*i+100,1000,80])
            text=font.render(stage_name[a-1][i],True,(0,0,0))
            screen.blit(text,(20,100*i+115))
        screen.blit(txt2,(830,680))
        pygame.display.flip()
class Btn(Sprite):
    def __init__(self,val):
        self.val=val+1  #val is 1~9
        self.image=btnimg[self.val-1]
        self.rect=self.image.get_rect()
    def click(self,mouse):
        if self.rect.collidepoint(mouse):
            stage(self.val)
            return True
        else:
            return False
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
def setpos(a,x,y):
    a.rect.x=x
    a.rect.y=y
def run(scr):
    global btnimg,screen
    screen=scr
    print('hi')
    btnimg=[]
    btn=[] # index is 0~8
    for x in range(9):
        btnimg.append(pygame.image.load('images/pack_'+str(x+1)+'.png').convert_alpha())
        btn.append(Btn(x))
    oa=200
    ob=80
    setpos(btn[0],10+oa,10+ob)
    setpos(btn[1],220+oa,10+ob)
    setpos(btn[2],430+oa,10+ob)
    setpos(btn[3],10+oa,220+ob)
    setpos(btn[4],220+oa,220+ob)
    setpos(btn[5],430+oa,220+ob)
    setpos(btn[6],10+oa,430+ob)
    setpos(btn[7],220+oa,430+ob)
    setpos(btn[8],430+oa,430+ob)
    screen.fill(WHITE)
    font1=pygame.font.Font('./NanumGothic.ttf',40)
    font2=pygame.font.Font('./NanumGothic.ttf',20)
    txt1=font1.render('SELECT MAP PACK',True,(0,0,0))
    txt2=font2.render('ESC to go back',True,(0,0,0))
    Terminate=False
    while not Terminate:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Terminate=True
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                kk=True
                for x in range(9):
                    if kk==True:
                        if btn[x].click(pygame.mouse.get_pos()):
                            kk=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                Terminate=True
        screen.fill(BLUE)
        for x in range(9):
            btn[x].draw(screen)
        screen.blit(txt1,(100,10))
        screen.blit(txt2,(830,680))
        pygame.display.flip()
