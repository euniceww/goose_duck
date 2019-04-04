import pygame

class Scoreboard():
    '''记分板'''
    def __init__(self,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        #记分板字体设置
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,48)
        #准备初始得分图像
        self.prep_score()

    def prep_score(self):
        '''将得分转换为一幅渲染图象'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color)
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)

