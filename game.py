import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.color import Color
# Initialize the game engine
pygame.init()
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
 
# make variables
size  = [1024,720]
screen= pygame.display.set_mode(size,DOUBLEBUF)
# Initialize
pygame.display.set_caption("Aroid 1.0.0")
arrowgroup = pygame.sprite.Group()
arrowimg=[]
for x in range(2):
    arrowimg.append(pygame.image.load('images/arrow_'+str(x+1)+'.png').convert_alpha())
#Loop until the user clicks the close button.
playerimg=[]
for x in range(4):
    playerimg.append(pygame.image.load('images/player_'+str(x+1)+'.png'))
clock = pygame.time.Clock()
player_mode = 1
player_x=512
player_y=360
speed = 15
def rotate(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect
class Player(Sprite):#(212,60),(812,660)
    def __init__(self):
        Sprite.__init__(self)
        self.sprite_image='images/player_1.png'
        self.sprite_width=64
        self.sprite_height=64
        self.image = pygame.image.load(self.sprite_image).convert_alpha()
        self.image.blit(self.image,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x=480
        self.rect.y=328
        self.moveDown=False
        self.moveUp=False
        self.moveLeft=False
        self.moveRight=False
    def update(self):
        global arrowgroup
        #move variable
        if self.moveDown ==True and self.rect.y < 592:
            if self.moveLeft==True or self.moveRight==True:
                self.rect.y=self.rect.y+int(speed*0.7)
            else:
                self.rect.y=self.rect.y+speed
        if self.moveUp==True and self.rect.y > 60:
            if self.moveLeft==True or self.moveRight==True:
                self.rect.y=self.rect.y-int(speed*0.7)
            else:
                self.rect.y=self.rect.y-speed
        if self.moveLeft ==True and self.rect.x > 212:
            if self.moveUp==True or self.moveDown==True:
                self.rect.x = self.rect.x-int(speed*0.7)
            else:
                self.rect.x = self.rect.x-speed
        if self.moveRight==True and self.rect.x < 744:
            if self.moveUp==True or self.moveDown==True:
                self.rect.x=self.rect.x+int(speed*0.7)
            else:
                self.rect.x=self.rect.x+speed
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
                ar.kill()
                del ar
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
            #TODO something
            self.kill()
            del self
    def draw():
        screen.blit(self.image,[self.rect.x,self.rect.y])

def newarrow(pos,speed,mode):
    global arrowgroup
    ar = Arrow(pos,speed,mode)
    arrowgroup.add(ar)
def rungame(lvlname):
    global player_mode,player
    #level load
    #lvl = open("levels/"+lvlname,'r')
    #level_name = lvl.readline()
    #level_time = int(lvl.readline())
    #lvl.close()

    #init
    finishGame= False
    player = Player()
    playergroup=pygame.sprite.Group()
    playergroup.add(player)
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
                if event.key ==pygame.K_1:
                    newarrow(50,10,0)
                if event.key ==pygame.K_2:
                    newarrow(150,10,0)
                if event.key ==pygame.K_3:
                    newarrow(250,10,0)
                if event.key ==pygame.K_4:
                    newarrow(350,10,0)
        #update
        player.update()
        for ar in arrowgroup:
            ar.update()
        screen.fill(WHITE)

        #draw after here
        
        arrowgroup.draw(screen)
        playergroup.draw(screen)
        pygame.draw.rect(screen,RED,[player.rect.x,player.rect.y,64,64],3)
        pygame.draw.rect(screen,BLACK,[212,60,600,600],5)

        #draw before here
        pygame.display.flip()

rungame("1")
pygame.quit()
