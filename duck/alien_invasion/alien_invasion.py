import sys
import pygame
from random import randint

from settings import Settings
from ship import Ship
from duck import Duck
from points import Points
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from award_text import AwardText
from stage_change import StageChange
import game_function as gf

def run_game():
    # 初始化游戏创建屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Duck Invasion')
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    time_passed = clock.tick(100)
    time_passed_second = time_passed / 1000.0

    #创建一艘飞船
    ship = Ship(screen)
    duck = Duck(screen)
    points = Points(screen)
    play_button = Button(screen,'start')
    stats = GameStats()
    scoreb =Scoreboard(screen,stats)
    award_txt = AwardText(screen)
    stage1_txt = StageChange(screen,'STAGE 1')
    stage2_txt = StageChange(screen, 'STAGE 2')
    stage3_txt = StageChange(screen, 'STAGE 3')
    #开始游戏主循环
    while 1:
        gf.check_events(stats,play_button)
        gf.update_screen(ai_settings,screen,ship,duck,points,play_button,scoreb,stats,award_txt,stage1_txt,stage2_txt,stage3_txt)
        x, y = pygame.mouse.get_pos()
        scoreb.prep_score()

        if stats.game_active:
            pygame.mouse.set_visible(False)
            ship.rect.centerx = x
            duck.move(time_passed_second)
            points.move(time_passed_second)
            if 100<=stats.score<200:
                duck.speed = randint(200,400)
                points.speed = randint(200,400)
            if stats.score>=200:
                duck.speed = randint(300, 450)
                points.speed = randint(300, 450)

        if gf.check_hit(duck, ship):
            stats.game_active = False
            #stats.begin_flag = False
            pygame.mouse.set_visible(True)

        if gf.check_hit(points,ship):
            points.restart()
            stats.score += 10


run_game()
