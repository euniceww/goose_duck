import pygame
from random import randint

class Duck():
    def restart(self):
        self.rect.centerx = randint(100, 700)
        self.rect.centery = randint(0, 300)
        self.speed = randint(100, 400)

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/duck.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.restart()

    def move(self, passed_time_second):
        if self.rect.centery < 650:
            self.rect.centery += self.speed * passed_time_second
        else:
            self.restart()

    def blitme(self):
        '''在指定位置绘制duck'''
        self.screen.blit(self.image,self.rect)