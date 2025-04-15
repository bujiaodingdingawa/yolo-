import pygame
import sys
import socket
import cv2
import numpy as np
import time

# ----------------------------------初始化----------------------------------

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

foo0 = [0, 0]
np.savetxt("G:/danmuchuanshu.txt", foo0, fmt='%d', delimiter=',')
dets1 = np.loadtxt("G:\danmuchuanshu.txt", delimiter=',')
print(dets1[0], dets1[1])

str0 = ['&', '@']
global ss
ss = [0, 0]
global yy
yy = [0, 0]
global zz
zz = 0
status = 0
done = False
# ---------------------------------------------------------------------------


# -----------------------连接函数--------------------------------

HOST = '192.168.137.1'
PORT = 8888  # 设置端口号，自己设置即可
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
global connection
connection, address = s.accept()  # 接收客户端的连接请求
try:
    connection.settimeout(10)  # 设置10s时限
    buf = connection.recv(1024)  # 接收数据实例化
    if buf:  # 接收成功
        connection.send(b'welcome to server!')  # 发送消息，b表示bytes类型
        print('Connection success!')
    else:  # 接收失败
        connection.send(b'Please go out!')
except socket.timeout:  # 超时
    print('time out!')


# ----------------------------------------------------------


def sendzuobiao():
    dets = np.loadtxt("G:\chuanshu.txt")
    if dets[0] < 300 and dets[1] < 400:
        for i in range(len(dets)):
            sta = str0[i] + str(dets[i])
            print(sta)
            connection.send(sta.encode("utf-8"))
            time.sleep(0.01)


def senddanmu():
    foo0 = [0, 0]
    np.savetxt("G:/shuangmuchuanshu.txt", foo0, fmt='%d', delimiter=',')
    sta1 = 'lgo'  # 停止旋转
    connection.send(sta1.encode("utf-8"))
    time.sleep(0.8)
    sta2 = 'lgo'
    connection.send(sta2.encode("utf-8"))
    time.sleep(0.8)
    sta3 = 'lspeedup'
    connection.send(sta3.encode("utf-8"))
    time.sleep(0.8)
    sta4 = 'lspeedup'
    connection.send(sta4.encode("utf-8"))
    time.sleep(0.3)
    sta5 = 'lspeedup'
    connection.send(sta5.encode("utf-8"))


def sendshuangmu():
    sta1 = 'lgo'  # 停止旋转
    connection.send(sta1.encode("utf-8"))
    time.sleep(0.3)
    sta1 = '!'
    connection.send(sta1.encode("utf-8"))
    sendzuobiao()
    foo0 = [0, 0]
    np.savetxt("G:/danmuchuanshu.txt", foo0, fmt='%d', delimiter=',')


# cap1 = cv2.VideoCapture(2)
# cap2 = cv2.VideoCapture(1)


while done == False:
    # 事件处理的步骤
    for event in pygame.event.get():  # 用户要做的事情（键盘事件...）
        if event.type == pygame.QUIT:  # 如果用户触发了关闭事件
            done = True  # 设置我们做了这件事的标志，所以我们就可以退出循环了
    # ret1,frame1 = cap1.read()
    # image1 = cv2.imencode('.png', frame1)[1].tobytes()
    # window['image1'].update(data=image1)

    # ret2,frame2 = cap2.read()
    # image2 = cv2.imencode('.png', frame2)[1].tobytes()
    # window['image2'].update(data=image2)

    # data = connection.recv(1024).decode('utf-8')
    # print(data)
    # window['depth-value'].update(data)
    # -------------------------手柄信息处理------------------------------

    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # 摇杆输入
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
        # 方向盘输入
        hats = joystick.get_numhats()
        for i in range(hats):
            hat = joystick.get_hat(i)
            if hat == (0, 1):  # 站
                print("stand")
                sta = 'stand'
                connection.send(sta.encode("utf-8"))
            if hat == (0, -1):  # 趴
                print("down")
                sta = 'down'
                connection.send(sta.encode("utf-8"))
            if hat == (-1, 0):  # 注射伸
                print("push")
                sta = 'push'
                connection.send(sta.encode("utf-8"))
            if hat == (1, 0):  # 注射缩
                print("back")
                sta = 'back'
                connection.send(sta.encode("utf-8"))

        # 按钮输入
        buttons = joystick.get_numbuttons()
        for i in range(buttons):
            if i == 3 and joystick.get_button(i) == 1:  # UM前进
                print("UY_up")
                sta = 'UY_up'
                connection.send(sta.encode("utf-8"))
            if i == 0 and joystick.get_button(i) == 1:  # UM后退
                print("UY_down")
                sta = 'UY_down'
                connection.send(sta.encode("utf-8"))
            if i == 2 and joystick.get_button(i) == 1:  # UM左移
                print("UX_left")
                sta = 'UX_left'
                connection.send(sta.encode("utf-8"))
            if i == 1 and joystick.get_button(i) == 1:  # UM右移
                print("UX_right")
                sta = 'UX_right'
                connection.send(sta.encode("utf-8"))
            if i == 9 and joystick.get_button(i) == 1:  # 药液排出
                print("Discharge")
                sta1 = 'Discharge'
                connection.send(sta1.encode("utf-8"))
            if i == 8 and joystick.get_button(i) == 1:  #
                print("long")
                sta = 'suction'
                connection.send(sta.encode("utf-8"))
            if i == 6 and joystick.get_button(i) == 1:  #
                print("zidongzhushe")
                sendzuobiao()
            if i == 7 and joystick.get_button(i) == 1:  # UM停
                print("U_stop")
                sta = 'U_stop'
                connection.send(sta.encode("utf-8"))
            if i == 4 and joystick.get_button(i) == 1:  # 舵机复位
                print("Servo_reset")
                sta = 'Servo_reset'
                connection.send(sta.encode("utf-8"))
            if i == 5 and joystick.get_button(i) == 1:  # 舵机垂直
                print("Servo_vertical")
                sta = 'Servo_vertical'
                connection.send(sta.encode("utf-8"))
    clock.tick(6)

