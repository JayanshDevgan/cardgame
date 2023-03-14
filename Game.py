from win32api import GetSystemMetrics
from pygame import mixer
from cards import Cards, cardsRectList, characterSet
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

        # rect1 = pygame.Rect(180, 700, 200, 250)
        # rect2 = pygame.Rect(200 + cardsBackFace.get_width(), 700, 200, 250)
        # rect3 = pygame.Rect(420 + cardsBackFace.get_width(), 700, 200, 250)
        # rect4 = pygame.Rect(640 + cardsBackFace.get_width(), 700, 200, 250)
        # rect5 = pygame.Rect(860 + cardsBackFace.get_width(), 700, 200, 250)
        # rect6 = pygame.Rect(1080 + cardsBackFace.get_width(), 700, 200, 250)

        # AI
        cardsBackFaceAI = pygame.image.load('./img/cards/cardsBackFace.png').convert()
        cardsBackFaceAI = pygame.transform.scale(cardsBackFaceAI, (200, 250))

        cardsBackFaceAIList = [cardsBackFaceAI] * 6
        
        AIrects = [pygame.Rect(180 + i * (20 + cardsBackFace.get_width()), 200, 200, 250) for i, _ in enumerate(range(6))]

        random.seed()

        # NoOfAnime = len(characterSet)
        # if NoOfAnime == 0:
        #     card_indices = [(i, j) for i in range(NoOfAnime) for j in range(len(characterSet["0"]["characters"]))]
        # elif NoOfAnime == 1:
        #     card_indices = [(i, j) for i in range(NoOfAnime) for j in range(len(characterSet["1"]["characters"]))]
        # else:
        #     card_indices = [(i, j) for i in range(NoOfAnime) for j in range(len(characterSet["2"]["characters"]))]

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePosition = pygame.mouse.get_pos()
                    for i, rect in enumerate(rects):
                        if cards[i] and rect.collidepoint(mousePosition):
                            j, k = card_indices.pop()
                            cardsBackFaceList[i] = pygame.image.load(characterSet[str(j)]["characters"][str(k)]["card"]).convert()
                            cardsBackFaceList[i] = pygame.transform.scale(cardsBackFaceList[i], (200, 250))
                            cards[i] = False
                    # if a:
                    #     if rect1.collidepoint(mousePosition):
                    #         i, j = card_indices.pop()
                    #         cardsBackFace1 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                    #         cardsBackFace1 = pygame.transform.scale(cardsBackFace1, (200, 250))
                    #         a = 0
                    # if b:
                    #     if rect2.collidepoint(mousePosition):
                    #         i, j = card_indices.pop()
                    #         cardsBackFace2 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                    #         cardsBackFace2 = pygame.transform.scale(cardsBackFace2, (200, 250))
                    #         b = 0
                    # if c:
                    #     if rect3.collidepoint(mousePosition):
                    #         i, j = card_indices.pop()
                    #         cardsBackFace3 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                    #         cardsBackFace3 = pygame.transform.scale(cardsBackFace3, (200, 250))
                    #         c = 0
                    # if d:
                    #     if rect4.collidepoint(mousePosition):
                    #         i, j = card_indices.pop()
                    #         cardsBackFace4 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                    #         cardsBackFace4 = pygame.transform.scale(cardsBackFace4, (200, 250))
                    #         d = 0
                    # if e:
                    #     if rect5.collidepoint(mousePosition):
                    #         i, j = card_indices.pop()
                    #         cardsBackFace5 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                    #         cardsBackFace5 = pygame.transform.scale(cardsBackFace5, (200, 250))
                    #         e = 0
                    # if f:
                    #     if rect6.collidepoint(mousePosition):
                    #         i, j = card_indices.pop()
                    #         cardsBackFace6 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                    #         cardsBackFace6 = pygame.transform.scale(cardsBackFace6, (200, 250))
                    #         f = 0
                    if all(var == False for var in cards):
                        for _ in range(6):
                            if cardsBackFaceAIList[_] != 0:
                                i, j = card_indices.pop()
                                cardsBackFaceAIList[_] = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"]).convert()
                                cardsBackFaceAIList[_] = pygame.transform.scale(cardsBackFaceAIList[_], (200, 250))


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
            # screen.blit(cardsBackFace1, rect1)
            # screen.blit(cardsBackFace2, rect2)
            # screen.blit(cardsBackFace3, rect3)
            # screen.blit(cardsBackFace4, rect4)
            # screen.blit(cardsBackFace5, rect5)
            # screen.blit(cardsBackFace6, rect6)
            # AI CARDS
            # screen.blit(cardsBackFaceAI, AIrects)
            # screen.blit(cardsBackFaceAI, AIrect2)
            # screen.blit(cardsBackFaceAI, AIrect3)
            # screen.blit(cardsBackFaceAI, AIrect4)
            # screen.blit(cardsBackFaceAI, AIrect5)
            # screen.blit(cardsBackFaceAI, AIrect6)
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
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    if any(rect.collidepoint(x, y) for rect in cardsRectList):
                        Details.Render()
                
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
                        mainGame.mainGame()

            screen.blit(lockerbackgroundImg, [0, 0])
            Cards.Render(screen)

            pygame.display.update()
