from visual import *
import time
import math
# 1. �ѼƳ]�w
#�[�t��
a = vector(0,-9.8,0)    #�[�t�׭�,�b x�Bz ��V�� 0,�b y ��V�� g=-9.8 ����/��^2
#�ɶ����j
dt = 0.001  #�e����s���ɶ����j,��쬰��
#�g�L�ɶ�
t = 0       #�����Ҹg�L���ɶ� ,��쬰��,��l�Ȭ�0
# 2. �e���]�w
#�e��
scene = display(center = (7.5, 1, -10), background=(0.,0.6,0.4),width=1200, height=800)
#�ѦҦa�O
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
    #theta ��0�רC���W�[4.5�ת���90�סA�O�o�⨤���ഫ���|��(ex:90�� = pi*90/180)
    theta+= 4.5
    ball.v = vector(v0*cos(math.radians(theta)),v0*sin(math.radians(theta)),0)
    while ball.pos.y - floor.pos.y >= r:
        rate(5000)
        #�t�ק�s
        ball.v+= a*dt
        #��m��s
        ball.pos+=ball.v*dt
        t += dt
        
        if ball.pos.x>Rmax:
            Rmax=ball.pos.x
            thetamax = theta




        
    print '�c =',n*4.5,'�X  ','R =',ball.pos.x
    n += 1
print ''
print '�c =',thetamax,'�X  ','Rmax =',Rmax
