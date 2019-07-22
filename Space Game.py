#!/usr/bin/env python
import pygame
from sys import exit
from time import sleep
from spacegame_variables import *
from random import randint

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# MENU/PAUSE CONTROLS


def cursor_controls(cursorY, resumegame, exit1):
    start = False
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        if cursorY == 335:
            cursorY = 335
        elif cursorY != 335:
            selectsound.play()
            cursorY = cursorY + 60
            exit1 = True
    if keys[pygame.K_UP]:
        if cursorY == 275:
            cursorY = 275
        elif cursorY != 275:
            selectsound.play()
            cursorY = cursorY - 60
            exit1 = False
    if keys[pygame.K_RETURN]:
        if cursorY == 335:
            pygame.quit()
            exit(0)
        elif cursorY == 275:
            startsound.play()
            pygame.mixer.music.pause()
            sleep(.8)
            start = True
        elif cursorY == 275 and resumegame == False:
            resumegame = True
            pygame.mixer.music.unpause()
    return cursorY, start, resumegame, exit1

# IN-GAME CONTROLS


def game_controls(spaceX):
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if spaceX > 0:
            spaceX = spaceX - 0.9
    if keys[pygame.K_RIGHT]:
        if spaceX < 515:
            spaceX = spaceX + 0.9
    if keys[pygame.K_ESCAPE]:
        cursorY = 275
        pygame.mixer.music.pause()
        pause_sound.play()
        pause(cursorY)
    return spaceX

# MAIN MENU


def menu(cursorY):
    pygame.mixer.music.load('menu_music.mp3')
    pygame.mixer.music.play(-1, 0.5)
    start = False
    resumegame = True
    exit1 = False
    while start == False:
        screen.blit(background, (0, 0))
        screen.blit(cursor, (cursorX, cursorY))
        if cursorY == 275:
            screen.blit(playtext, (playtext_rect))
            screen.blit(exitext2, (exittext2_rect))
        elif cursorY == 335:
            screen.blit(playtext2, (playtext2_rect))
            screen.blit(exitext, (exittext_rect))
        screen.blit(title, (title_rect))
        pygame.display.flip()
        cursorY, start, resumegame, exit1 = cursor_controls(
            cursorY, resumegame, exit1)
    pygame.mixer.music.load('game_music.mp3')
    pygame.mixer.music.play(-1, 0.0)
    sleep(0.6)
    game(spaceX, spaceY, cursorY)

# PAUSE MENU


def pause(cursorY):
    start = False
    resumegame = False
    exit1 = False
    while start == False:
        screen.blit(background, (0, 0))
        if cursorY == 275:
            screen.blit(resume, (resume_rect))
            screen.blit(exitext2, (exittext2_rect))
        elif cursorY == 335:
            screen.blit(resume2, (resume2_rect))
            screen.blit(exitext, (exittext_rect))
        if exit1 == True:
            screen.blit(cursor, (cursor_exitX, cursorY))
        else:
            screen.blit(cursor, (cursor_pauseX, cursorY))
        screen.blit(pause1, (pause1_rect))
        pygame.display.flip()
        cursorY, start, resumegame, exit1 = cursor_controls(
            cursorY, resumegame, exit1)
        if resumegame == True:
            break
    pygame.mixer.music.unpause()

# VICTORY SCREEN


def victory(cursorY, score):
    start = False
    resumegame = True
    exit1 = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load('victory.mp3')
    pygame.mixer.music.play(0, 0.0)
    while start == False:
        screen.blit(background, (0, 0))
        scoretext = myfont3.render("Score: %d" % score, 1, white)
        if cursorY == 275:
            screen.blit(restarttext, (restarttext_rect))
            screen.blit(exitext2, (exittext2_rect))
        elif cursorY == 335:
            screen.blit(restarttext2, (restarttext2_rect))
            screen.blit(exitext, (exittext_rect))
        if exit1 == True:
            screen.blit(cursor, (cursor_exitX, cursorY))
        else:
            screen.blit(cursor, (cursor_restartX, cursorY))
        screen.blit(win, (win_rect))
        screen.blit(scoretext, (10, 10))
        pygame.display.flip()
        cursorY, start, resumegame, exit1 = cursor_controls(
            cursorY, resumegame, exit1)
    pygame.mixer.music.load('game_music.mp3')
    pygame.mixer.music.play(-1, 0.0)
    sleep(0.6)
    game(spaceX, spaceY, cursorY)

