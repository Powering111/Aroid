import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.color import Color


def run():
    pygame.init()
    size = (400, 300)
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption("Simple Test")
 
    run = True
    clock = pygame.time.Clock()
    img=pygame.image.load('images/arrow_1.png').convert_alpha()
    # 게임 루프
    while run:
        # 사용자 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # 게임 상태 그리기
        screen.fill((100,255,255))
        screen.blit(img,(100,100))
        pygame.display.flip()
 
        clock.tick(60)
        
    pygame.quit()
run()