# -------------------------------------------------------------


pygame.quit()
# window.close()

''' 
        # 方向盘输入
        hats = joystick.get_numhats()
        for i in range(hats):
            hat = joystick.get_hat(i)
            if hat == (0,1):                                  #履带启停
                print("lgo")
                sta = 'lgo'
                connection.send(sta.encode("utf-8"))
            elif hat == (0,-1):                               #履带后退
                print("lback")
                sta = 'lback'
                connection.send(sta.encode("utf-8"))
            elif hat == (-1,0):                               #履带左转
                print("lleft")
                sta = 'lleft'
                connection.send(sta.encode("utf-8"))
            elif hat == (1,0):                                #履带右转
                print("lright")
                sta = 'lright'
                connection.send(sta.encode("utf-8"))

        #按钮输入
        buttons = joystick.get_numbuttons()
        for i in range(buttons):
            if i == 9 and joystick.get_button(i) == 1:        #切换模式
                if status == 1:
                    status = 0
                    print("切换模式")
                elif status == 0:
                    status = 1
                    print("切换模式")
            if status == 0:
                if i == 4 and joystick.get_button(i) == 1:    # 履带加速
                     print("sdown")
                     sta = 'lspeedup'
                     connection.send(sta.encode("utf-8"))
                elif i == 5 and joystick.get_button(i) == 1:  # 履带减速
                     print("sup")
                     sta = 'lspeeddown'
                     connection.send(sta.encode("utf-8"))
                elif i == 6 and joystick.get_button(i) == 1:  # 气囊打开
                     print("airopen")
                     sta = 'airopen'
                     connection.send(sta.encode("utf-8"))
                elif i == 7 and joystick.get_button(i) == 1:  # 气囊关闭
                     print("airclose")
                     sta = 'airclose'
                     connection.send(sta.encode("utf-8"))
                elif i == 0 and joystick.get_button(i) == 1:  # 自动巡路
                     sta = 'lgo'
                     connection.send(sta.encode("utf-8"))
                     time.sleep(0.5)
                     sta = 'lleft'
                     connection.send(sta.encode("utf-8"))
                     while ss[0] == ss[1]:
                        try:
                            dets11 = np.loadtxt("G:\danmuchuanshu.txt", delimiter=',')
                            print(dets11[0], dets11[1])
                        except IndexError:
                            continue
                        ss[1] = ss[0]
                        ss[0] = dets11[0]
                     senddanmu()
                     while yy[0] == yy[1]:
                        try:
                            dets22 = np.loadtxt("G:\shuangmuchuanshu.txt", delimiter=',')
                            print(dets22[0], dets22[1])
                        except IndexError:
                            continue
                        yy[1] = yy[0]
                        yy[0] = dets22[0]
                     time.sleep(0.5)
                     sendshuangmu()
                elif i == 1 and joystick.get_button(i) == 1:  # 一键调试
                    print("alltest")
                    sta = 'alltest'
                    connection.send(sta.encode("utf-8"))
                elif i == 2 and joystick.get_button(i) == 1:  # 一键补药
                    t = t - 1
                elif i == 3 and joystick.get_button(i) == 1:  # 自动注射
                    sendzuobiao()

            elif status == 1:
                if i == 5 and joystick.get_button(i) == 1:    # 推杆伸长/缩短
                    print("long&short")
                    sta = 'long&short'
                    connection.send(sta.encode("utf-8"))
                elif i == 4 and joystick.get_button(i) == 1:  # 舵机垂直/复位
                    print("reset&vertical")
                    sta = 'reset&vertical'
                    connection.send(sta.encode("utf-8"))
                elif i == 3 and joystick.get_button(i) == 1:  # UM前进
                    print("umgo")
                    sta = 'umgo'
                    connection.send(sta.encode("utf-8"))
                elif i == 0 and joystick.get_button(i) == 1:  # UM后退
                    print("umback")
                    sta = 'umback'
                    connection.send(sta.encode("utf-8"))
                elif i == 2 and joystick.get_button(i) == 1:  # UM左移
                    print("umleft")
                    sta = 'umleft'
                    connection.send(sta.encode("utf-8"))
                elif i == 1 and joystick.get_button(i) == 1:  # UM右移
                    print("umright")
                    sta = 'umright'
                    connection.send(sta.encode("utf-8"))
                elif i == 7 and joystick.get_button(i) == 1:  # 推杆停止
                    print("Rodstop")
                    sta1 = 'Rodstop'
                    connection.send(sta1.encode("utf-8"))
                elif i == 8 and joystick.get_button(i) == 1:  # UM停止
                    print("umstop")
                    sta1 = 'umstop'
                    connection.send(sta1.encode("utf-8"))
                elif i == 6 and joystick.get_button(i) == 1:  # 泵吸入/排出
                    print("suc&dis")
                    sta1 = 'suc&dis'
                    connection.send(sta1.encode("utf-8"))

    clock.tick(6)

pygame.quit()
'''
