# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 22:42:47 2022

@author: starg
"""

import pygame
from settings import *
import random
import math
from weapon import Weapon
from debug import debug

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../Graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        self.health = 200
        self.maxhealth = 1000
        self.hp_bar = 400
        self.hp_ratio = self.maxhealth / self.hp_bar
        self.inventory = []
        #self.weapon = Weapon('lance',20,3,player.rect)
        self.tick = 0
    
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
            
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0    
            
        if keys[pygame.K_LEFT]:
            self.direction.x = -1    
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1    
        else:
            self.direction.x = 0
            
    
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('hor')
        self.hitbox.y += self.direction.y * speed
        self.collision('ver')
        self.rect.center = self.hitbox.center
    def update(self):
        if self.tick >= 63:
            self.tick = 0  
        self.tick += 1
        step = math.floor(self.tick / 16)
        debug(step)
        
        
        self.input()
        self.move(self.speed)
        if self.direction.y == -1:
            self.image = pygame.image.load(f'../Graphics/player/up/up_{step}.png')
        elif self.direction.y == 1:
            self.image = pygame.image.load(f'../Graphics/player/down/down_{step}.png')
        elif self.direction.x == -1:
            self.image = pygame.image.load(f'../Graphics/player/left/left_{step}.png')
        elif self.direction.x == 1:
            self.image = pygame.image.load(f'../Graphics/player/right/right_{step}.png')
        
    def damage(self,amount):
        if self.health > 0:
            self.health -= amount
        if self.health <= 0:
            self.health = 0
    
    def heal(self,amount):
        if self.health < self.maxhealth:
            self.health += amount
        if self.health >= self.maxhealth:
            self.health = self.maxhealth
    
    
    def hp_bar(self):
        pygame.draw.rect(screen, (255,0,0), (10,10,self.health,25))
    
    
    def collision(self, direction):
        if direction == 'hor':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == 'ver':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
            