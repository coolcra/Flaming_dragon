import pygame
import random
import math
import os
import time
import sys
from os import path
from newsettings import *
from spritesdata import *
#game elements
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        #i used self.living = 1 to signify that he is still alive...
        self.living = 1
        self.score = 0
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        #get the time
        self.time = pygame.time.get_ticks()
        pygame.key.set_repeat(500, 100)
        self.all_sprites = pygame.sprite.Group()
        #here is where all the images are gonna be drawn
        self.console = Console(self, 0)
        self.food = Food(self, 300, 350)
        self.education = Education(self, 25, 350)
        self.family = Family(self, 800, 350)
        self.money = Money(self, 362, 525)
        #i tried to use food_bar to represent his food, but later decided on using a bar instead
        initial_food = 100
        #food_bar is just the amount of food he has -_-
        self.food_bar = initial_food
        initial_money = 0
        #same goes for money_bar, just the amount of money he has
        self.money_bar = initial_money
        if self.money_bar < 0:
            self.money_bar = 0
        initial_education = 0
        self.education_level = initial_education
        #parents
        initial_family = 3
        self.family_member = 3

    def scorelol(self):
        #heres where i update his score every second by using set_timer()
        self.SCOREEVENT = pygame.USEREVENT - 1
        pygame.time.set_timer(self.SCOREEVENT, 1000)
        self.all_sprites.update()
        pygame.display.flip()

    def run(self):
        #main algorithm running the game
        self.playing = True
        self.hunger()
        self.reproduce()
        self.scorelol()
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.draw()
            self.update()

    def hunger(self):
        #to get his food to decrease every second (not realistic but yeah)
        self.HUNGEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.HUNGEREVENT, 1000)
        self.all_sprites.update()
        pygame.display.flip()

    def reproduce(self):
        #well realistically again not possible to have a child every 10s
        #but to make it more challenging, i did so
        self.REPRODUCEEVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.REPRODUCEEVENT, 10000)
        self.all_sprites.update()
        pygame.display.flip()

    def food_food(self, x, y, cool):
        #here's how I represented my player's food as a bar
        if cool < 0:
            cool = 0
        if cool > 100:
            cool = 100
        BAR_LENGTH = 300
        BAR_HEIGHT = 25
        fill = (cool / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, WHITE, outline_rect, 2)
        #die lor
        if cool == 0:
            self.living = 0
            self.quit()

    def quit(self):
        #quit
        pygame.quit()
        sys.exit()

    def update(self):
        #updates the game
        self.all_sprites.update()


    def draw(self):
        #drawing of the food bar thing, and everything else
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        font = pygame.font.SysFont('Arial', 16, True, False)
        self.food_food(400, 375, self.food_bar)
        #i put my rules on the game page so players can refer to it more easily
        text = font.render("Here are the rules:" , True, BLACK)
        screen.blit(text, [0, 16])
        text = font.render("Press w to earn money 2 x your education level" , True, BLACK)
        screen.blit(text, [0, 32])
        text = font.render("Press f to buy food costing 2 x the number of people in your family" , True, BLACK)
        screen.blit(text, [0, 48])
        text = font.render("Every 10 seconds you will gain 1 family member and every second you lose food which is 5 x the number of people in your family" , True, BLACK)
        screen.blit(text, [0, 64])
        text = font.render("Press e to increase your education level costing 10 x your education level" , True, BLACK)
        screen.blit(text, [0, 80])
        text = font.render("If you run out of food you die, poor thing" , True, BLACK)
        screen.blit(text, [0, 96])
        font = pygame.font.SysFont('Arial', 30, True, False)
        text = font.render("Score: " + str(self.score), True, BLACK)
        screen.blit(text, [0, 300])
        text = font.render("= " + str(self.education_level), True, BLACK)
        screen.blit(text, [125, 390])
        text = font.render("= " + str(self.family_member), True, BLACK)
        screen.blit(text, [900, 390])
        font = pygame.font.SysFont('Arial', 60, True, False)
        text = font.render("= $" + str(self.money_bar), True, BLACK)
        screen.blit(text, [475, 525])
        #update
        self.all_sprites.update()
        pygame.display.flip()

    def events(self):
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == self.HUNGEREVENT:
                #deducts food every second according to number of family members, after all family members need to eat also
                self.food_bar = self.food_bar - 5 * self.family_member
                self.all_sprites.update()
                pygame.display.flip()

            if event.type == self.SCOREEVENT:
                #every 0.1second alive gives you a score of 1. Time is literally time (the variable)
                time = pygame.time.get_ticks()
                #included education level so ppl are more motivated to learn more!
                self.score = time // 100 + self.education_level * 50
                self.all_sprites.update()
                pygame.display.flip()

            if event.type == self.REPRODUCEEVENT:
                #well i dont think anyone can even get to 20, but in case they did i made sure max number of family members < 20 ( you dont want the food to run out before you can replenish it as 5 x 20 = 100)
                if self.family_member < 20:
                    self.family_member = self.family_member + 1
                    self.all_sprites.update()
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                #basically how the guy buys food, cost is 2 x number of family members
                if self.money_bar >= 2 * self.family_member:
                    self.money_bar = self.money_bar - 2 * self.family_member
                    self.food_bar = self.food_bar + 15
                    if self.food_bar > 100:
                        self.food_bar = 100
                    self.all_sprites.update()
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                #working ie gain money :)
                self.money_bar = self.money_bar + 2 * self.education_level
                self.all_sprites.update()
                pygame.display.flip()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                #sets conditions so the guy has no debt or negative money, he pays money to learn also
                if self.money_bar >= 10 * self.education_level:
                    self.money_bar = self.money_bar - 10 * self.education_level
                    self.education_level += 1
                self.all_sprites.update()
                pygame.display.flip()


            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #essentially quitting the game
                self.quit()




    def end_screen(self):
        #end_screen is actually the start screen. I tried to link both together but I ended up with several errors, so I just called it end_screen for fun
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
                    #different modes corresponding to different initial cash, wanted to do different food also but realised hard mode would be literally impossible
                    if event.key == pygame.K_h:
                        #hard mode
                        waiting = False
                        initial_money = 50
                        self.money_bar = 50
                        initial_food = 100
                    if event.key == pygame.K_m:
                        #medium mode
                        waiting = False
                        initial_money = 100
                        self.money_bar = 100
                        initial_food = 100
                    if event.key == pygame.K_e:
                        #easy mode
                        waiting = False
                        initial_money = 200
                        self.money_bar = 200
                        initial_food = 100

#does everything
g = Game()
g.end_screen()
#as i said, end_screen is the start screen
g.run()
