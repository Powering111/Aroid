import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.color import Color
import queue

def init():
    global BLACK,WHITE,BLUE,GREEN,RED,size,screen,clock,arrowgroup,arrowimg,playerimg,font,backgroundColor,ongroundColor,levelName,levelAuthor,levelDifficulty,levelTime,level,gameEnd,nowTick,nextTick,nowEvent
    # Initialize the game engine
    pygame.init()
    pygame.font.init()
    BLACK= ( 0,  0,  0)
    WHITE= (255,255,255)
    BLUE = ( 0,  0,255)
    GREEN= ( 0,255,  0)
    RED  = (255,  0,  0)

    # make variables
    size  = [1024,720]
    screen= pygame.display.set_mode(size,DOUBLEBUF)
    pygame.display.set_caption("Aroid 1.0.0")
    clock = pygame.time.Clock()
    #load
    arrowgroup = pygame.sprite.Group()
    arrowimg=[]
    for x in range(2):
        arrowimg.append(pygame.image.load('images/arrow_'+str(x+1)+'.png').convert_alpha())
    playerimg=[]
    for x in range(4):
        playerimg.append(pygame.image.load('images/player_'+str(x+1)+'.png'))
    # Initialize
    font=pygame.font.Font('./NanumGothic.ttf',30)
    backgroundColor=WHITE
    ongroundColor=BLACK
    levelName="Level"
    levelAuthor="Troll"
    levelDifficulty=1
    levelTime=0
    level=queue.Queue()
    nowTick=0
    gameEnd=-1
    nowEvent=queue.Queue()
def loadLevel(levelfilename):
    global levelName,levelAuthor,levelDifficulty,levelTime,level
    #level load
    lvl = open("levels/"+levelfilename+"/level",'r')
    levelName = lvl.readline()
    levelAuthor=lvl.readline()
    levelDifficulty=int(lvl.readline())
    levelTime = int(lvl.readline())
    #level load
    for nowsec in range(levelTime): # as 1 second
        oneline=lvl.readline().strip().split()# 1 line
        for x in range(len(oneline)):
            level.put(int(oneline[x]))
    lvl.close()
def levelEvent():
    global level,player,backgroundColor,ongroundColor
    # 1 tick
    if level.empty():
        return
    event=level.get()
    for e in range(event):# 1 event
        eventType=level.get()
        if eventType==1:
            ak=level.get()
            bk=level.get()
            ck=level.get()
            backgroundColor=(ak,bk,ck)
            ongroundColor=(255-ak,255-bk,255-ck)
        elif eventType==2:
            arrowType=level.get()
            arrowPos=level.get()
            arrowSpeed=level.get()
            newarrow(arrowPos,arrowSpeed,arrowType)
        elif eventType==3:
            t=level.get()
            if t==1:
                player.mode=level.get()
            elif t==2:
                player.Damage(level.get())
            elif t==3:
                player.SH=level.get()
            elif t==4:
                player.DEF+=level.get()
            elif t==5:
                player.DEF=level.get()
            elif t==6:
                player.IDEF+=level.get()
            elif t==7:
                player.IDEF=level.get()
            elif t==8:
                player.HP+=level.get()
            elif t==9:
                player.HP=level.get()
            elif t==10:
                player.SPEED+=level.get()
            elif t==11:
                player.SPEED=level.get()
            elif t==12:
                player.MHP+=level.get()
            elif t==13:
                player.MHP=level.get()
    if player.SPEED>200:
        player.SPEED=200
    elif player.SPEED<20:
        player.SPEED=20
    player.speed=int((player.SPEED*15)/100)
    if player.HP>player.MHP:
        player.HP=player.MHP
    if player.DEF>3:
        player.DEF=3
    if player.SH>1:
        player.SH=1
    if player.HP<=0:
        player.HP=0
