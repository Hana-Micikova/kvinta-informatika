import tkinter
from random import randrange,randint
x_max,y_max=1000,1000
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

for _ in range(2000):
    r=20
    x,y=randrange(x_max-r),randrange(y_max-r)
    farba="black"
    
    if x<=x_max/2 and y<=y_max/2:
        farba="red"
        
    elif x<=x_max/2 and y>y_max/2:
        farba="blue"
        
    elif x>x_max/2 and y<=y_max/2:
        farba="green"
        
    elif x>x_max/2 and y>y_max/2:
        farba="yellow" 
        
    else:
        print('houston, we have a problem')
        
    canvas.create_rectangle(x-r,y-r,x+r,y+r,fill=farba)    
