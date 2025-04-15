import PySimpleGUI as sg
import pygame
import sys
import socket
import cv2
import numpy as np
import time
#----------------------------------初始化----------------------------------


pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
str0=['@', '&', '^']
done = False

#---------------------------------------------------------------------------


#-----------------------连接函数--------------------------------
'''
HOST = '0.0.0.0'
PORT = 8002  # 设置端口号，自己设`置即可
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
'''
#----------------------------------------------------------



def send():
    dets = np.loadtxt("G:\chuanshu.txt", delimiter='/n')
    for i in range (len(dets)) :
        print(dets[i])
        sta = str0[i] + str(dets[i])
        #connection.send(sta.encode("utf-8"))
        time.sleep(0.01)

def deadArea(value):
    if(abs(value)>0.15): return value
    else: return 0

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




    #data = connection.recv(1024).decode('utf-8')
    #window['depth-value'].update(data+"      ")
#---------------------------------



#-------------------------手柄信息处理------------------------------

    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        #摇杆输入
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)

        # 方向盘输入

        buttons = joystick.get_numbuttons()
        for i in range(buttons):
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
                #sta = 'sup'
                #connection.send(sta.encode("utf-8"))
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
                # sta = 'lspeeddown'
                # connection.send(sta.encode("utf-8"))

        # 按钮输入
    clock.tick(2)

#-------------------------------------------------------------


pygame.quit()

