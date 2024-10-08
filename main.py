from win32api import GetSystemMetrics
import pygame
from pygame.locals import *
from pygame import mixer
from mainGame import run_game

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
BACKGROUND_IMAGE_PATH = "./img/background.jpg"
START_TEXT_FONT_SIZE = 32
START_TEXT_COLOR = (255, 255, 255)
START_TEXT = "Press SPACE To Enter Game"

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Main Menu!")
        self.background_img = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE_PATH).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font('freesansbold.ttf', START_TEXT_FONT_SIZE)
        self.start_text = self.font.render(START_TEXT, True, START_TEXT_COLOR)
        self.start_text_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 180))
        self.bg_music = mixer.music
        self.bg_music.load('./audio/background.wav')
        self.is_bg_music_playing = False
        
    def play_bg_music(self):
        self.bg_music.play(-1)
        self.is_bg_music_playing = True

    def pause_bg_music(self):
        self.bg_music.pause()
        self.is_bg_music_playing = False
        
    def toggle_bg_music(self):
        if self.is_bg_music_playing:
            self.pause_bg_music()
        else:
            self.play_bg_music()
        
    def handle_input(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_m:
                self.toggle_bg_music()
            elif event.key == K_SPACE:
                pygame.quit()
                run_game()
                
    def run(self):
        self.play_bg_music()
        while True:
            for event in pygame.event.get():
                self.handle_input(event)
            
            self.screen.blit(self.background_img, [0, 0])
            self.screen.blit(self.start_text, self.start_text_rect)
            pygame.display.update()

if __name__ == "__main__":
    MainMenu().run()
