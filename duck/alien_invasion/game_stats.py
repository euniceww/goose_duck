class GameStats():
    '''游戏的各种状态信息'''
    def __init__(self):
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.score = 0
        self.stage1_flag = 0
        #self.begin_flag = False
        self.stage2_flag = 0
        self.stage3_flag = 0
        self.stage_change = False
