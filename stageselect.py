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
stages=[2,2,2,2,2,2,2,2,2]
giveMoney=[10,100,500,1000,1500,2000,3000,5000,10000]
stage_name=[['Tutorial_1','Tutorial_2'],['Nakji-1','Nakji-2'],['easy-1','easy-2'],['medium-1','medium-2'],['hard-1','hard-2'],['insane-1','insane-2'],['extreme-1','super extreme'],['chaos-1','chaos0035'],['hidden-1','HIDDEN!!']]
def endGame(percent):
    global screen
    Terminate=False
    font=pygame.font.Font('./NanumGothic.ttf',60)
    font2=pygame.font.Font('./NanumGothic.ttf',30)
    text=None
    if percent == 100:
        text=font.render("큭큭 재미없다.깨서",True,(0,255,0))
    else:
        text=font.render("냥...죽었냥",True,(255,255,255))
    while not Terminate:
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                Terminate=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                Terminate=True
        if percent==100:
            screen.fill(WHITE)
            
        else:
            screen.fill(BLACK)
        screen.blit(text,(300,300))
        screen.blit(font2.render("ESC를 눌러 돌아가기",True,(255,255,0)),(10,10))
        pygame.display.flip()
    return percent
def stage(a):
    global screen
    Terminate=False
    font=pygame.font.Font('./NanumGothic.ttf',40)
    txt=font.render(packs[a-1],True,(0,0,0))
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
                            return endGame(game.run(stage_name[a][i],screen)),i
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
    txt1=font1.render('히히 제일 어려운 걸로 ㅋㅋ',True,(0,0,0))
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
