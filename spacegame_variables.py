#!/usr/bin/env python
import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# COLORS
gray = (159, 159, 159)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 214, 51)

# DIMENSIONS AND POSITIONS
width = 600
height = 570
size = (width, height)
screen = pygame.display.set_mode(size)
cursorX = 185
cursor_pauseX = 145
cursor_restartX = 135
cursor_exitX = 185
cursorY = 275
spaceX = 255
spaceY = 420

# TEXT VARIABLES
fontpath = "Arwing.ttf"
myfont = pygame.font.Font(fontpath, 75)
myfont2 = pygame.font.Font(fontpath, 40)
myfont3 = pygame.font.Font(fontpath, 25)

title = myfont.render("Space Jam", 1, yellow)
title_rect = title.get_rect(center = (width/2, 158))

playtext = myfont2.render("Play", 1, white)
playtext_rect = playtext.get_rect(center = (width/2, 298))

playtext2 = myfont2.render("Play", 1, gray)
playtext2_rect = playtext2.get_rect(center = (width/2, 298))

exitext = myfont2.render("Exit", 1, white)
exittext_rect = exitext.get_rect(center = (width/2, 358))

exitext2 = myfont2.render("Exit", 1, gray)
exittext2_rect = exitext.get_rect(center = (width/2, 358))

pause1 = myfont.render("Paused", 1, yellow)
pause1_rect = pause1.get_rect(center = (width/2, 158))

resume = myfont2.render("Resume", 1, white)
resume_rect = resume.get_rect(center = (width/2, 298))

resume2 = myfont2.render("Resume", 1, gray)
resume2_rect = resume2.get_rect(center = (width/2, 298))

restarttext = myfont2.render("Restart", 1, white)
restarttext_rect = restarttext.get_rect(center = (width/2, 298))

restarttext2 = myfont2.render("Restart", 1, gray)
restarttext2_rect = restarttext2.get_rect(center = (width/2, 298))

win = myfont.render("You Win!", 1, yellow)
win_rect = win.get_rect(center = (width/2, 158))

# IMAGE VARIABLES
cursor_image = pygame.image.load('cursor.png')
cursor = pygame.transform.scale(cursor_image, (45, 45))

background_image = pygame.image.load('background.png')
background = pygame.transform.scale(background_image, (600, 612))

spaceship_image = pygame.image.load('spaceship.png')
spaceship = pygame.transform.scale(spaceship_image, (83, 83))

laser_image = pygame.image.load('laser.png')
laser = pygame.transform.scale(laser_image, (35, 58))

enemy_image = pygame.image.load('enemy.png')
enemy = pygame.transform.scale(enemy_image, (50, 50))

enemylaser_image = pygame.image.load('enemylaser.png')
enemylaser = pygame.transform.scale(enemylaser_image, (50, 50))

explosion_image = pygame.image.load('explosion.png')
explosion = pygame.transform.scale(explosion_image, (50, 50))

# SOUND VARIABLES
selectsound = pygame.mixer.Sound('menuselect.wav')
startsound = pygame.mixer.Sound('gamestart.wav')
pause_sound = pygame.mixer.Sound('pausesound.wav')
lasersound = pygame.mixer.Sound('laser.wav')
enemydamagesound = pygame.mixer.Sound('enemydamage.wav')