def rotate(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect
class Player(Sprite):#(212,60),(812,660)
    def __init__(self):
        Sprite.__init__(self)
        self.sprite_width=64
        self.sprite_height=64
        self.mode=0
        self.image = playerimg[self.mode]
        self.image.blit(self.image,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x=480
        self.rect.y=328
        self.moveDown=False
        self.moveUp=False
        self.moveLeft=False
        self.moveRight=False
        self.speed=15
        self.SPEED=100
        self.HP=10
        self.MHP=10
        self.DEF=0
        self.SH=0
        self.IDEF=0
    def update(self):
        global arrowgroup
        
        #move variable
        if self.moveDown ==True and self.rect.y < 592:
            if self.moveLeft==True or self.moveRight==True:
                self.rect.y=self.rect.y+int(self.speed*0.7)
            else:
                self.rect.y=self.rect.y+int(self.speed)
        if self.moveUp==True and self.rect.y > 60:
            if self.moveLeft==True or self.moveRight==True:
                self.rect.y=self.rect.y-int(self.speed*0.7)
            else:
                self.rect.y=self.rect.y-int(self.speed)
        if self.moveLeft ==True and self.rect.x > 212:
            if self.moveUp==True or self.moveDown==True:
                self.rect.x = self.rect.x-int(self.speed*0.7)
            else:
                self.rect.x = self.rect.x-int(self.speed)
        if self.moveRight==True and self.rect.x < 744:
            if self.moveUp==True or self.moveDown==True:
                self.rect.x=self.rect.x+int(self.speed*0.7)
            else:
                self.rect.x=self.rect.x+int(self.speed)
        #Fix out of Field
        if self.rect.y> 592:
            self.rect.y=592
        if self.rect.y<60:
            self.rect.y=60
        if self.rect.x<212:
            self.rect.x=212
        if self.rect.x>744:
            self.rect.x=744
        for ar in arrowgroup:
            if self.rect.colliderect(ar.rect):
                #TODO make things
                m=ar.mode
                if m==0:
                    self.damage(2)
                elif m==1:
                    self.damage(2)
                    self.MHP+=1
                ar.kill()
                del ar
    def damage(self,d):
        if self.SH==1:
            self.SH=0
            return
        if self.DEF<d:
            d-=self.DEF
            self.DEF=0
        else:
            DEF-=d
            d=0
        self.HP-=d
        return
    def draw():
        screen.blit(self.image,[self.rect.x,self.rect.y])
class Arrow(Sprite):
    def __init__(self,pos,speed,mode):
        Sprite.__init__(self)
        self.sprite_width=31
        self.sprite_height=64
        self.speed=speed
        self.mode=mode
        self.image = arrowimg[self.mode]
        self.image.set_colorkey([255,0,255])
        self.image.blit(self.image,(0,0))
        self.rect = self.image.get_rect()
        self.pos=pos
        if (self.pos>=0 and self.pos<100):
            self.image,self.rect=rotate(self.image,self.rect,180)
            self.rect.x=pos*6+212
            self.rect.y=-4
        elif (self.pos>=100 and self.pos<200):
            self.rect.x=812
            self.rect.y=60+(pos-100)*6
            self.image,self.rect=rotate(self.image,self.rect,90)
        elif (self.pos>=200 and self.pos<300):
            self.rect.x=812-(pos-200)*6
            self.rect.y=660
        elif (self.pos>=300 and self.pos<400):
            self.rect.x=212-64
            self.rect.y=660-(pos-300)*6
            self.image,self.rect=rotate(self.image,self.rect,270)
    def update(self):
        global player
        if self.pos>=0 and self.pos<100:
            self.rect.y=self.rect.y + self.speed
        elif self.pos>=100 and self.pos<200:
            self.rect.x = self.rect.x - self.speed
        elif self.pos>=200 and self.pos<300:
            self.rect.y=self.rect.y-self.speed
        elif self.pos>=300 and self.pos<400:
            self.rect.x=self.rect.x+self.speed
        if (self.rect.y >= 660 and (self.pos>=0 and self.pos<100)) or (self.rect.x<=212 and(self.pos>=100 and self.pos<200)) or (self.rect.y<=60 and (self.pos>=200 and self.pos<300)) or (self.rect.x>=812 and(self.pos>=300 and self.pos<400)):
            #TODO Event when Purple and pink and gray arrow
            self.kill()
            del self
    def draw():
        screen.blit(self.image,[self.rect.x,self.rect.y])

def newarrow(pos,speed,mode):
    global arrowgroup
    ar = Arrow(pos,speed,mode)
    arrowgroup.add(ar)
def rungame(lvlname):
    
    global player_mode,player,nowTick,gameEnd
    
    loadLevel(lvlname)
    #init
    finishGame= False
    player = Player()
    playergroup=pygame.sprite.Group()
    playergroup.add(player)
    nextTick=0
    while not finishGame:
        #set 60FPS
        clock.tick(60)
        #event get
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finishGame=True
            #WASD key input
            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    player.moveUp=True
                if event.key ==pygame.K_s:
                    player.moveDown=True
                if event.key ==pygame.K_a:
                    player.moveLeft=True
                if event.key ==pygame.K_d:
                    player.moveRight=True
            if event.type ==pygame.KEYUP:
                if event.key==pygame.K_w:
                    player.moveUp=False
                if event.key ==pygame.K_s:
                    player.moveDown=False
                if event.key ==pygame.K_a:
                    player.moveLeft=False
                if event.key ==pygame.K_d:
                    player.moveRight=False
        #update
        
        player.update()
        for ar in arrowgroup:
            ar.update()

        # events
        if nextTick==0: #once per tick
            if gameEnd==-1:
                levelEvent()
            if player.HP==0 and gameEnd==-1: # game over
                arrowgroup.empty()
                gameEnd=10
            if nowTick==levelTime and gameEnd==-1: # level clear
                gameEnd=20
            if gameEnd==0:
                return int((float(nowTick)/float(levelTime)*float(100)))
            elif gameEnd>0:
                gameEnd-=1
            elif gameEnd == -1:
                nowTick+=1 # Now time (tick)
            nextTick=6 # Frames before next tick
        nextTick-=1
        screen.fill(backgroundColor)
        
        #draw after here
        hpText=font.render('HP'+str(player.HP),False,(0,0,0))
        screen.blit(hpText,(100,0))
        arrowgroup.draw(screen)
        playergroup.draw(screen)
        
        pygame.draw.rect(screen,ongroundColor,[212,60,600,600],5)

        #draw before here
        pygame.display.flip()
def run(lvn):
    init()
    return rungame(lvn)
