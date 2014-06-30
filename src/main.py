#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from player import Player
import time
import ntpath

#resolution = 640, 480
pygame.init()
scenery1 = "../resources/imagens/scenarios/namek-3d-2.jpg"
scenery2 = "../resources/imagens/scenarios/Wasteland-2.jpg"
scenery3 = "../resources/imagens/scenarios/trunks-future-2.png"
scenery4 = "../resources/imagens/scenarios/arena-2-2.gif"
scenery = [pygame.image.load(scenery1),pygame.image.load(scenery2),pygame.image.load(scenery3),pygame.image.load(scenery4)]
menu_image = "../resources/imagens/Openning/goku-vs-vegeta-2.jpg"
background = pygame.image.load(scenery4)
resolution = background.get_size()
width, height = resolution
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN, 32)
#screen = pygame.display.set_mode(resolution)
background.convert()
background_openning = pygame.image.load(menu_image).convert()
#background_openning = pygame.transform.flip(background_openning, 1,0)
scene1 = pygame.transform.scale(scenery[0], (500,300))
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
gameState = 0 #Menu
previousGameState = 0
s0Option = range(4) 
is0 = 0
s1Option = range(5)
is1 = 0
s3Option = range(4)
is3 = 0
sc = 0
sg = 0
volume = 0.9
vsPC = False
song1 = '../resources/sounds/sparking.mp3'
song2 = '../resources/sounds/temos-a-forca-1.wav'
song3 = '../resources/sounds/cha-la.mp3'
song = [song1,song2,song3]

player1 = Player(acaoInicial="down")
player1.loadCharacter('goku')
power1 = SpriteAnimation(acaoInicial="void")
player1.loadPower1(power1)
player2 = Player(acaoInicial="down")
player2.loadCharacter('vegeta')
power2 = SpriteAnimation(acaoInicial="void")
player2.loadPower2(power2)

delta = 13 #Velocidade do movimento, quanto maior mais rapido
player2.facingRight = False
player2.x = 850
player2.y = 350

def restart():
    """
    Restar the game
    """
    player2.acao = "down"
    player1.acao = "down"
    player1.pos = 1
    player2.pos = 1
    player1.movex, player1.movey = 0,0
    player2.movex, player2.movey = 0,0
    player1.facingRight = True
    player2.facingRight = False
    player1.x = 250
    player1.y = 350
    player2.x = 850
    player2.y = 350
    player1.HP = 140
    player2.HP = 140
    player1.XP = 30
    player2.XP = 30

def show_splashscreen():
    """
    Show the splash screen.
    This is called once when the game is first started.
    """
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.mixer.music.load('../resources/splash.ogg')
    pygame.mixer.music.play()
    white = 250, 250, 250
    screen.fill(white) 
    # Slowly fade the splash screen image from white to opaque. 
    splash = pygame.image.load("../resources/estevaosplash.png").convert()
    for i in range(25):
        splash.set_alpha(i)
        screen.blit(splash, (90,50))
        pygame.display.update()
        pygame.time.wait(100)

    pygame.mixer.fadeout(2000)
    screen.blit(splash,(90,50))
    pygame.display.update()
    pygame.time.wait(1500)
    global gameState
    gameState = 0

def openMenu():
    """
    Main Menu
    """
    global gameState
    global previousGameState
    global vsPC
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    titlefont = pygame.font.SysFont("monospace", 75,bold = True)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    title = titlefont.render("SS4-Battle", 1, (255,255,255))
    playerVsPlayer = myfont.render("Player Vs Player", 1, (255,255,255))
    playerVsPc = myfont.render("Player Vs Pc", 1, (255,255,255))
    options = myfont.render("Options", 1, (255,255,255))
    quit = myfont.render("Quit", 1, (255,255,255))


    global is0
    if s0Option[is0] == 0:
        playerVsPlayer = boldFont.render("Player Vs Player", 1, (255,255,255))
    if s0Option[is0] == 1:
        playerVsPc = boldFont.render("Player Vs Pc", 1, (255,255,255))
    if s0Option[is0] == 2:
        options = boldFont.render("Options", 1, (255,255,255))
    if s0Option[is0] == 3:
        quit = boldFont.render("Quit", 1, (255,255,255))

    #screen.blit(title, (200,105))
    screen.blit(playerVsPlayer, (300,505))
    screen.blit(playerVsPc, (300,555))
    screen.blit(options, (300,605))
    screen.blit(quit, (300,655))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                if s0Option[is0] == 0:
                    #gameState = 2
                    #vsPC = False
                    gameState = 4
                    restart()
                if s0Option[is0] == 1:
                    previousGameState = 0
                    #gameState = 2
                    #vsPC = True
                if s0Option[is0] == 2:
                    previousGameState = 0
                    gameState = 3
                if s0Option[is0] == 3:
                    pygame.quit()
                    sys.exit()

            if event.key==K_DOWN:
                if s0Option[is0] < s0Option[-1]:
                    is0 += 1
                    # to jump player vs PC
                    if is0 == 1:
                        is0 +=1
            if event.key==K_UP:
                if s0Option[is0] > s0Option[0]:
                    is0 -= 1
                    # to jump player vs PC
                    if is0 == 1:
                        is0 -=1
