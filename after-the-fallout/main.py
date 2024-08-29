import pygame
import sys
import time
import random
from pygame import mixer
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

class constant:
    bg = 0, 0, 0
    pygame.init()
    screen = display_surface = pygame.display.set_mode((1360, 705))
    gameIcon = pygame.image.load("icon.png")
    state = "splash"
    mL = 0
    sL = 0

class intro:
    textShade = 250
    text1 = pygame.font.Font('Grand9K Pixel.ttf', 75)    # Font created and edited By: Jayvee D. Enaguas (Grand Chaos), credits for the Grand9K Pixel font given to them.
    intro1 = text1.render("Luka22r presents...", True, (textShade, textShade, textShade))
    titleRect = intro1.get_rect()
    titleRect.center = (700, 400)

    pfp = pygame.image.load("pfp.png")
    pfpRect = pfp.get_rect()
    pfpRect.center = (550, 100)
    pfp = pygame.transform.scale(pfp, (300, 300))

class game:
    heart = "heart.mp3"

    playerX = 700
    playerY = 600
    playerDirection = "left"
    playerChords = [playerX, playerY]
    playerLeft = pygame.transform.scale(pygame.image.load("left.png"), (150, 150))
    playerRight = pygame.transform.scale(pygame.image.load("right.png"), (150, 150))
    playerRect = playerLeft.get_rect()
    playerRect.center = tuple(playerChords)

    roomNumber = 1
    room2 = pygame.transform.scale(pygame.image.load("background2.png"), (1375, 700))
    room1 = pygame.transform.scale(pygame.image.load("background1.png"), (1375, 700))

    playerTextNumber = 2
    playerTextChords = [700, 0]
    text2 = pygame.font.Font('Grand9K Pixel.ttf', 25)    # Font created and edited By: Jayvee D. Enaguas (Grand Chaos), credits for the Grand9K Pixel font given to them.
    playerText1 = text2.render("Unknown: AAAHHHHHHH", True, (intro.textShade, intro.textShade, intro.textShade))
    playerTextRect = playerText1.get_rect()
    playerTextRect.center = tuple(playerTextChords)

    playerText2 = text2.render("Patrick: Youch!", True, (intro.textShade, intro.textShade, intro.textShade))
    playerText3 = text2.render("Patrick: Where... Am I?", True, (intro.textShade, intro.textShade, intro.textShade))
    playerText4 = text2.render("Patrick: Let's find a way back to the surface.", True, (intro.textShade, intro.textShade, intro.textShade))
    playerText5 = text2.render("A stone, a good tool for breaking things.", True, (intro.textShade, intro.textShade, intro.textShade))
    playerText6 = text2.render("The sewer exit is blocked by a bolder...", True, (intro.textShade, intro.textShade, intro.textShade))


