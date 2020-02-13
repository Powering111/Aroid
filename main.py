import pygame
from pygame.locals import *
from pygame.color import Color
from pygame.surface import Surface
from pygame.sprite import Sprite
import sys
import os
import stageselect
from stageselect import stages
pygame.init()
screen= pygame.display.set_mode([1024,720],DOUBLEBUF)
pygame.display.set_caption("Aroid InDev 0.0.4")
pygame.display.set_icon(pygame.image.load('images/icon.png'))
pygame.font.init()
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
def save():
    global money,stagePercent
    print("====SAVE====")
    file = open(os.environ["appdata"]+"\\Aroid\\save","w")
    file.write("SAVEFILE Indev 0.0.4a\n")
    file.write(str(money)+"\n")
    for x in range(9):
        data=""
        print(stageselect.stages[x])
        for y in range(stageselect.stages[x]):
            data+=str(stagePercent[x][y])
            data+=" "
        print("saved value : "+str(data))
        file.write(data+"\n")
    file.close()
    print("====saved====")
def load():
    global money,stagePercent
    print("====LOAD====")
    if not os.path.exists(os.environ["appdata"]+"\\Aroid"):#no folder
        print("Directory Not Exists. Made Directory.")
        os.mkdir(os.environ["appdata"]+"\\Aroid")
    if not os.path.isfile(os.environ["appdata"]+"\\Aroid\\save"):#no file
        print("File not exists. Making File")
        money=0
        stagePercent=[]
        for x in range(9):
            dat=[]
            for y in range(stageselect.stages[x]):
                dat.append(0)
            stagePercent.append(dat)
        save()
    else:  #yes file
        print("Loading File..")
        stagePercent=[]
        file = open(os.environ["appdata"]+"\\Aroid\\save","r")
        fileVer=str(file.readline()).strip()
        print("File Version : "+fileVer)
        if(fileVer=="SAVEFILE Indev 0.0.4a"):#file version check
            money=int(str(file.readline()).strip())
            for x in range(9):
                data=[]
                dat=str(file.readline()).strip().split()
                for y in range(stageselect.stages[x]):
                    data.append(int(dat[y]))
                stagePercent.append(data)
        else:
            print("File not valid")
            sys.exit()
        file.close()
        print("====loaded====")
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
    def click(self,mouse): #On click of button
        global screen,money,stagePercent
        if self.rect.collidepoint(mouse):
            if self.i1==0:
                
                m,sp,s1,s2=stageselect.run(screen,money,stagePercent)
                if not m==-1:
                    if m==100 and stagePercent[s1][s2]!=100:
                        money+=sp
                    if stagePercent[s1][s2]<m:
                        stagePercent[s1][s2]=m
                
                save()
            elif self.i1==2:
                save()
                pygame.quit()
                sys.exit()
def main():
    global btnimg,mouse
    for x in range(9): 
        print("Loaded:",stagePercent[x])
    Terminate=False
    Titleimg=pygame.image.load('images/Title.png').convert_alpha()
    btnimg=[]
    ddddfont=pygame.font.Font('./NanumGothic.ttf',25)
    moneyimg=pygame.image.load('images/money.png').convert_alpha()
    
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
        btn1.update(pygame.mouse.get_pos())
        btn2.update(pygame.mouse.get_pos())
        screen.fill(GREEN)
        moneytext=ddddfont.render(str(money),True,(0,0,0))
        screen.blit(Titleimg,(230,60))
        screen.blit(moneyimg,(10,10))
        screen.blit(moneytext,(50,10))
        
        btn1.draw()
        btn2.draw()
        pygame.display.flip()
load()
main()
save()
pygame.quit()
sys.exit()
