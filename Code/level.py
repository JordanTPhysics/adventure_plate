# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 22:28:08 2022

@author: starg
"""

import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from entity import Entity

class Level:
    def __init__(self):
        
        
        self.display_surface = pygame.display.get_surface()
        #sprite groups setup
        
        self.visible_sprites = YCamGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.init_map()
    
    
    
    def init_map(self):
        for idx_row, row in enumerate(WORLD_MAP):
            for idx_col, col in enumerate(row):
                x = idx_col*TILESIZE
                y = idx_row*TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                if col == 'e':
                    self.entity = Entity((x,y),[self.visible_sprites],self.obstacle_sprites)
                    
                
                
    def run(self):
        #draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.custom_draw(self.entity)
        self.visible_sprites.update()
        #debug(self.player.direction)
        
class YCamGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.halfw = self.display_surface.get_width() //2
        self.halfh = self.display_surface.get_height() //2
        
    def custom_draw(self,player):
        
        self.offset.x = player.rect.centerx - self.halfw
        self.offset.y = player.rect.centery - self.halfh
        
        
        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery ):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_rect)
            
# class GameState():
#     def __init__(self):
#         self.state = 'main_game'   

#     def main_game(self):  
            
            