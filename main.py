import pygame
import os

WIDTH, HEIGHT = 900,500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("My Game")

WHITE=(255,255,255)

FPS=60  

SHIP_WIDTH, SHIP_HEIGHT = 55,40


YELLOW_SHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SHIP =pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP_IMAGE,(SHIP_WIDTH, SHIP_HEIGHT)),90)

RED_SHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SHIP =pygame.transform.rotate(pygame.transform.scale(RED_SHIP_IMAGE,(SHIP_WIDTH, SHIP_HEIGHT)),270)

def open_window(red,yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SHIP,(red.x,red.y))
    pygame.display.update()


def main():

    red=pygame.Rect(100,300,SHIP_WIDTH,SHIP_HEIGHT)
    yellow=pygame.Rect(700,300,SHIP_WIDTH,SHIP_HEIGHT)

    clock =pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        yellow.x+=1
        open_window(red,yellow)

        
    pygame.quit()

if __name__ =="__main__":
    main()