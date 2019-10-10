import pygame
from os import path
import os
from newsettings import *
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.init()
game_folder = os.path.dirname(__file__)
resources_folder = os.path.join(game_folder, 'resources')
family_img = pygame.image.load(os.path.join(resources_folder, 'family_member.png')).convert()
money_img = pygame.image.load(os.path.join(resources_folder, 'money.png')).convert()
food_img = pygame.image.load(os.path.join(resources_folder, 'food.png')).convert()
education_img = pygame.image.load(os.path.join(resources_folder, 'education.png')).convert()
player_img = pygame.image.load(os.path.join(resources_folder, 'player.png')).convert()
food_station_img = pygame.image.load(os.path.join(resources_folder, 'food_station.png')).convert()
work_img = pygame.image.load(os.path.join(resources_folder, 'work.png')).convert()
school_img = pygame.image.load(os.path.join(resources_folder, 'school.png')).convert()
all_sprites = pygame.sprite.Group()
player = pygame.sprite.Group()

class Console(pygame.sprite.Sprite):
    def __init__(self, game, x):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.width = WIDTH
        self.height = HEIGHT
        self.surface = pygame.Surface((2 * self.width, 2 * self.height))
        self.surface.fill(WHITE)
        self.surface.set_colorkey(WHITE)
        pygame.draw.rect(self.surface, RED, [0, 200, 1075, 500])
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.rect.x = x

class Family(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = family_img
        self.image.set_colorkey(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Money(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = money_img
        self.image.set_colorkey(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Food(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = food_img
        self.image.set_colorkey(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Education(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = education_img
        self.image.set_colorkey(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
