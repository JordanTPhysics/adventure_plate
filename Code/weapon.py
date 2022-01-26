# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:36:31 2022

@author: starg
"""

import pygame
weapon_image = pygame.image.load('../Graphics/weapons/lance/right.png')

class Weapon(pygame.sprite.Sprite):
    def __init__(self, w_type, damage, w_range, pos):
        self.image = weapon_image
        self.damage = damage
        
        
        
        
