import pygame
from pygame.locals import *
from sys import exit
from random import randrange, choice

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
mid = (125,125,125)
colors = [green, red, blue,mid]
color_change = 1
font_size = 8

fps =144

screen_width = 1080
screen_height = 720

obj_list = []
repeat_list = []
number_of_obj = 20
generate = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Matrix Rain')
font = pygame.font.SysFont('arial',font_size, True, True)

characters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','w','y',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             '0','1','2','3','4','5','6','7','8','9','~','`','!','@','#','$','%','^','','','','','_','=','-','+','*']

class matrix_rain:
    def __init__(self):
        self.color = green
        self.fill = 1                                            
        self.ypos_list = []
        self.characters_list = []
        self.xpos = randrange(font_size,screen_width + font_size, font_size)
        self.ypos = randrange(0, screen_height+font_size, font_size)
        self.ypos_list.append(self.ypos)

    def draw_codeline(self):
        random_character = choice(characters)
        self.characters_list.append(random_character)

        for msg, y in zip(self.characters_list, self.ypos_list):
            message = f'{msg}'
            text = font.render(message, True, self.color)
            screen.blit(text, (self.xpos, y))

    def desloc_codeline(self):
        if self.ypos > screen_height or len(self.ypos_list) > 20:
            message = ' '
            text = font.render(message, True,white)
            screen.fill(black,(self.xpos, self.ypos_list[0], text.get_width() + font_size, text.get_height()* self.fill))
            if text.get_height() * self.fill > len(self.ypos_list) * text.get_height():
                self.characters_list.clear()
            else:
                self.fill += 1

        else:
            self.ypos += font_size
            self.ypos_list.append(self.ypos)
            message = f'{self.characters_list[-1]}'
            text = font.render(message, True,white)
            screen.fill(black, (self.xpos, self.ypos_list[-1], text.get_width()+font_size, text.get_height()))
            screen.blit(text, (self.xpos, self.ypos_list[-1]))

def create_multiples_obj(obj_list, number_of_obj, generate):
    if generate:
        for i in range(number_of_obj):
            obj = matrix_rain()
            if obj.xpos in repeat_list or obj.ypos > screen_height:
                repeat_list.remove(obj.xpos)
                obj.characters_list.clear()
                del obj
            else:
                obj_list.append(obj)
                repeat_list.append(obj.xpos)
        for i in obj_list:
            i.color = colors[color_change]
            i.draw_codeline()
            i.desloc_codeline()
    else:
        for i in obj_list:
            i.color = colors[color_change]
            i.draw_codeline()
            i.desloc_codeline()

clock = pygame.time.Clock()
initial_time = 0
current_time = 0
color_time = 0

while True:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    current_time = pygame.time.get_ticks()

    if current_time - color_time > 1000:                      #change color duration
        color_change = (color_change + 1) % len(colors)
        color_time = pygame.time.get_ticks()

    if current_time - initial_time >1000:                     # start displaying
        generate = True
        initial_time = pygame.time.get_ticks()

    create_multiples_obj(obj_list, number_of_obj, generate)

    pygame.display.flip()