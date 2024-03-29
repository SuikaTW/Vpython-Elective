from visual import *

v=0.09
dt = 0.01
t=0

#產生一個寬400像素,高400像素的3度空間以進行繪圖
scene = display(width=400, height=400,center=(0,0.06,0))
#產生一個扁長形方塊,當做是地板
floor = box(pos=(0,0,0), length=0.3, height=0.005, width=0.3, material=materials.wood)
#產生一個正立方物體
cube = box(pos=(-0.1, 0.05/2, -0.1), length=0.05, height=0.05, width=0.05, material=materials.earth)

#讓物體運動
while(true):
    while(cube.pos.x <0.10):#d
        rate(1000)
        t+= dt
        cube.pos.x +=v*dt
    while(cube.pos.z <0.10):#s
        rate(1000)
        t+= dt
        cube.pos.z +=v*dt
    while(cube.pos.x >-0.10):#a
        rate(1000)
        t+= dt
        cube.pos.x -=v*dt
    while(cube.pos.z >-0.10):#w
        rate(1000)
        t+= dt
        cube.pos.z -=v*dt
    while(cube.pos.z <0.10):#s
        rate(1000)
        t+= dt
        cube.pos.z +=v*dt
    while(cube.pos.x <0.10):#d
        rate(1000)
        t+= dt
        cube.pos.x +=v*dt
    while(cube.pos.z >-0.10):#w
        rate(1000)
        t+= dt
        cube.pos.z -=v*dt
    while(cube.pos.x >-0.10):#a
        rate(1000)
        t+= dt
        cube.pos.x -=v*dt
    