def Options():
    """
    Option Menu
    """
    global gameState
    global delta
    global previousGameState
    global volume
    global song
    global sg
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    playerVsPlayer = myfont.render("Game Speed "+str(delta), 1, (255,255,255))
    playerVsPc = myfont.render("Music Volume "+str(volume*100), 1, (255,255,255))
    options = myfont.render("Resume", 1, (255,255,255))
    music = myfont.render("Music", 1, (255,255,255))
    title = myfont.render(ntpath.basename(song[sg]), 1, (255,255,255))

    global is3
    if s3Option[is3] == 0:
        playerVsPlayer = boldFont.render("Game Speed "+str(delta), 1, (255,255,255))
    if s3Option[is3] == 2:
        playerVsPc = boldFont.render("Music Volume "+str(volume*100), 1, (255,255,255))
    if s3Option[is3] == 3:
        options = boldFont.render("Resume", 1, (255,255,255))
    if s3Option[is3] == 1:
        music = boldFont.render("Music", 1, (255,255,255))
        title = boldFont.render(ntpath.basename(song[sg]), 1, (255,255,255))
    screen.blit(playerVsPlayer, (340,250))
    screen.blit(playerVsPc, (340,350))
    screen.blit(options, (340,395))
    screen.blit(music, (340,305))
    screen.blit(title, (540,305))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                if s3Option[is3] == 3:
                    gameState = 2
            if event.key==K_DOWN:
                if s3Option[is3] < s3Option[-1]:
                    is3 += 1
            if event.key==K_UP:
                if s3Option[is3] > s3Option[0]:
                    is3 -= 1
            if event.key==K_RIGHT:
                if s3Option[is3] == 0:
                    delta += 1
                if s3Option[is3] == 2:
                    if volume < 0.9:
                        volume += 0.1
                        pygame.mixer.music.set_volume(volume)
                if s3Option[is3] == 1:
                    if sg == len(song)-1:
                        sg =-1
                    sg +=1
                    loadMusic(song[sg])
            if event.key==K_LEFT:
                if s3Option[is3] == 0:
                    delta -= 1
                if s3Option[is3] == 2:
                    if volume > 0.1:
                        volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
                    if volume < 0.2:
                        volume = 0
                        pygame.mixer.music.set_volume(volume)
                if s3Option[is3] == 1:
                    if sg == 0:
                        sg =len(song)
                    sg -=1
                    loadMusic(song[sg])
def chooseScenery():
    """
    Choose Scenery Screen
    """
    global gameState
    global previousGameState
    global sc
    global background
    global scenery
    global scene1
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)

    playerVsPlayer = boldFont.render(">", 1, (255,255,255))
    playerVsPlayer2 = boldFont.render("<", 1, (255,255,255))
    screen.blit(playerVsPlayer, (865,420))
    screen.blit(playerVsPlayer2, (300,420))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                    gameState = 2
                    vsPC = False
                    background = scenery[sc]
            if event.key==K_RIGHT:
                if sc == len(scenery)-1:
                    sc =-1
                sc +=1
                scene1 = pygame.transform.scale(scenery[sc], (500,300))
            if event.key==K_LEFT:
                if sc == 0:
                    sc = len(scenery)
                sc -=1
                scene1 = pygame.transform.scale(scenery[sc], (500,300))
    screen.blit(scene1,(350,300))
    pygame.display.update()

