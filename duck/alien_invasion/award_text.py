import pygame

class AwardText():
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('arial', 40)
        self.text = 'YOU ARE MY FAVOURITE DUCK IN THE WORLD'
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.centerx = self.screen_rect.centerx
        self.text_rect.centery = self.screen_rect.centery - 60

    def blitme(self):
        self.screen.blit(self.text_image, self.text_rect)