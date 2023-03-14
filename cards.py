import pygame

characterSet = {
    "0": {
        "animename": "Naruto",
        "tposY": 20,
        "posY": 80,
        "characters": {
            "0": { 
                "card": "./img/cards/naruto/naruto-1.png",
                "id": 0,
                "name": "naruto",
                "posX": 10,
                "A": 60,
                "D": 80,
                "S": 78
            },
            "1": {
                "card": "./img/cards/naruto/sasuke-1.png",
                "id": 1,
                "name": "sasuke",
                "posX": 25,
                "A": 80,
                "D": 55,
                "S": 90
            },
            "2": {
                "card": "./img/cards/naruto/kakashi-1.png",
                "id": 2,
                "name": "kakashi",
                "posX": 210,
                "A": 80,
                "D": 50,
                "S": 80
            },
            "3": {
                "card": "./img/cards/naruto/sakura-1.png",
                "id": 3,
                "name": "sakura",
                "posX": 395,
                "A": 65,
                "D": 60,
                "S": 52
            },
            "4": {
                "card": "./img/cards/naruto/orochimaru-1.png",
                "id": 4,
                "name": "orochimaru",
                "posX": 580,
                "A": 80,
                "D": 90,
                "S": 72
            },
            "5": {
                "card": "./img/cards/naruto/itachi-1.png",
                "id": 5,
                "name": "itachi",
                "posX": 765,
                "A": 75,
                "D": 90,
                "S": 75
            },
            "6": {
                "card": "./img/cards/naruto/rocklee-1.png",
                "id": 6,
                "name": "rocklee",
                "posX": 950,
                "A": 80,
                "D": 60,
                "S": 100
            },
            "7": {
                "card": "./img/cards/naruto/madara-1.png",
                "id": 7,
                "name": "madara",
                "posX": 1135,
                "A": 92,
                "D": 70,
                "S": 90
            },
            "8": {
                "card": "./img/cards/naruto/tenten-1.png",
                "id": 8,
                "name": "tenten",
                "posX": 1320,
                "A": 65,
                "D": 45,
                "S": 35
            },
        }
    },
    "1": {
        "animename": "Hunter Hunter",
        "tposY": 320,
        "posY": 380,
        "characters": {
            "0": {
                "card": "./img/cards/hunterXhunter/GonFreecss-1.png",
                "id": 9,
                "name": "Gon Freecss",
                "posX": 10,
                "A": 85,
                "D": 90,
                "S": 70
            },
            "1": {
                "card": "./img/cards/hunterXhunter/hisoka-1.png",
                "id": 10,
                "name": "hisoka",
                "posX": 25,
                "A": 100,
                "D": 80,
                "S": 90
            },
            "2": {
                "card": "./img/cards/hunterXhunter/killuazoldyck-1.png",
                "id": 11,
                "name": "killua zoldyck",
                "posX": 210,
                "A": 95,
                "D": 90,
                "S": 100
            },
            "3": {
                "card": "./img/cards/hunterXhunter/leorio-1.png",
                "id": 12,
                "name": "leorio",
                "posX": 395,
                "A": 15,
                "D": 70,
                "S": 80
            },
            "4": {
                "card": "./img/cards/hunterXhunter/kurapika-1.png",
                "id": 13,
                "name": "kurapika",
                "posX": 580,
                "A": 45,
                "D": 80,
                "S": 80
            },
            "5": {
                "card": "./img/cards/hunterXhunter/biscuitkrueger-1.png",
                "id": 14,
                "name": "biscuit krueger",
                "posX": 765,
                "A": 92,
                "D": 80,
                "S": 70
            },
            "6": {
                "card": "./img/cards/hunterXhunter/IllumiZoldyck-1.png",
                "id": 15,
                "name": "Illumi Zoldyck",
                "posX": 950,
                "A": 85,
                "D": 80,
                "S": 80
            },
        }
    },
    "2": {
        "animename": "Demon Slayer",
        "tposY": 620,
        "posY": 680,
        "characters": {
            "0": {
                "card": "./img/cards/Demon Slayer/TanjiroKamado-1.png",
                "id": 16,
                "name": "Tanjiro Kamado",
                "posX": 10,
                "A": 80,
                "D": 80,
                "S": 70
            },
            "1": {
                "card": "./img/cards/Demon Slayer/NezukoKamado-1.png",
                "id": 17,
                "name": "Nezuko Kamado",
                "posX": 25,
                "A": 80,
                "D": 90,
                "S": 70
            },
            "2": {
                "card": "./img/cards/Demon Slayer/ZenitsuAgatsuma-1.png",
                "id": 18,
                "name": "Zenitsu Agatsuma",
                "posX": 210,
                "A": 90,
                "D": 60,
                "S": 90
            },
            "3": {
                "card": "./img/cards/Demon Slayer/GiyuTomioka-1.png",
                "id": 19,
                "name": "Giyu Tomioka",
                "posX": 395,
                "A": 92,
                "D": 80,
                "S": 70
            },
            "4": {
                "card": "./img/cards/Demon Slayer/InosukeHashibira-1.png",
                "id": 20,
                "name": "Inosuke Hashibira",
                "posX": 580,
                "A": 80,
                "D": 80,
                "S": 75
            },
            "5": {
                "card": "./img/cards/Demon Slayer/SakonjiUrokodaki-1.png",
                "id": 21,
                "name": "Sakonji Urokodaki",
                "posX": 765,
                "A": 100,
                "D": 80,
                "S": 80
            },
            "6": {
                "card": "./img/cards/Demon Slayer/Makomo-1.png",
                "id": 22,
                "name": "Makomo",
                "posX": 950,
                "A": 10,
                "D": 10,
                "S": 10
            },
            "7": {
                "card": "./img/cards/Demon Slayer/Sabito-1.png",
                "id": 23,
                "name": "Sabito",
                "posX": 1135,
                "A": 100,
                "D": 80,
                "S": 90
            },
        }
    }
}

