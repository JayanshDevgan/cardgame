from win32api import GetSystemMetrics
from pygame import mixer
from cards import Cards, cards_rect_list, characterSet, animename_List
from Details import Details
import mainGame
import pygame
import random

class Game:
    pygame.init()

    def __init__(self):
        pass

    def Start():
        mixer.init()
        mixer.music.load('./audio/background.wav')
        mixer.music.play(-1)

        BGMusic = True

        screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
        pygame.display.set_caption("Game Name")
        display_surface = pygame.display.get_surface()

        maingamebackground = pygame.image.load("./img/maingamebackgroundimg.png").convert()
        maingamebackground = pygame.transform.scale(maingamebackground, (GetSystemMetrics(0), GetSystemMetrics(1)))
        # PLAYER
        cardsBackFace = pygame.image.load('./img/cards/cardsBackFace.png').convert()
        cardsBackFace = pygame.transform.scale(cardsBackFace, (200, 250))
    
        cardsBackFaceList = [cardsBackFace] * 6

        rects = [pygame.Rect(180 + i * (20 + cardsBackFace.get_width()), 700, 200, 250) for i, _ in enumerate(range(6))]

        # AI
        cardsBackFaceAI = pygame.image.load('./img/cards/cardsBackFace.png').convert()
        cardsBackFaceAI = pygame.transform.scale(cardsBackFaceAI, (200, 250))

        cardsBackFaceAIList = [cardsBackFaceAI] * 6
        
        AIrects = [pygame.Rect(180 + i * (20 + cardsBackFace.get_width()), 200, 200, 250) for i, _ in enumerate(range(6))]

        random.seed()

        card_indices = []

        for anime_id, anime in characterSet.items():
            characters = anime["characters"]
            for j in range(len(characters)):
                card_indices.append((anime_id, j))

        random.shuffle(card_indices)

        cards = [True] * 6
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    mousePosition = pygame.mouse.get_pos()
                    for i, rect in enumerate(rects):
                        if cards[i] and rect.collidepoint(mousePosition):
                            j, k = card_indices.pop()
                            cardsBackFaceList[i] = pygame.image.load(characterSet[str(j)]["characters"][str(k)]["card"]).convert()
                            cardsBackFaceList[i] = pygame.transform.scale(cardsBackFaceList[i], (200, 250))
                            cards[i] = False
                    
                selected_card = None
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(rects):
                        if rect.collidepoint(mouse_pos) and not cards[i]:
                            if selected_card == i:
                                selected_card = None
                                pygame.draw.rect(screen, (0, 0, 0), rect, 2)
                            else:
                                if selected_card is not None:
                                    pygame.draw.rect(screen, (0, 0, 0), rects[selected_card], 2)
                                selected_card = i
                                while True:
                                    pygame.draw.rect(screen, (255, 0, 0), rect, 3)
                                    pygame.display.update()
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                                            mouse_pos = pygame.mouse.get_pos()
                                            for j, r in enumerate(rects):
                                                if r.collidepoint(mouse_pos) and not cards[j]:
                                                    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
                                                    selected_card = None
                                                    break
                                            else:
                                                continue
                                            break
                                    else:
                                        continue
                                    break
                            pygame.display.update()
                            break

                # Redraw the selected card border (if any)
                if selected_card is not None:
                    pygame.draw.rect(screen, (255, 0, 0), rects[selected_card], 3)
                pygame.display.update()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if BGMusic:
                            mixer.music.pause()
                            BGMusic = False
                        else:
                            mixer.music.unpause()
                            BGMusic = True

            # PLAYER CARDS
            screen.blit(maingamebackground, [0, 0])
            for i in range(6):
                screen.blit(cardsBackFaceList[i], rects[i])

            for i, rect in zip(range(6), AIrects):
                screen.blit(cardsBackFaceAIList[i], rect)
            pygame.display.update()  

    def Locker():
        pygame.quit()
        mixer.init()
        mixer.music.load('./audio/background.wav')
        mixer.music.play(-1)

        BGMusic = True

        screen = pygame.display.set_mode((GetSystemMetrics(0), GetSystemMetrics(1)))
        pygame.display.set_caption("Locker")

        lockerbackgroundImg = pygame.image.load("./img/lockerbackgroundimg.jpg").convert()
        lockerbackgroundImg = pygame.transform.scale(lockerbackgroundImg, (GetSystemMetrics(0), GetSystemMetrics(1)))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Set the x, y positions of the mouse click
                    x, y = event.pos
                    # Check if any card rectangle collides with the mouse click position
                    for i, rect in enumerate(cards_rect_list):
                        if rect.collidepoint(x, y):
                            details = Details()
                            details.render(str(animename_List[i]))
                    
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
                        mainGame.run_game()

            screen.blit(lockerbackgroundImg, [0, 0])
            Cards.render(screen)

            pygame.display.update()
