import tkinter
from random import randrange,randint
x_max,y_max=1800,1000
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

for _ in range(20000):
    r=20
    x,y=randrange(x_max-r),randrange(y_max-r)
    a,b="pink","cyan"

    if (x<x_max/6*2 and y<y_max/6*2):
        farba=a
        
    elif (x>x_max/6*3 and y>y_max/6*3):
        farba=a

    elif (x<x_max/6*2 and y>y_max/6*3):
        farba=a

    elif (x>x_max/6*3 and y<y_max/6*2):
        farba=a

    else:
        farba=b

    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba)    
        
