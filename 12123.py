import pygame



# 这是一个简单的类，将帮助我们打印到屏幕上。它与操纵杆无关，只是输出信息。



pygame.init()



# 保持循环直到用户点击关闭按钮
done = False

# 被用来管理屏幕更新的速度
clock = pygame.time.Clock()

# 初始化joystick
pygame.joystick.init()

# 准备好打印

# -------- 程序主循环 -----------
while done == False:
    # 事件处理的步骤
    for event in pygame.event.get():  # 用户要做的事情（键盘事件...）
        if event.type == pygame.QUIT:  # 如果用户触发了关闭事件
            done = True  # 设置我们做了这件事的标志，所以我们就可以退出循环了

        #	可能的joystick行为: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    # 绘制的步骤
    # 首先，用白色清除屏幕。不要放其它的绘图指令
    # 在这条上面的指令，将会被擦除

    # 得到joystick的数量
    joystick_count = pygame.joystick.get_count()



    # 在每个joystick中：
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # 从操作系统中获取控制器/joystick的名称


        # 通常轴成对运行，一个轴向上/向下，另一个轴向左/右。
        axes = joystick.get_numaxes()



        buttons = joystick.get_numbuttons()

        hats = joystick.get_numhats()
        for i in range(hats):
            hat = joystick.get_hat(i)
            if hat == (0, 1):  # 履带启停
                print("lgo")
                # sta = 'lgo'
                # connection.send(sta.encode("utf-8"))
            if hat == (0, -1):  # 履带后退
                print("lback")
                # sta = 'lback'
                # connection.send(sta.encode("utf-8"))
            if hat == (-1, 0):  # 履带左转
                print("lleft")
                # sta = 'lleft'
                # connection.send(sta.encode("utf-8"))
            if hat == (1, 0):  # 履带右转
                print("lright")
                # sta = 'lright'
                # connection.send(sta.encode("utf-8"))
            if hat == (-1, 1):  # 履带加速
                print("lspeedup")
                # sta = 'lspeedup'
                # connection.send(sta.encode("utf-8"))
            if hat == (1, 1):  # 履带减速
                print("lspeeddown")

        for i in range(buttons):
            #button = joystick.get_button(i)
            if i == 3 and joystick.get_button(i) == 1:      #UM前进
                print("umgo")
                #sta = 'umgo'
                #connection.send(sta.encode("utf-8"))
            if i == 0 and joystick.get_button(i) == 1:      #UM后退
                print("umback")
                #sta = 'umback'
                #connection.send(sta.encode("utf-8"))
            if i == 2 and joystick.get_button(i) == 1:      #UM左移
                print("umleft")
                #sta = 'umleft'
                #connection.send(sta.encode("utf-8"))
            if i == 1 and joystick.get_button(i) == 1:      #UM右移
                print("umright")
                #sta = 'umright'
                #connection.send(sta.encode("utf-8"))
            if i == 9 and joystick.get_button(i) == 1:      #UM停止&&推杆停止
                print("umstop && Rodstop")
                #sta1 = 'umstop'
                #connection.send(sta1.encode("utf-8"))
                #sta2 = 'Rodstop'
                #connection.send(sta2.encode("utf-8"))
            if i == 8 and joystick.get_button(i) == 1:      #推杆注射回收
                print("long")
                #sta = 'long'
                #connection.send(sta.encode("utf-8"))
            if i == 6 and joystick.get_button(i) == 1:      #泵开启
                print("opshot")
                #sta = 'opshot'
                #connection.send(sta.encode("utf-8"))
            if i == 7 and joystick.get_button(i) == 1:      #泵吸入
                print("clshot")
                #sta = 'clshot'
                #connection.send(sta.encode("utf-8"))
            if i == 4 and joystick.get_button(i) == 1:      #舵机下旋
                print("sdown")
                #sta = 'sdown'
                #connection.send(sta.encode("utf-8"))
            if i == 5 and joystick.get_button(i) == 1:      #舵机上旋
                print("sup")

        # 帽子开关。完全或完全没有方向，不像操纵杆。
        # 值在数组中返回



    # 所有绘图的指令必须在这一条前面

    # 向前运行，并更新屏幕

    # 限制每秒20帧
    clock.tick(20)

# 关闭窗口并退出.
# 如果你忘记这行，程序会被挂起，如果它从IDLE中运行的话
# （通常在IDLE中运行，需要两条退出语句）
# pygame.quit()
# sys.exit()
pygame.quit()