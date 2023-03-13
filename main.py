from win32api import GetSystemMetrics
from pygame.locals import *
from pygame import mixer
from mainGame import mainGame
import pygame

pygame.init()

mixer.init()
mixer.music.load('./audio/background.wav')
mixer.music.play(-1)

# icon = pygame.image.load('./img/space-ship.png')
# pygame.display.set_icon(icon)

def mainMenu():
    BGMusic = True
    screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
    backgroundImg = pygame.image.load("./img/background.jpg").convert()
    backgroundImg = pygame.transform.scale(backgroundImg, (GetSystemMetrics(0), GetSystemMetrics(1)))
    font = pygame.font.Font('freesansbold.ttf', 32)              # white
    start_text = font.render('Press SPACE To Enter Game', True, (255, 255, 255))
    start_textRect = start_text.get_rect()
    start_textRect.center = (GetSystemMetrics(0) // 2, (GetSystemMetrics(1)) - 180)

    pygame.display.set_caption("Main Menu!")

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_m:
                    if BGMusic:
                        mixer.music.pause()
                        BGMusic = False
                    else: 
                        mixer.music.unpause()
                        BGMusic = True
                        
                if event.key == K_SPACE:
                    pygame.quit()
                    mainGame()

        screen.blit(backgroundImg, [0, 0])
        screen.blit(start_text, start_textRect)

        pygame.display.update()

if  __name__ == "__main__":
    mainMenu()