cards_rect_list, animename_list = [], []

class Cards:
    def __init__(self):
        return self
    
    # def Render(screen):
    #     cardsList, animenameList = [], []
    #     pygame.init()
    #     font = pygame.font.Font('freesansbold.ttf', 32)
    #     c_posX, c_posY, t_posY = [], [], []
    #     for i in characterSet:
    #             animenametext = font.render(characterSet[str(i)]["animename"], True, (255, 255, 255))
    #             animenameList.append(animenametext)
                
    #             for j in characterSet[i]["characters"]:
    #                 cardsImg1 = pygame.image.load(characterSet[str(i)]["characters"][str(j)]["card"])
    #                 cardsImg1 = pygame.transform.scale(cardsImg1, (170, 220))

    #                 cardsList.append(cardsImg1)
                    
    #                 if characterSet[str(i)]["characters"][str(j)]["posX"] > 10:
    #                     c_posX.append(characterSet[str(i)]["characters"][str(j)]["posX"] + cardsImg1.get_width())
    #                 else:
    #                     c_posX.append(characterSet[str(i)]["characters"][str(j)]["posX"])
    #                 c_posY.append(characterSet[str(i)]["posY"])
    #             t_posY.append(characterSet[str(i)]["tposY"])

    #     for (y, animename) in zip(t_posY, animenameList):
    #         screen.blit(animename, [10, y])
    #     for (x, y, cardsImg) in zip(c_posX, c_posY, cardsList):
    #         # screen.blit(cardsImg, [x, y])
    #         cardsRectList.extend([screen.blit(cardsImg, [x, y])])


    def render(screen):
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 32)

        # Pre-load card images
        card_images = {}
        for i in characterSet:
            for j in characterSet[i]["characters"]:
                card_file = characterSet[str(i)]["characters"][str(j)]["card"]
                if card_file not in card_images:
                    card_img = pygame.image.load(card_file).convert()
                    card_img = pygame.transform.scale(card_img, (170, 220))
                    card_images[card_file] = card_img

        cardsList, animenameList, c_posX, c_posY, t_posY = [], [], [], [], []

        for i in characterSet:
            animenametext = font.render(characterSet[str(i)]["animename"], True, (255, 255, 255))
            animenameList.append(animenametext)

            for j in characterSet[i]["characters"]:
                card_img = card_images[characterSet[str(i)]["characters"][str(j)]["card"]]
                cardsList.append(card_img)

                if characterSet[str(i)]["characters"][str(j)]["posX"] > 10:
                    c_posX.append(characterSet[str(i)]["characters"][str(j)]["posX"] + card_img.get_width())
                else:
                    c_posX.append(characterSet[str(i)]["characters"][str(j)]["posX"])
                c_posY.append(characterSet[str(i)]["posY"])
            t_posY.append(characterSet[str(i)]["tposY"])

        for (y, animename) in zip(t_posY, animenameList):
            screen.blit(animename, [10, y])
        for (x, y, card_img) in zip(c_posX, c_posY, cardsList):
            cards_rect_list.append(screen.blit(card_img, [x, y]))
