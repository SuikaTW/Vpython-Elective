from visual import *
scene = display(width=1000, height=1000, background=(0.5,0.6,0.5))

x_axis = arrow(axis=(2,0,0), shaftwidth=0.01)
y_axis = arrow(axis=(0,2,0), shaftwidth=0.01)
z_axis = arrow(axis=(0,0,2), shaftwidth=0.01)
label(pos=(2.1,0,0), text='x', box = False)
label(pos=(0,2.1,0), text='y', box = False)
label(pos=(0,0,2.1), text='z', box = False)

w = 2*pi/6
R = 1
vectors = vector(0,0,0)
i = 0
while i<6:
    rate(1000)
    vec = vector(R*cos(w*i),R*sin(w*i),0)
    arrow(pos=vectors,axis=vec,color=color.black, shaftwidth=0.02)
    vectors += vec
    i += 1
    