class menu:
    drip = "drip.mp3"

    startButton = pygame.transform.scale(pygame.image.load("startButton.png"), (250, 250))
    startButton2 = pygame.transform.scale(pygame.image.load("startButton2.png"), (250, 250))
    startButton3 = pygame.transform.scale(pygame.image.load("startButton3.png"), (250, 250))
    startButton4 = pygame.transform.scale(pygame.image.load("startButton4.png"), (250, 250))
    startButtonRect = startButton.get_rect()
    startButtonRect.center = (650, 600)

    afterTitle = pygame.transform.scale(pygame.image.load("afterTitle.png"), (400, 400))
    theTitle = pygame.transform.scale(pygame.image.load("theTitle.png"), (400, 400))
    falloutTitle = pygame.transform.scale(pygame.image.load("falloutTitle.png"), (400, 400))
    afterRect = afterTitle.get_rect()
    theRect = theTitle.get_rect()
    falloutRect = falloutTitle.get_rect()
    afterRect.center = (650, 300)
    theRect.center = (650, 410)
    falloutRect.center = (700, 525)
 
    backstoryText1 = game.text2.render("It all started on the 5th of November, 2038. After 85 years of ceasefire across", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText2 = game.text2.render("after the British Prime Minister at the time, David Smith, a ", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText3 = game.text2.render("the North and South Korean borders, peace negotiations began to degrade", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText4 = game.text2.render("reformist, made a sarcastic comment about the North Korean military integrity.", True, (intro.textShade, intro.textShade, intro.textShade))

    backstoryTextRect1 = backstoryText1.get_rect()
    backstoryTextRect1.center = (700, 50)
    backstoryTextRect2 = backstoryText2.get_rect()
    backstoryTextRect2.center = (700, 250)
    backstoryTextRect3 = backstoryText3.get_rect()
    backstoryTextRect3.center = (700, 150)
    backstoryTextRect4 = backstoryText4.get_rect()
    backstoryTextRect4.center = (700, 350)

    korea = pygame.transform.scale(pygame.image.load("korea.png"), (600, 400))
    koreaRect = korea.get_rect()
    koreaRect.center = (700, 565)

    backstoryText5 = game.text2.render("After this foolish action the North Korean leader responded with a nuclear death threat.", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText6 = game.text2.render("A mere day later the British army detected a supersonic flying dutch civilian vehical hurtling over the british", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText7 = game.text2.render("isles, in a desperate attempt to protect the nation from destruction thinking this vehical was a warhead", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText8 = game.text2.render("the british goverment shot it down and notified the rest of NATO.", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText9 = game.text2.render("Eventually, North Korea responded with war and the rest was history.", True, (intro.textShade, intro.textShade, intro.textShade))

    backstoryTextRect5 = backstoryText5.get_rect()
    backstoryTextRect5.center = (700, 50)
    backstoryTextRect6 = backstoryText6.get_rect()
    backstoryTextRect6.center = (700, 100)
    backstoryTextRect7 = backstoryText7.get_rect()
    backstoryTextRect7.center = (700, 150)
    backstoryTextRect8 = backstoryText8.get_rect()
    backstoryTextRect8.center = (700, 200)
    backstoryTextRect9 = backstoryText9.get_rect()
    backstoryTextRect9.center = (700, 250)

    mushroomCloud = pygame.transform.scale(pygame.image.load("mushroom-cloud.png"), (600, 400))
    mushroomCloudRect = mushroomCloud.get_rect()
    mushroomCloudRect.center = (700, 565)

    backstoryText10 = game.text2.render("11 year later the echos of this wars scars still remain, with the remaining human population now mutated", True, (intro.textShade, intro.textShade, intro.textShade))
    backstoryText11 = game.text2.render("by the ongoing nuclear winter. Alone among this changed world is a inncoent child looking for a home.", True, (intro.textShade, intro.textShade, intro.textShade))

    backstoryTextRect10 = backstoryText10.get_rect()
    backstoryTextRect10.center = (700, 100)
    backstoryTextRect11 = backstoryText11.get_rect()
    backstoryTextRect11.center = (700, 200)

def physicClock(screen):
    if constant.mL >= 0:
        constant.mL = constant.mL + 1
    if constant.mL == 5:
        constant.mL = constant.mL - 5
    if constant.mL == 4:
        constant.sL = constant.sL + 1
    elif constant.sL >= 4:
        constant.sL = 0
    print("Clock:", constant.sL)

def renderALL(screen):
    if constant.state == "game":
        if game.roomNumber == 1:
            screen.blit(game.room1, (0, 0))
            if game.playerTextNumber == 2:
                screen.blit(game.playerText2, game.playerTextRect)
            elif game.playerTextNumber == 3:
                screen.blit(game.playerText3, game.playerTextRect)
            elif game.playerTextNumber == 4:
                screen.blit(game.playerText4, game.playerTextRect)
            elif game.playerTextNumber == 5:
                screen.blit(game.playerText5, game.playerTextRect)

        elif game.roomNumber == 2:
            screen.blit(game.room2, (0, 0))

        if game.playerDirection == "left":
                game.playerRect.center = (game.playerX, game.playerY)
                screen.blit(game.playerLeft, game.playerRect)
        elif game.playerDirection == "right":
                game.playerRect.center = (game.playerX, game.playerY)
                screen.blit(game.playerRight, game.playerRect)
    pygame.display.update()

def backstory(screen):
    print("game started")
    introducing = True
    backstoryPart = 0
    while introducing:
        if backstoryPart == 0:
            screen.fill(constant.bg)
            screen.blit(menu.backstoryText1, menu.backstoryTextRect1)
            screen.blit(menu.backstoryText2, menu.backstoryTextRect2)
            screen.blit(menu.backstoryText3, menu.backstoryTextRect3)
            screen.blit(menu.backstoryText4, menu.backstoryTextRect4)
            screen.blit(menu.korea, menu.koreaRect)

        elif backstoryPart == 1:
            screen.fill(constant.bg)
            screen.blit(menu.backstoryText5, menu.backstoryTextRect5)
            screen.blit(menu.backstoryText6, menu.backstoryTextRect6)
            screen.blit(menu.backstoryText7, menu.backstoryTextRect7)
            screen.blit(menu.backstoryText8, menu.backstoryTextRect8)
            screen.blit(menu.backstoryText9, menu.backstoryTextRect9)
            screen.blit(menu.mushroomCloud, menu.mushroomCloudRect)

        elif backstoryPart == 2:
            screen.fill(constant.bg)
            screen.blit(menu.backstoryText10, menu.backstoryTextRect10)
            screen.blit(menu.backstoryText11, menu.backstoryTextRect11)
            screen.blit(menu.mushroomCloud, menu.mushroomCloudRect)

        elif backstoryPart == 3:
            screen.fill(constant.bg)
            introducing = False

        print(backstoryPart)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("User quit: Program shutdown")

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and backstoryPart > 0:
                backstoryPart -= 1
            elif keys[pygame.K_RIGHT] and backstoryPart < 3:
                backstoryPart += 1


        for event in pygame.event.get():
            if keys[K_LEFT] and backstoryPart > 0:
                backstoryPart = backstoryPart - 1
            if keys[K_RIGHT] and backstoryPart < 2:
                backstoryPart = backstoryPart + 1
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("User quit: Program shutdown")

def draw_intro(screen):
    screen.fill(constant.bg)
    screen.blit(intro.pfp, intro.pfpRect)
    screen.blit(intro.intro1, intro.titleRect)
    if intro.textShade <= 2:
        mixer.init()
        mixer.music.load(menu.drip)
        mixer.music.set_volume(1)
        mixer.music.play(-1)
        constant.state = "menu"
    else:
        intro.textShade = intro.textShade - 1
        intro.intro1 = intro.text1.render("Luka22r presents...", True, (intro.textShade, intro.textShade, intro.textShade))

def draw_menu(screen):
    if constant.sL == 0:
        screen.fill(constant.bg)
        screen.blit(game.room2, (0, 0))
        screen.blit(menu.startButton, menu.startButtonRect)
        screen.blit(menu.afterTitle, menu.afterRect)
        screen.blit(menu.theTitle, menu.theRect)
        screen.blit(menu.falloutTitle, menu.falloutRect)
        pygame.display.update()

    if constant.sL == 1:
        screen.fill(constant.bg)
        screen.blit(game.room2, (0, 0))
        screen.blit(menu.startButton2, menu.startButtonRect)
        screen.blit(menu.afterTitle, menu.afterRect)
        screen.blit(menu.theTitle, menu.theRect)
        screen.blit(menu.falloutTitle, menu.falloutRect)
        pygame.display.update()
    
    if constant.sL == 2:
        screen.fill(constant.bg)
        screen.blit(game.room2, (0, 0))
        screen.blit(menu.startButton3, menu.startButtonRect)
        screen.blit(menu.afterTitle, menu.afterRect)
        screen.blit(menu.theTitle, menu.theRect)
        screen.blit(menu.falloutTitle, menu.falloutRect)
        pygame.display.update()
    
    if constant.sL == 3:
        screen.fill(constant.bg)
        screen.blit(game.room2, (0, 0))
        screen.blit(menu.startButton4, menu.startButtonRect)
        screen.blit(menu.afterTitle, menu.afterRect)
        screen.blit(menu.theTitle, menu.theRect)
        screen.blit(menu.falloutTitle, menu.falloutRect)
        pygame.display.update()

def draw_game(screen):
    keys = pygame.key.get_pressed()
    screen.fill(constant.bg)

    if game.roomNumber==1:
        if game.playerX <= 360 and game.playerY <= 650: # Steps room 1
            game.playerY = game.playerY + 5
        elif game.playerX >= 375 and game.playerY >= 610:
            game.playerY = game.playerY - 5

    if game.playerTextChords[1] <= 250: # text falling
        game.playerTextChords[0] = game.playerTextChords[0] - 5
        game.playerTextChords[1] = game.playerTextChords[1] + 5
        game.playerTextRect.center = tuple(game.playerTextChords)
        screen.blit(game.playerText1, game.playerTextRect)
        pygame.display.update()
    else:
        if game.playerX >= 1200:
            game.roomNumber = game.roomNumber - 1
            game.playerX = 10
        elif game.playerX <= 0:
            game.roomNumber = game.roomNumber + 1
            game.playerX = 1100

        if keys[K_LEFT]: # movement
            game.playerDirection = "left"
            game.playerX = game.playerX - 5
            game.playerRect.center = (game.playerX, game.playerY)
            print(game.playerX)
        elif keys[K_RIGHT]:
            if game.playerX <=900:
                if game.roomNumber==1:
                    game.playerDirection = "right"
                    game.playerX = game.playerX + 5
                    game.playerRect.center = (game.playerX, game.playerY)
            if game.roomNumber > 1:
                game.playerDirection = "right"
                game.playerX = game.playerX + 5
                game.playerRect.center = (game.playerX, game.playerY)
        elif keys[K_RETURN]:
            if constant.mL==1:
                if game.roomNumber==1:
                    if game.playerTextNumber <= 3:
                        game.playerTextNumber = game.playerTextNumber + 1

        renderALL(screen)
        pygame.display.update()

pygame.display.set_icon(constant.gameIcon)

while True:
    physicClock(constant.screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("User quit: Program shutdown")

        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            print(mousePos)
            mousePos = list(mousePos)
            if mousePos[0] >= 525 and mousePos[0] <= 775 and mousePos[1] >= 515 and mousePos[1] <= 600:
                pygame.mixer.music.stop() 
                backstory(constant.screen)
                mixer.init()
                mixer.music.load(game.heart)
                mixer.music.set_volume(1)
                mixer.music.play(1)
                titleShade = 250
                constant.state = "game"

    if constant.state == "splash":
        draw_intro(constant.screen)
    elif constant.state == "menu":
        draw_menu(constant.screen)
    elif constant.state == "game":
        draw_game(constant.screen)

    pygame.display.update()