import pygame
from pygame.sprite import Sprite
import game
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
pygame.font.init()
stage_name=[]
infofile=open('./levels/info','r')
packs=infofile.readline().strip().split()
giveMoney=list(map(int,infofile.readline().strip().split()))
stages=list(map(int,infofile.readline().strip().split()))
for x in range(len(packs)):
    stage_name.append(infofile.readline().strip().split())
stage_name
def stage(a):
    global screen
    Terminate=False
    font=pygame.font.Font('./NanumGothic.ttf',40)
    txt=font.render(packs[a],True,(0,0,0))
    font2=pygame.font.Font('./NanumGothic.ttf',20)
    txt2=font2.render('ESC를 눌러 돌아가기',True,(0,0,0))
    while not Terminate:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                kk=True
                for i in range(stages[a]):
                    if kk==True:
                        if pygame.Rect(10,100*i+100,1000,80).collidepoint(pygame.mouse.get_pos()):
                            pygame.mixer.music.stop()
                            return game.run(stage_name[a][i],screen),i
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                return -1,-1
        screen.fill(GREEN)
        screen.blit(txt,(10,20))
        for i in range(stages[a]):
            pygame.draw.rect(screen,WHITE,[10,100*i+100,1000,80])
            pygame.draw.rect(screen,(255,255,0),[10,100*i+100,10*stagePercent[a][i],80])
            text=font.render(stage_name[a][i],True,(0,0,0))
            text2=None
            if stagePercent[a][i]==100:
                text2=font.render(str(stagePercent[a][i])+"%",True,GREEN)
            else:    
                text2=font.render(str(stagePercent[a][i])+"%",True,(0,0,0))
            screen.blit(text,(20,100*i+115))
            screen.blit(text2,(900,100*i+115))
        screen.blit(txt2,(830,680))
        pygame.display.flip()
class Btn(Sprite):# Pack select button
    def __init__(self,val):
        self.val=val
        self.image=btnimg[self.val]
        self.rect=self.image.get_rect()
    def click(self,mouse):       # on click of pack
        if self.rect.collidepoint(mouse): # clicked
            s,t=stage(self.val)
            if t==-1:
                return -1,-1
            else:
                return s,t
        else:# not clicked
            return -2,-2
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
def setpos(a,x,y):
    a.rect.x=x
    a.rect.y=y
def run(scr,m,sp):
    global btnimg,screen,money,stagePercent
    # background music
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.load('sounds/simple.wav')
    pygame.mixer.music.play(-1)
    money=m
    stagePercent=sp
    for x in range(9):
        for y in range(stages[x]):
            print("x"+str(x)+"  y:"+str(y)+"  h  "+str(stagePercent[x][y]))
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
    txt1=font1.render('맵 팩 선택',True,(0,0,0))
    txt2=font2.render('Esc를 눌러 돌아가기',True,(0,0,0))
    Terminate=False
    while not Terminate:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Terminate=True
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                kk=True
                for x in range(9):
                    if kk==True:
                        a,nn=btn[x].click(pygame.mouse.get_pos())
                        if a==-1:
                            kk=False
                        elif a>=0:
                            return a,giveMoney[x],x,nn
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                Terminate=True
        screen.fill(BLUE)
        for x in range(9):
            btn[x].draw(screen)
        screen.blit(txt1,(100,10))
        screen.blit(txt2,(830,680))
        pygame.display.flip()
    return -1,-1,-1,-1
