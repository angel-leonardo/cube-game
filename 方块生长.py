# Author by lvanqi
import pygame  # 预处理
import random
import datetime

Game_size = (1200, 850)  # 游戏大小
FPS = 60  # 游戏帧数
clock = pygame.time.Clock()  # 游戏计时


class Gift(object):  # 蓝方块类
    def __init__(self, x_g, y_g, v_y, size_g):
        self.x = x_g
        self.y = y_g
        self.size = size_g
        self.vy = v_y

    def rankup(self, x0, y0, rank0):  # 加分
        if (self.x + self.size - x0) * (self.x - (x0 + rank0)) < 0 and (self.y + self.size - y0) * (
                self.y - (y0 + rank0)) < 0:
            return True
        else:
            return False

    def hamiton(self):  # 运动
        return Gift(self.x, self.y + self.vy, self.vy + 1, self.size)


class Foe(object):  # 红方块类
    def __init__(self, x_g, y_g, v_x, size_g):
        self.x = x_g
        self.y = y_g
        self.size = size_g
        self.vx = v_x

    def death(self, x0, y0, rank0):  # 死亡
        if (self.x + self.size - x0) * (self.x - (x0 + rank0)) < 0 and (self.y + self.size - y0) * (
                self.y - (y0 + rank0)) < 0:
            return True
        else:
            return False

    def hamiton(self):  # 运动
        return Foe(self.x + self.vx, self.y, self.vx, self.size)