def loadMenu():
    """
    Menu during the playing game
    """
    global gameState
    global previousGameState
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    initialScreen = myfont.render("Initial Screen", 1, (255,255,255))
    playerVsPlayer = myfont.render("Resume", 1, (255,255,255))
    playerVsPc = myfont.render("Options", 1, (255,255,255))
    options = myfont.render("Restart", 1, (255,255,255))
    quit = myfont.render("Quit", 1, (255,255,255))

    global is1
    if s1Option[is1] == 0:
        initialScreen = boldFont.render("Initial Screen", 1, (255,255,255))
    if s1Option[is1] == 1:
        playerVsPlayer = boldFont.render("Resume", 1, (255,255,255))
    if s1Option[is1] == 2:
        playerVsPc = boldFont.render("Options", 1, (255,255,255))
    if s1Option[is1] == 3:
        options = boldFont.render("Restart", 1, (255,255,255))
    if s1Option[is1] == 4:
        quit = boldFont.render("Quit", 1, (255,255,255))
    screen.blit(initialScreen, (340,250))
    screen.blit(playerVsPlayer, (340,305))
    screen.blit(playerVsPc, (340,360))
    screen.blit(options, (340,415))
    screen.blit(quit, (340,470))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = 2
                previousGameState = 1
            if event.key==K_RETURN:
                if s1Option[is1] == 0:
                    gameState = 0
                if s1Option[is1] == 1:
                    gameState = 2
                if s1Option[is1] == 2:
                    gameState = 3
                    previousGameState = 1
                if s1Option[is1] == 3:
                    restart()
                    gameState = 2
                if s1Option[is1] == 4:
                    pygame.quit()
                    sys.exit()
            if event.key==K_DOWN:
                if s1Option[is1] < s1Option[-1]:
                    is1 += 1
            if event.key==K_UP:
                if s1Option[is1] > s1Option[0]:
                    is1 -= 1
def loadMusic (music):
    """Load the musics of a list"""
    #pygame.mixer.music.load('resources/sounds/sparking.mp3')
    pygame.mixer.music.load(music)
    #pygame.mixer.music.play(-1,9)
    pygame.mixer.music.play(-1)

def playPC():
    if player2.XP > 20:
        player2.acao = "kameham"
        power2.acao = "kame"
        player2.pressed = True
        power2.pressed = True
        player2.pos = 1
        player2.Attacking = True
        player2.Defending = False
        if player2.facingRight == False:
            player2AttackRect = Rect(player2.x-950, player2.y+10, 1000, 60)
            #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
        elif player2.facingRight == True:
            player2AttackRect = Rect(player2.x+45, player2.y+10, 1000, 60)
            #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
        if player2AttackRect.colliderect(player1.Rect) == True:
            if player1.Defending == False:
                player1.HP -= 10
            if player1.Defending == True and player1.Attacking == False:
                player1.HP -= 2
        player2.acao = "down"
        player2.XP-=10
    if player2.XP <0 or player2.XP < 30:
        player2.acao = "load"
        player2.pressed = True
        player2.pos = 1
        player2.XP+= 5 

def playLoop():
    """
    Game Loop
    """
    global vsPC
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if vsPC == False:
            player1.playPlayer1(event,player2,power1)
            player2.playPlayer2(event,player1,power2)
        #playPlayer2(event)
        elif vsPC == True:
            player1.playPlayer1(event,player2,power1)
            #playPC() 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                global gameState
                global previousGameState
                gameState = 1
                previousGameState = 2
    global width
    global height
    player1.TurnAround1(player2)
    player1.movementInsideScreen1(width,height,delta)
    player2.movementInsideScreen2(width,height,delta)
    player1.powerPlacing1(power1)
    player2.powerPlacing2(power2)
    player1.rect1()
    player2.rect2()
    player1.statusBar1(screen)
    player2.statusBar2(screen,width)
    player2.standUpPosition2()
    player2.defeated2(screen)
    clock.tick(60)
    player2.update(player2.pos,screen)
    player1.update(player1.pos,screen)
    power1.update(player1.pos,screen)
    power2.update(player2.pos,screen)
    pygame.display.update()

show_splashscreen()
loadMusic(song[0])
while 1:
    if gameState == 0:
        openMenu()
    elif gameState == 1:
        loadMenu()
    elif gameState == 2:
        playLoop()
    elif gameState == 3:
        Options()
    elif gameState == 4:
        chooseScenery()

