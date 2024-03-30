# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

import time



# 1. 參數設定
#加速度
g = -10.    #加速度值,在 x、z 方向為 0,在 y 方向為 g=-9.8 公尺/秒^2
#速度
vy = 0.0      #球的 y 方向速度(公尺/秒)，初始值為0
#高度
h = 10.0    #球的初始高度，單位為公尺
#時間間隔
dt = 0.005  #畫面更新的時間間隔,單位為秒
#經過時間
t = 0.0       #模擬所經過的時間 ,單位為秒,初始值為0

# 2. 畫面設定
#畫布
scene = display(center = (0, h/2, 0), background=(0.5,0.6, 0))
#參考地板
floor = box(pos=(0,0,0), length=15, height=0.5, width=5)
#球
ball = sphere(pos =(0, h, 0), radius=0.2, color=color.blue)

count = 1.0
temp=10
c=0

time.sleep(5)

while ball.pos.y > floor.height/2 + ball.radius:
    rate(100)
    t += dt
    c=c+1
    ball.pos.y = ball.pos.y + vy*dt
    vy += g*dt
    if(c%40==0 and count <=5):
        print 't =',t,' vy =',vy,' distance =',h-ball.pos.y,' Δ distance =',abs(temp-ball.pos.y)
        temp=ball.pos.y
        count =count + 1  
    
print 'falling time = ',t
