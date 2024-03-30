from visual import *
import time
import math
# 1. 參數設定
#加速度
a = vector(0,-9.8,0)    #加速度值,在 x、z 方向為 0,在 y 方向為 g=-9.8 公尺/秒^2
#時間間隔
dt = 0.001  #畫面更新的時間間隔,單位為秒
#經過時間
t = 0       #模擬所經過的時間 ,單位為秒,初始值為0
# 2. 畫面設定
#畫布
scene = display(center = (7.5, 1, -10), background=(0.,0.6,0.4),width=1200, height=800)
#參考地板
floor = box(pos=(7.5,0,0), length=72, height=0.005, width=5, color=color.yellow)

r = 0.2
v0 = 20
n = 0
thetamax = 0
Rmax = 0
theta = 0

time.sleep(3)
while n<=19:
    ball = sphere(pos =(0, r + floor.height/2, 0), radius=r, color=(0.3,0.1*n,0.1*n) ,make_trail= true)
    #theta 由0度每次增加4.5度直到90度，記得把角度轉換成徑度(ex:90度 = pi*90/180)
    theta+= 4.5
    ball.v = vector(v0*cos(math.radians(theta)),v0*sin(math.radians(theta)),0)
    while ball.pos.y - floor.pos.y >= r:
        rate(5000)
        #速度更新
        ball.v+= a*dt
        #位置更新
        ball.pos+=ball.v*dt
        t += dt
        
        if ball.pos.x>Rmax:
            Rmax=ball.pos.x
            thetamax = theta




        
    print 'θ =',n*4.5,'°  ','R =',ball.pos.x
    n += 1
print ''
print 'θ =',thetamax,'°  ','Rmax =',Rmax
