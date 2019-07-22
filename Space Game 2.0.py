#!/usr/bin/env python
import pygame
import random
from spacegame_variables import *
from sys import exit
from time import sleep

# List of things to add:
#     - Main Menu
#     - Pause Menu
#     - Victory Screen
#     - Score Text
#     - Music/Sound
#     - Enemy Lasers
#     - Player Health
#     - Boss Fight (?)

# ENTITY CLASSES
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemysprite
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playersprite
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        pygame.mouse.set_visible(0)

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = lasersprite
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 10

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cursor
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        pygame.mouse.set_visible(0)

class Enemy_Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemylasersprite
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 10

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
enemy_list = pygame.sprite.Group()
enemylaser_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
sprites_list = pygame.sprite.Group()
cursor_list = pygame.sprite.Group()
enemy_spawn_x = 95
enemy_spawn_y = 75
check = 0
enemy_list2 = []
enemyX_list = []
enemyY_list = []

# ENEMY SPAWNER
for i in range(15):
    enemy = Enemy()
    enemy.rect.x = enemy_spawn_x
    enemy.rect.y = enemy_spawn_y
    enemy_list2.append(enemy)
    enemyX_list.append(enemy_spawn_x)
    enemyY_list.append(enemy_spawn_y)
    enemy_list.add(enemy)
    sprites_list.add(enemy)
    enemy_spawn_x += 90
    check += 1
    if check == 5:
        enemy_spawn_y += 75
        enemy_spawn_x = 95
        check = 0

# MAIN GAME LOOP
def game():
    enemy = Enemy()
    player = Player()
    sprites_list.add(player)
    clock = pygame.time.Clock()
    score = 0
    player.rect.y = 450
    score = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = player.rect.x + 24
                laser.rect.y = player.rect.y - 20
                sprites_list.add(laser)
                laser_list.add(laser)

        enemyshoot = int(random.randint(0, 14))
        enemylaser = Enemy_Laser()
        enemylaser.rect.x = enemyX_list[enemyshoot]
        enemylaser.rect.y = enemyY_list[enemyshoot]
        sprites_list.add(enemylaser)
        enemylaser_list.add(enemylaser)

        sprites_list.update()

        for laser in laser_list:
            enemy_hit_list = pygame.sprite.spritecollide(laser, enemy_list, True)

            for enemy in enemy_hit_list:
                laser_list.remove(laser)
                sprites_list.remove(laser)
                score += 1
                print score

        screen.blit(background, (0, 0))
        sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    exit()

game()
