from win32api import GetSystemMetrics
from pygame import mixer
import pygame
import Game

class Details:
    def __init__(self):
        return self
    
    def Render():
        pygame.quit()
        pygame.init()
        mixer.init()
        mixer.music.load('./audio/background.wav')
        mixer.music.play(-1)

        BGMusic = True

        screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
        pygame.display.set_caption("Details")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if BGMusic:
                            mixer.music.pause()
                            BGMusic = False
                        else: 
                            mixer.music.unpause()
                            BGMusic = True

                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            Game.Game.Locker()

            pygame.display.update()