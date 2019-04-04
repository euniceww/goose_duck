import pygame
import sys


def check_events(stats,play_button):
    '''响应按键和鼠标事件'''
    # 监视键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)

def check_play_button(stats,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        stats.game_active = True
        stats.reset_stats()
        #stats.begin_flag = True

def update_screen(ai_settings,screen,ship,duck,points,play_button,scoreboard,stats,award_txt,stage1_txt,stage2_txt,stage3_txt):
    '''更新屏幕图像'''
    # 每次循环都重绘屏幕填色
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    duck.blitme()
    points.blitme()
    scoreboard.show_score()
    if not stats.game_active and not stats.stage_change:
        play_button.draw_button()

    if stats.score > 300:
        award_txt.blitme()

    #绘制三个stage标志
    if stats.score >=0 and stats.stage1_flag < 300 : #and stats.begin_flag :
        stage1_txt.blitme()
        stats.stage1_flag += 1
        stats.game_active = False
        stats.stage_change = True
    if stats.stage1_flag == 300: #and stats.begin_flag:
        stats.game_active = True
        stats.stage1_flag = 301
        stats.stage_change = False

    if stats.score >=100 and stats.stage2_flag < 300 :
        stage2_txt.blitme()
        stats.stage2_flag += 1
        stats.game_active = False
        stats.stage_change = True
    if stats.stage2_flag == 300:
        stats.game_active = True
        stats.stage2_flag = 301
        stats.stage_change = False

    if stats.score >=200 and stats.stage3_flag < 300 :
        stage3_txt.blitme()
        stats.stage3_flag += 1
        stats.game_active = False
        stats.stage_change = True
    if stats.stage3_flag == 300:
        stats.game_active = True
        stats.stage3_flag = 301
        stats.stage_change = False

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def check_hit(object,goose):
    if goose.rect.y + goose.image.get_height()>(object.rect.y + object.image.get_height())>goose.rect.y\
    and goose.rect.x<object.rect.centerx<goose.rect.x+goose.image.get_width():
        return True
    else:
        return False

