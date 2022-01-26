# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 22:12:12 2022

@author: starg
"""

import pygame, sys
from settings import *
from level import Level
class Game:
    def __init__(self):
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Zelda game')
        self.clock = pygame.time.Clock()
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill(BACKGROUND)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
            
            
            
if __name__ == '__main__':
    game = Game()
    game.run()