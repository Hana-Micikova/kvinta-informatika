import tkinter
from random import randrange,randint
x_max,y_max=1000,1000
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

s1,s2=x_max/2,y_max/2

for _ in range(2000):
    x,y=randrange(x_max),randrange(y_max)
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
        
    canvas.create_line(s1,s2,x,y,fill=farba)
