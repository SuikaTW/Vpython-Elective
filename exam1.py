# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *
from visual.graph import *

# 1. 參數設定
g = 9.8  # 加速度
a = vector(0,-g,0)  # 加速度值,在 x、z 方向為 0,在 y 方向為 g=-9.8 公尺/秒^2
ballv = vector(6,10,0)  # 球的 y 方向速度(公尺/秒)
h = 3  # 球的初始高度，單位為公尺
dt = 0.01  # 畫面更新的時間間隔,單位為秒
t = 0  # 模擬所經過的時間 ,單位為秒,初始值為0

# 2. 畫面設定
scene = display(center = (0, h/2, 0), background=(0.5,0.6, 0))
gdyt = gdisplay(x=800, y=0, title='y - t', xtitle='t (s)', ytitle='y (m)', ymax=10, ymin=-10, xmax=100)
gdxt = gdisplay(x=800, y=0, title='x - t', xtitle='t (s)', ytitle='x (m)', ymax=10, ymin=-10, xmax=100)
yt = gcurve(gdisplay=gdyt, color=color.yellow)
xt = gcurve(gdisplay=gdxt, color=color.yellow)

# 參考地板和牆壁
floor = box(pos=(0,0,0), length=15, height=0.005, width=5)
wall1 = box(pos=((floor.length)/2,5,0), length=0.005, height=10, width=5)
wall2 = box(pos=(-(floor.length)/2,5,0), length=0.005, height=10, width=5)

# 球
ball = sphere(pos =(0, h, 0), radius=0.2, color=color.yellow ,make_trail= true,retain=50)

# 速度向量及速度標籤
vvec = arrow(shaftwidth=0.1)
vlable = label(pos=(0,0,0), text='v', box = False, opacity=0)

while t<20:
    rate(100)
    ball.pos = ball.pos + ballv*dt
    ballv = ballv + a*dt
    if ball.pos.y < ball.radius and ballv.y < 0:
        ballv.y = -ballv.y
    elif ball.pos.x > floor.length/2 - ball.radius and ballv.x > 0:
        ballv.x = -ballv.x
    elif ball.pos.x < -floor.length/2 + ball.radius and ballv.x < 0:
        ballv.x = -ballv.x
    vvec.pos = ball.pos
    vvec.axis = ballv/5
    vlable.pos = vvec.pos + vvec.axis+(0.5,0.5,0.5)
    yt.plot(pos=(t,ball.pos.y))
    xt.plot(pos=(t,ball.pos.x))
    t += dt