# PLAYS GAME


def game(spaceX, spaceY, cursorY):
    enemyX = [95, 183, 273, 363, 455, 95, 183,
              273, 363, 455, 95, 183, 273, 363, 455]
    enemyY = [75, 75, 75, 75, 75, 150, 150,
              150, 150, 150, 225, 225, 225, 225, 225]
    enemy_list = []
    enemy_number = 0
    score = 0
    while True:
        enemy_list.append(enemy)
        scoretext = myfont3.render("Score: %d" % score, 1, white)
        screen.blit(background, (0, 0))
        screen.blit(scoretext, (10, 10))
        screen.blit(spaceship, (spaceX, spaceY))
        for enemy_number in range(0, enemy_number + 1):
            screen.blit(enemy_list[enemy_number],
                        (enemyX[enemy_number], enemyY[enemy_number]))
            if enemy_number != 14:
                enemy_number = enemy_number + 1
        pygame.display.flip()
        spaceX = game_controls(spaceX)
        spaceX, score = playerlaser(
            spaceX, enemy_list, enemy_number, enemyY, enemyX, score, scoretext)
        if score == 15:
            victory(cursorY, score)

# PLAYER SHOOTS LASER


def playerlaser(spaceX, enemy_list, enemy_number, enemyY, enemyX, score, scoretext):
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        lasersound.play()
        laserX = spaceX + 24
        laserY = spaceY - 20
        hitcheck = 0
        while laserY > 0:
            spaceX = game_controls(spaceX)
            laserY = laserY - 1
            screen.blit(background, (0, 0))
            screen.blit(laser, (laserX, laserY))
            screen.blit(spaceship, (spaceX, spaceY))
            for enemy_number in range(0, enemy_number + 1):
                screen.blit(enemy_list[enemy_number],
                            (enemyX[enemy_number], enemyY[enemy_number]))
                if enemy_number != 14:
                    enemy_number = enemy_number + 1
            screen.blit(scoretext, (10, 10))
            pygame.display.flip()
            for number in range(0, 15):
                hitcheck, score = lasershot(
                    number, laserX, laserY, enemyX, enemyY, enemy_list, score, hitcheck)
            if hitcheck == 1:
                enemydamagesound.play()
                break
    return spaceX, score

# LASER HIT CHECK


def lasershot(enemy_number, laserX, laserY, enemyX, enemyY, enemy_list, score, hitcheck):
    if laserY == enemyY[enemy_number] and laserX >= (enemyX[enemy_number] - 25) and laserX <= (enemyX[enemy_number] + 35):
        enemy_list.pop(enemy_number)
        screen.blit(explosion, (enemyX[enemy_number], enemyY[enemy_number]))
        pygame.display.flip()
        sleep(0.05)
        enemyX[enemy_number] = 1000
        enemyY[enemy_number] = 1000
        hitcheck = 1
        score = score + 1
    return hitcheck, score

# ENEMY LASER


def enemylasers(spaceX, enemy_list, enemy_number, enemyY, enemyX, score, scoretext):
    enemy_shoot = 1
    lasersound.play()
    enemylaserX = enemyX[enemy_shoot]
    enemylaserY = enemyY[enemy_shoot] + 5
    enemy_number = 0
    while enemylaserY < 570:
        spaceX = game_controls(spaceX)
        spaceX, score = playerlaser(
            spaceX, enemy_list, enemy_number, enemyY, enemyX, score, scoretext)
        enemylaserY = enemylaserY + 1
        screen.blit(background, (0, 0))
        screen.blit(enemylaser, (enemylaserX, enemylaserY))
        screen.blit(spaceship, (spaceX, spaceY))
        for enemy_number in range(0, enemy_number + 1):
            screen.blit(enemy_list[enemy_number],
                        (enemyX[enemy_number], enemyY[enemy_number]))
            if enemy_number != 14:
                enemy_number = enemy_number + 1
        screen.blit(scoretext, (10, 10))
        pygame.display.flip()
    return spaceX, score


menu(cursorY)