def initGame():  # 游戏主体
    rank = 20  # 初始化过程
    pygame.init()
    screen = pygame.display.set_mode(Game_size)
    hua_shu = pygame.font.Font('FZSTK.TTF', 30)
    pygame.display.set_caption('小游戏      by吕安祺')
    rankup_sound = pygame.mixer.Sound('ru_sound.mp3')
    bg = pygame.image.load('startbp.jpg')
    helpbg = pygame.image.load('help.jpg')
    cbg = pygame.image.load('credits.jpg')
    egg = pygame.image.load('eggpic.jpg')
    bg1 = pygame.transform.scale(bg, Game_size)
    helpbg1 = pygame.transform.scale(helpbg, Game_size)
    cbg1 = pygame.transform.scale(cbg, Game_size)
    egg1 = pygame.transform.scale(egg, Game_size)
    starttext1 = hua_shu.render('单击空格开始游戏', True, (255, 0, 0))
    starttext2 = hua_shu.render('单击h显示玩法', True, (255, 0, 0))
    starttext3 = hua_shu.render('单击q退出游戏', True, (255, 0, 0))
    starttext4 = hua_shu.render('单击r查看积分榜', True, (255, 0, 0))
    starttext5 = hua_shu.render('单击c制作者名单', True, (255, 0, 0))
    eggstarttext = hua_shu.render('欢迎来到鬼畜关卡', True, (255, 0, 0))
    textexchange = hua_shu.render('来到了未知领域呢！', True, (255, 0, 0))
    textegg = hua_shu.render('行到水穷处，坐看云起时', True, (0, 0, 0))
    screen.blit(bg1, (0, 0))
    screen.blit(starttext1, (500, 350))
    screen.blit(starttext2, (500, 450))
    screen.blit(starttext3, (500, 550))
    screen.blit(starttext4, (500, 650))
    screen.blit(starttext5, (500, 750))
    pygame.display.flip()
    pygame.mixer.music.load('startmusic.mp3')
    pygame.mixer.music.play(-1)
    egg_m = 0
    egg_count = 0
    l_str_rank = []
    with open(file='rank.txt', mode='r', encoding='utf-8') as rfb:
        l_rank = rfb.read().split('\n')
    for i in l_rank:
        l_str_rank.append(hua_shu.render(i, True, (0, 0, 0)))
    for i in range(10):
        l_rank[i] = l_rank[i].split()
    l_rank = list(map(lambda x: [int(x[0]), x[1], x[2], x[3]], l_rank))
    initbool = False
    endbool = False
    while not initbool:  # 游戏开始画面
        helpbool = False
        screen.blit(bg1, (0, 0))
        screen.blit(starttext1, (500, 350))
        screen.blit(starttext2, (500, 450))
        screen.blit(starttext3, (500, 550))
        screen.blit(starttext4, (500, 650))
        screen.blit(starttext5, (500, 750))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 彩蛋触发
                screen.fill((255, 255, 255))
                screen.blit(textexchange, (500, 400))
                egg_m = 1
            if event.type == pygame.KEYDOWN:
                if event.key == 32:  # 开始游戏
                    screen.fill((255, 255, 255))
                    egg_m = 0
                    initbool = True
                    pygame.display.update()
                    break
                elif event.key == 104:  # 帮助界面
                    screen.blit(helpbg1, (0, 0))
                    pygame.display.update()
                    while not helpbool:
                        for eventh in pygame.event.get():
                            if eventh.type == pygame.QUIT:  # 退出
                                exit()
                            if eventh.type == pygame.KEYDOWN:
                                if eventh.key == 32:  # 开始游戏
                                    screen.fill((255, 255, 255))
                                    egg_m = 0
                                    helpbool = True
                                    initbool = True
                                    pygame.display.update()
                                    break
                                elif eventh.key == 98:  # 返回循环
                                    helpbool = True
                                    break
                elif event.key == 113:  # 退出
                    exit()
                elif event.key == 99:  # 制作人名单
                    screen.blit(cbg1, (0, 0))
                    pygame.display.update()
                    while not helpbool:
                        for eventh in pygame.event.get():
                            if eventh.type == pygame.QUIT:
                                exit()
                            if eventh.type == pygame.KEYDOWN:
                                if eventh.key == 98:  # 返回
                                    helpbool = True
                                    break
                elif event.key == 114:  # 积分榜画面
                    screen.fill((255, 255, 255))
                    screen.blit(hua_shu.render('积分榜', True, (0, 0, 0)), (0, 0))
                    screen.blit(hua_shu.render('按b返回', True, (0, 0, 0)), (0, 700))
                    for i in range(len(l_str_rank)):
                        screen.blit(l_str_rank[i], (0, 100 + 50 * i))
                    pygame.display.update()
                    while not helpbool:
                        for eventh in pygame.event.get():
                            if eventh.type == pygame.QUIT:
                                exit()
                            if eventh.type == pygame.KEYDOWN:
                                if eventh.key == 98:  # 返回
                                    helpbool = True
                                    break
            if event.type == pygame.MOUSEBUTTONUP:  # 彩蛋终止
                screen.fill((255, 255, 255))
                egg_m = 0
                initbool = True
                pygame.display.update()
                break
            if egg_m == 1:  # 彩蛋进行
                egg_count += 1
                pygame.draw.line(screen, (0, 0, 255), (100, 800), (100 + egg_count // 10, 800), 10)
                if egg_count >= 10000:
                    screen.fill((255, 255, 255))
                    screen.blit(eggstarttext, (500, 400))
                    pygame.display.update()
                    initbool = True
                    break
            pygame.display.update()
    if egg_m == 1:  # 彩蛋界面
        screen.blit(egg1, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    screen.fill((255, 255, 255))
                    screen.blit(textegg, (550, 400))
                pygame.display.update()
    else:  # 游戏主循环
        dead = False
        l_gift = []
        l_foe = []
        pygame.draw.line(screen, (0, 0, 0), (0, 600), (Game_size[0], 600), 2)
        pygame.draw.line(screen, (255, 0, 0), (0, 600), (0, 0), 2)
        pygame.draw.line(screen, (255, 0, 0), (Game_size[0], 0), (Game_size[0], 600), 2)
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (Game_size[0], 0), 2)
        x_set = Game_size[0] // 2 - 10
        h_set = 600 - rank
        vx, vh = 0, 0
        pygame.mixer.init()
        pygame.mixer.music.load('bgm1demo.mp3')
        pygame.mixer.music.play(-1)
        pygame.draw.rect(screen, (0, 0, 0), (x_set, h_set, rank, rank))
        while True:
            if dead:  # 死亡判断
                break
            clock.tick(FPS)  # 初始化运行模块
            porpu1, porpu2 = random.randint(1, 100), random.randint(1, 100)
            if porpu1 < 5:
                l_gift.append(Gift(random.randint(0, Game_size[0]), 0, 0, random.randint(3, 5)))
            if porpu2 < 2:
                l_foe.append(Foe(0, random.randint(0, 600 - 11), random.randint(1, 5), random.randint(5, 10)))
            pygame.draw.rect(screen, (255, 255, 255), (x_set, h_set, rank, rank))  # 画面重置模块
            pygame.draw.rect(screen, (255, 255, 255), (0, 800, Game_size[0], Game_size[1] - 800))
            for i in l_gift:
                pygame.draw.rect(screen, (255, 255, 255), (i.x, i.y, i.size, i.size))
            for i in l_foe:
                pygame.draw.rect(screen, (255, 255, 255), (i.x, i.y, i.size, i.size))
            pygame.draw.line(screen, (255, 0, 0), (0, 600), (0, 0), 2)
            pygame.draw.line(screen, (255, 0, 0), (Game_size[0] - 2, 0), (Game_size[0] - 2, 600), 2)
            pygame.draw.line(screen, (255, 0, 0), (0, 0), (Game_size[0], 0), 2)
            x_set += vx  # 运动加载模块
            h_set += vh
            for i in range(len(l_gift)):
                l_gift[i] = l_gift[i].hamiton()
            for i in range(len(l_foe)):
                l_foe[i] = l_foe[i].hamiton()
            if h_set < 600 - rank:
                vh += 1
            i = 0
            while i < len(l_gift):  # 碰撞判断模块
                if l_gift[i].rankup(x_set, h_set, rank):
                    rankup_sound.play()
                    rank += l_gift[i].size
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (l_gift[i].x, l_gift[i].y, l_gift[i].size, l_gift[i].size))
                    del l_gift[i]
                else:
                    i += 1
            while i < len(l_foe):
                if l_foe[i].death(x_set, h_set, rank):
                    dead = True
                    break
                else:
                    i += 1
            if x_set + rank > Game_size[0] or x_set < 0 or h_set < 0:
                dead = True
            for event in pygame.event.get():  # 接受输入模块
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    char = event.key
                    if char == pygame.K_LEFT:
                        vx = -5
                    elif char == pygame.K_RIGHT:
                        vx = 5
                    elif char == 32:
                        vh = -8
                if event.type == pygame.KEYUP:
                    char = event.key
                    if (char == pygame.K_LEFT and vx < 0) or (char == pygame.K_RIGHT and vx > 0):
                        vx = 0
            if h_set > 600 - rank:  # 清除与重置模块
                vh = 0
                h_set = 600 - rank
            i = 0
            while i < len(l_gift):
                if l_gift[i].y + l_gift[i].size > 600:
                    del l_gift[i]
                else:
                    i += 1
            i = 0
            while i < len(l_foe):
                if l_foe[i].x + l_foe[i].size > Game_size[0]:
                    del l_foe[i]
                else:
                    i += 1
            ranktest = hua_shu.render('你的大小：' + str(rank), True, (0, 255, 0))  # 积分
            pygame.draw.rect(screen, (0, 0, 0), (x_set, h_set, rank, rank))  # 画面渲染模块
            for i in l_gift:
                pygame.draw.rect(screen, (0, 0, 255), (i.x, i.y, i.size, i.size))
            for i in l_foe:
                pygame.draw.rect(screen, (255, 0, 0), (i.x, i.y, i.size, i.size))
            screen.blit(ranktest, (0, 800))
            pygame.display.update()
    pygame.mixer.init()  # 结束初始化
    t = datetime.datetime.now()
    t = t.strftime("%Y-%m-%d %H:%M:%S")
    pygame.mixer.music.load('endmusicdddemo.mp3')
    pygame.mixer.music.play(-1)
    if rank > l_rank[9][0]:  # 达到积分榜的画面
        rank_str = ''
        while not endbool:
            endtext = hua_shu.render('游戏结束，你的大小是：' + str(rank), True, (0, 255, 0))
            screen.fill((255, 255, 255))
            screen.blit(endtext, (400, 400))
            screen.blit(hua_shu.render('恭喜进入积分榜！', True, (255, 0, 0)), (400, 500))
            screen.blit(hua_shu.render('键入你的感想(暂不支持中文):' + rank_str, True, (255, 0, 0)), (400, 600))
            pygame.display.update()
            for event in pygame.event.get():  # 写入感想
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        endbool = True
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        if rank_str != '':
                            rank_str = rank_str[0: len(rank_str) - 1]
                    else:
                        try:
                            rank_str = rank_str + chr(event.key)
                        except:
                            pass
        l_rank.append([rank, t, rank_str])  # 重置与写入积分榜
        l_rank.sort(key=lambda x: x[0], reverse=True)
        del l_rank[-1]
        for i in range(10):
            l_rank[i][0] = str(l_rank[i][0])
            l_rank[i] = ' '.join(l_rank[i])
        with open(file=r'rank.txt', mode='w', encoding='utf-8') as rwfb:
            rwfb.write('\n'.join(l_rank))
    else:  # 未达积分榜画面（未测试）
        while True:
            endtext = hua_shu.render('游戏结束，你的大小是：' + str(rank), True, (0, 255, 0))
            screen.fill((255, 255, 255))
            screen.blit(endtext, (400, 400))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


initGame()
