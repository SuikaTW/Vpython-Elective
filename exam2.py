from visual import *
scene = display(width=1000, height=1000, background=(0.5,0.6,0.5))
x_axis = arrow(axis=(17,0,0), shaftwidth=0.1)
y_axis = arrow(axis=(0,17,0), shaftwidth=0.1)
label(pos=(17.5,0,0), text='x', box = False)
label(pos=(0,17.5,0), text='y', box = False)
label(pos=(3,-0.5,0), text='(3,0,0)', box = False)
label(pos=(6,-0.5,0), text='(6,0,0)', box = False)
label(pos=(9,-0.5,0), text='(9,0,0)', box = False)
label(pos=(12,-0.5,0), text='(12,0,0)', box = False)
label(pos=(15,-0.5,0), text='(15,0,0)', box = False)
label(pos=(-1,3,0), text='(0,3,0)', box = False)
label(pos=(-1,6,0), text='(0,6,0)', box = False)
label(pos=(-1,9,0), text='(0,9,0)', box = False)
label(pos=(-1,12,0), text='(0,12,0)', box = False)
label(pos=(-1,15,0), text='(0,15,0)', box = False)
R = 1
i = 0
vectors = vector(3,0,0)
#дTид
for tri in range(5):
    while i<3:
        rate(1000)
        vec = vector(R*cos((2*pi/3)*i),R*sin((2*pi/3)*i),0)
        arrow(pos = vectors,axis = vec,color = color.black,shaftwidth = 0.1)
        i += 1
        vectors += vec
    i = 0
    vectors += (0,3,0)
vectors = vector(6,0,0)
#6
for tri in range(4):
    while i<6:
        rate(1000)
        vec = vector(R*cos((2*pi/6)*i),R*sin((2*pi/6)*i),0)
        arrow(pos = vectors,axis = vec,color = color.black,shaftwidth = 0.1)
        i += 1
        vectors += vec
    i = 0
    vectors += (0,3,0)

vectors = vector(9,0,0)
for tri in range(3):
    while i<9:
        rate(1000)
        vec = vector(R*cos((2*pi/9)*i),R*sin((2*pi/9)*i),0)
        arrow(pos = vectors,axis = vec,color = color.black,shaftwidth = 0.1)
        i += 1
        vectors += vec
    i = 0
    vectors += (0,3,0)
vectors = vector(12,0,0)
for tri in range(2):
    while i<12:
        rate(1000)
        vec = vector(R*cos((2*pi/12)*i),R*sin((2*pi/12)*i),0)
        arrow(pos = vectors,axis = vec,color = color.black,shaftwidth = 0.1)
        i += 1
        vectors += vec
    i = 0
    vectors += (0,3,0)
vectors= vector(15,0,0)
for tri in range(1):
    while i<15:
        rate(1000)
        vec = vector(R*cos((2*pi/15)*i),R*sin((2*pi/15)*i),0)
        arrow(pos = vectors,axis = vec,color = color.black,shaftwidth = 0.1)
        i += 1
        vectors += vec
    i = 0
    vectors += (0,3,0)



