import pygame
import random
import math
import os
import time
import sys
from os import path
from newsettings import *
from spritesdata import *
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.time = pygame.time.get_ticks()
        pygame.key.set_repeat(500, 100)
        self.all_sprites = pygame.sprite.Group()
        self.console = Console(self, 0)
        self.player = Player(self, 390, 595)
        self.work = Work(self, 450, 250)
        self.food_station = Food_Station(self, 750, 200)
        self.food = Food(self, 25, 20)
        self.education = Education(self, 300, 10)
        self.school = School(self, 100, 200)
        self.family = Family(self, 600, 10)
        self.money = Money(self, 800, 15)
        self.food_bar = 100
        initial_money = 0
        self.money_bar = initial_money
        initial_education = "Student"
        self.education_level = initial_education
        initial_family = 3
        self.family_member = 3

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.hunger()
            self.events()
            self.update()
            self.draw()

    def hunger(self):
        HUNGEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(HUNGEREVENT, 1000)
        self.all_sprites.update()
        pygame.display.flip()

    def food_food(self, x, y, cool):
        if cool < 0:
            cool = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (cool / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, WHITE, outline_rect, 2)

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        font = pygame.font.SysFont('Arial', 15, True, False)
        self.food_food(120, 50, self.food_bar)
        text = font.render("Number of days:" , True, BLACK)
        screen.blit(text, [0, 110])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("= " + str(self.education_level), True, BLACK)
        screen.blit(text, [400, 40])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("= " + str(self.family_member), True, BLACK)
        screen.blit(text, [700, 40])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("= $" + str(self.money_bar), True, BLACK)
        screen.blit(text, [900, 40])
        self.all_sprites.update()
        pygame.display.flip()

    def events(self):
        # catch all events here
        HUNGEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(HUNGEREVENT, 10000)
        if pygame.event.get(HUNGEREVENT):
            self.food_bar = self.food_bar - 10
            self.all_sprites.update()
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                if event.key == pygame.K_ESCAPE:
                    self.quit()


    def end_screen(self):
        screen.fill(BLUE)
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("Life Simulator V2" , True, WHITE)
        screen.blit(text, [400, 100])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("Controls: F for food, E for education, W for work", True, WHITE)
        screen.blit(text, [175, 250])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("Hard mode: h    Easy mode: e    Normal mode: m", True, WHITE)
        screen.blit(text, [175, 400])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("Start by pressing a key corresponding to that mode", True, WHITE)
        screen.blit(text, [150, 600])
        pygame.display.flip()
        waiting = True
        while waiting:
            pygame.init()
            clock = pygame.time.Clock()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        waiting = False
                        initial_money = 50
                        self.money_bar = 50
                        self.food_bar = 100
                    if event.key == pygame.K_m:
                        waiting = False
                        initial_money = 100
                        self.money_bar = 100
                        self.food_bar = 100
                    if event.key == pygame.K_e:
                        waiting = False
                        initial_money = 200
                        self.money_bar = 200
                        self.food_bar = 100

g = Game()
g.end_screen()
g.run()
