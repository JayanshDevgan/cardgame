# from win32api import GetSystemMetrics
# from pygame import mixer
# from Game import Game
# import pygame

# def mainGame():
#     pygame.init()
#     mixer.init()
#     mixer.music.load('./audio/background.wav')
#     mixer.music.play(-1)

#     BGMusic = True
#     clock = pygame.time.Clock()
#     fps = 60

#     font = pygame.font.Font('freesansbold.ttf', 32)              # white
#     about_text1 = font.render('Press ENTER To Start Game', True, (255, 255, 255))
#     about_text2 = font.render('Press BACKSPACE or ESC To Exit Game', True, (255, 255, 255))
#     about_text3 = font.render('Press L To Check Locker', True, (255, 255, 255))

#     about1_textRect = about_text1.get_rect()
#     about1_textRect.center = (GetSystemMetrics(0) // 2, (GetSystemMetrics(1)) - 280)
#     about2_textRect = about_text2.get_rect()
#     about2_textRect.center = (GetSystemMetrics(0) // 2, (GetSystemMetrics(1)) - 180)
#     about3_textRect = about_text3.get_rect()
#     about3_textRect.center = (GetSystemMetrics(0) // 2, (GetSystemMetrics(1)) - 230)

#     screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
#     pygame.display.set_caption("No name for now!")

#     backgroundArenaImg = pygame.image.load("./img/backgroundarenaimg.jpg").convert()
#     backgroundArenaImg = pygame.transform.scale(backgroundArenaImg, (GetSystemMetrics(0), GetSystemMetrics(1)))

#     # game loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_m:
#                     if BGMusic:
#                         mixer.music.pause()
#                         BGMusic = False
#                     else: 
#                         mixer.music.unpause()
#                         BGMusic = True
#                 if event.key == pygame.K_RETURN:
#                     Game.Start()
#                 if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                 if event.key == pygame.K_l:
#                     Game.Locker()

#         screen.blit(backgroundArenaImg, [0, 0])
#         screen.blit(about_text1, about1_textRect)
#         screen.blit(about_text2, about2_textRect)
#         screen.blit(about_text3, about3_textRect)
#         pygame.display.update()
#         clock.tick(fps)


from win32api import GetSystemMetrics
from pygame import mixer
from Game import Game
import pygame

def run_game():
    # Initialize pygame and mixer
    pygame.init()
    mixer.init()
    
    # Load and play background music
    mixer.music.load('./audio/background.wav')
    mixer.music.play(-1)

    # Set up game loop variables
    clock = pygame.time.Clock()
    fps = 60
    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("No name for now!")
    
    # Set up text variables
    font_size = 32
    font = pygame.font.Font('freesansbold.ttf', font_size)
    about_text1 = font.render('Press ENTER To Start Game', True, (255, 255, 255))
    about_text2 = font.render('Press BACKSPACE or ESC To Exit Game', True, (255, 255, 255))
    about_text3 = font.render('Press L To Check Locker', True, (255, 255, 255))
    about1_text_rect = about_text1.get_rect()
    about1_text_rect.center = (screen_size[0] // 2, screen_size[1] - 280)
    about2_text_rect = about_text2.get_rect()
    about2_text_rect.center = (screen_size[0] // 2, screen_size[1] - 180)
    about3_text_rect = about_text3.get_rect()
    about3_text_rect.center = (screen_size[0] // 2, screen_size[1] - 230)
    
    # Set up background image
    background_img = pygame.image.load("./img/backgroundarenaimg.jpg").convert()
    background_img = pygame.transform.scale(background_img, screen_size)

    # Set up game loop
    bg_music_enabled = True
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    bg_music_enabled = not bg_music_enabled
                    if bg_music_enabled:
                        mixer.music.unpause()
                    else:
                        mixer.music.pause()
                if event.key == pygame.K_RETURN:
                    Game.Start()
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_l:
                   Game.Locker()

        screen.blit(background_img, [0, 0])
        screen.blit(about_text1, about1_text_rect)
        screen.blit(about_text2, about2_text_rect)
        screen.blit(about_text3, about3_text_rect)
        pygame.display.update()
        clock.tick(fps)
