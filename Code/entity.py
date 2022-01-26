# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 23:34:53 2022

@author: starg
"""

import pygame
from settings import *
import random


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../Graphics/monsters/raccoon/idle/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        self.health = 200
    
    
    def input(self):
        self.direction.x = random.randrange(-1,1)
        self.direction.y = random.randrange(-1,1)
    
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('hor')
        self.hitbox.y += self.direction.y * speed
        self.collision('ver')
        self.rect.center = self.hitbox.center
        
    def update(self):
        self.input()
        self.move(self.speed)
        
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
        
        
        
        
    
    
    