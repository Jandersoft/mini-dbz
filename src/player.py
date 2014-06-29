#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
import time

class Player(SpriteAnimation):
    def __init__(self, acaoInicial, speed = 15):
        """Iniciation of the player states"""
        SpriteAnimation.__init__(self,acaoInicial, speed = 15)
        self.pos = 1
        self.movex, self.movey = 0,0
        self.facingRight = True
        self.x = 200
        self.y = 300
        self.Rect = Rect(self.x, self.y, 35, 70)
        self.HP = 150
        self.XP =30
        self.Defending = False
        self.Attacking = False
        self.punchDamage = 0
        self.kickDamage = 0
        self.hitDefended = 0
        self.powerDamage = 0
        self.powerDamageDefended = 0
        self.inicio = 0

    def playPlayer1(self,eventArg, player2, power1):
        if self.HP>0:
            event = eventArg
            if event.type == KEYDOWN:
                #Goku
                if event.key == K_s:
                    self.acao = "down"
                    self.pos = 1
                    self.movey+=1
                if event.key == K_w:
                    self.acao = "up"
                    self.pos = 1
                    self.movey-=1
                
                if event.key == K_p:
                    self.acao = "defend"
                    self.pos = 1
                    self.Defending = True
                if self.facingRight == True:
                    if event.key == K_d:
                        self.acao = "right"
                        self.pos = 1
                        self.movex+=1
                    if event.key == K_a:
                        self.acao = "up"
                        self.pos = 1
                        self.movex-=1
                if self.facingRight == False:
                    if event.key == K_d:
                        self.acao = "up"
                        self.pos = 1
                        self.movex+=1
                    if event.key == K_a:
                        self.acao = "right"
                        self.pos = 1
                        self.movex-=1
                if event.key == K_u:
                    if self.XP > 0:
                        self.acao = "kameham-1"
                        power1.acao = "kame"
                        self.pressed = True
                        power1.pressed = True
                        self.pos = 1
                        self.Attacking = True
                        self.Defending = False
                        if self.facingRight == True:
                            selfAttackRect = Rect(self.x+30, self.y+20, 1000, 60)
                            #pygame.draw.rect(screen, (0,255,0), selfAttackRect)
                        else:
                            selfAttackRect = Rect(self.x-1000, self.y+20, 1000, 60)
                            #pygame.draw.rect(screen, (0,255,0), selfAttackRect)
                        if selfAttackRect.colliderect(player2.Rect) == True:
                            if player2.Defending == False:
                                player2.HP -= self.powerDamage
                                player2.acao = "hited"
                                player2.inicio = time.time()
                            if player2.Defending == True and player2.Attacking == False:
                                player2.HP -= player2.powerDamageDefended
                        self.XP-=10
                if event.key == K_i:
                    self.acao = "punch"
                    self.pressed = True
                    self.pos = 1
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-5, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    if selfAttackRect.colliderect(player2.Rect) == True:
                        if player2.Defending == False:
                            player2.HP -= self.punchDamage
                            player2.acao = "hited"
                            player2.inicio = time.time()
                        if player2.Defending == True and player2.Attacking == False:
                            player2.HP -= player2.hitDefended
                if event.key == K_o:
                    self.acao = "kick"
                    self.pressed = True
                    self.pos = 1
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-5, self.y, 35, 70)
                        #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
                    if selfAttackRect.colliderect(player2.Rect) == True:
                        if player2.Defending == False:
                            player2.HP -= self.kickDamage
                            player2.acao = "hited"
                            player2.inicio = time.time()
                        if player2.Defending == True and player2.Attacking == False:
                            player2.HP -= player2.hitDefended

                if event.key == K_j:
                    self.acao = "load"
                    self.pressed = True
                    self.pos = 1
                    self.XP+= 5 
                    
            if event.type == KEYUP:
                if event.key == K_s:
                    self.acao = "down"
                    self.pos = 0
                    self.movey=0
                if event.key == K_w:
                    self.acao = "up"
                    self.pos = 0
                    self.movey=0
                if event.key == K_p:
                    self.acao = "defend"
                    self.pos = 0
                    self.Defending = False
                if event.key == K_i:
                    self.Attacking = False
                if self.facingRight  == True:
                    if event.key == K_d:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_a:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                if self.facingRight  == False:
                    if event.key == K_a:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_d:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0

                if event.key == K_u:
                    self.acao = "kameham-1"
                    power1.acao = "void"
                    self.pos = 0
                    self.movex=0
    
    def TurnAround1(self,player2):
        """
        Virar automaticamente
        """
        if self.x > player2.x:
            self.facingRight = False
            player2.facingRight = True
        if self.x < player2.x:
            self.facingRight = True
            player2.facingRight = False

    def movementInsideScreen1(self,width,height,delta):
        if self.facingRight == True:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.facingRight == False:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.movey == 1 and self.y<height-70:
            self.y += self.movey * delta
        if self.movey == -1 and self.y>0:
            self.y += self.movey * delta

    def movementInsideScreen2(self,width,height,delta):
        if self.facingRight == False:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.facingRight == True:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.movey == 1 and self.y<height-70:
            self.y += self.movey * delta
        if self.movey == -1 and self.y>0:
            self.y += self.movey * delta

    def powerPlacing1(self,power1):
        #Posicionamento dos Poderes
        if (self.facingRight == True):
            power1.x = self.x+45
            power1.y = self.y+25
        else:
            power1.x = self.x-930
            power1.y = self.y+20
    def powerPlacing2(self,power2):
        if (self.facingRight == False):
            power2.x = self.x-910
            power2.y = self.y+5
        elif (self.facingRight == True):
            power2.x = self.x+50
            power2.y = self.y+5

    def rect1(self):
        if self.acao != "right":
            self.Rect = Rect(self.x, self.y, 35, 70)
        elif self.acao == "right" and self.facingRight == True:
            self.Rect = Rect(self.x+30, self.y, 35, 70)
        elif self.acao == "right" and self.facingRight == False:
            self.Rect = Rect(self.x, self.y, 35, 70)

    def rect2(self):
        self.Rect = Rect(self.x, self.y, 35, 70)

    def hPRect1(self,screen):
        player1HPRect = Rect(80 , 20, self.HP*2, 20)
        player1XPRect = Rect(80 , 60, self.XP*2, 20)
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), player1HPRect)
        pygame.draw.rect(screen, (0,0,255), player1XPRect)
    
    def hPRect2(self,screen,width):
        """
        Barras de Hp e XP
        """
        player2HPRect = Rect(width-80, 20, -self.HP*2, 20)
        player2XPRect = Rect(width-80, 60, -self.XP*2, 20)
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), player2HPRect)
        pygame.draw.rect(screen, (0,0,255), player2XPRect)

    def standUpPosition2(self):
        if self.movex or self.movey !=0:
            self.inicio = time.time()
        if self.Defending== True:
            self.inicio = time.time()
        if time.time()-self.inicio>0.4 and self.HP>0:
            self.acao = "down"
            self.inicio = time.time()+1000

    def defeated2(self,screen,cronometrar,player1Win):
        if self.HP <= 0:
            #import pdb; pdb.set_trace()
            self.acao = "lose"
            if cronometrar == True:
                self.inicio = time.time()
                cronometrar = False
            if time.time()-self.inicio>1:
                screen.blit(player1Win, (300,150))

    def playPlayer2(self,eventArg,player1,power2):
        if self.HP>0:
            event = eventArg
            #Vegeta
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.acao = "down"
                    self.pos = 1
                    self.movey+=1
                if event.key == K_UP:
                    self.acao = "up"
                    self.pos = 1
                    self.movey-=1
                if self.facingRight == False:
                    if event.key == K_LEFT:
                        self.acao = "right"
                        self.pos = 1
                        self.movex-=1
                    if event.key == K_RIGHT:
                        self.acao = "up"
                        self.pos = 1
                        self.movex+=1
                if self.facingRight == True:
                    if event.key == K_LEFT:
                        self.acao = "up"
                        self.pos = 1
                        self.movex-=1
                    if event.key == K_RIGHT:
                        self.inicio = time.time()
                        self.acao = "right"
                        self.pos = 1
                        self.movex+=1
                if event.key == K_KP5:
                    self.acao = "defend"
                    self.pos = 1
                    self.Defending = True
                if event.key == K_KP8 or event.key == K_8:
                    self.inicio = time.time()
                    self.acao = "punch"
                    self.pos = 1
                    self.pressed = True
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == False:
                        player2AttackRect = Rect(self.x-15, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    elif self.facingRight == True:
                        player2AttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    if player2AttackRect.colliderect(player1.Rect) == True:
                        if player1.Defending == False:
                            player1.HP -= self.punchDamage
                            player1.acao = "hited"
                        if player1.Defending == True and player1.Attacking == False:
                            player1.HP -= player1.hitDefended
                if event.key == K_KP9:
                    self.inicio = time.time()
                    self.acao = "kick"
                    self.pos = 1
                    self.pressed = True
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == False:
                        player2AttackRect = Rect(self.x-5, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    if self.facingRight == True:
                        player2AttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    if player2AttackRect.colliderect(player1.Rect) == True:
                        if player1.Defending == False:
                            player1.HP -= self.kickDamage
                            player1.acao = "hited"
                        if player1.Defending == True and player1.Attacking == False:
                            player1.HP -= player1.hitDefended
                if event.key == K_KP7 or event.key == K_9:
                    if self.XP > 0:
                        self.inicio = time.time()
                        self.acao = "kameham"
                        power2.acao = "kame"
                        self.pressed = True
                        power2.pressed = True
                        self.pos = 1
                        self.Attacking = True
                        self.Defending = False
                        if self.facingRight == False:
                            player2AttackRect = Rect(self.x-950, self.y+10, 1000, 60)
                            #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
                        elif self.facingRight == True:
                            player2AttackRect = Rect(self.x+45, self.y+10, 1000, 60)
                            #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
                        if player2AttackRect.colliderect(player1.Rect) == True:
                            if player1.Defending == False:
                                player1.HP -= self.powerDamage
                                player1.acao = "hited"
                            if player1.Defending == True and player1.Attacking == False:
                                player1.HP -= player1.powerDamageDefended
                        self.XP-=10
                if event.key == K_KP4:
                    self.acao = "load"
                    self.pressed = True
                    self.pos = 1
                    self.XP+= 5 
                    self.inicio = time.time()

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    self.acao = "down"
                    self.pos = 0
                    self.movey=0
                if event.key == K_UP:
                    self.acao = "up"
                    self.pos = 0
                    self.movey=0
                if event.key == K_KP5:
                    self.acao = "defend"
                    self.pos = 0
                    self.Defending = False
                if self.facingRight == False:
                    if event.key == K_LEFT:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_RIGHT:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                if self.facingRight == True:
                    if event.key == K_LEFT:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_RIGHT:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
