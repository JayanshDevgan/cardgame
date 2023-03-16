import os
import pygame
from pygame import mixer
from win32api import GetSystemMetrics

import Game


class Details:
    def __init__(self):
        pygame.init()
        mixer.init()
        mixer.music.load(os.path.join("audio", "background.wav"))
        mixer.music.play(-1)
        self.BGMusic = True
        self.screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
        pygame.display.set_caption("Details")

    def render(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if self.BGMusic:
                            mixer.music.pause()
                            self.BGMusic = False
                        else:
                            mixer.music.unpause()
                            self.BGMusic = True

                    if event.key in (pygame.K_BACKSPACE, pygame.K_ESCAPE):
                        pygame.quit()
                        Game.Game.Locker()

            pygame.display.update()
