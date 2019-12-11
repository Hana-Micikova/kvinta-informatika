import tkinter
from random import randrange,randint
x_max,y_max=900,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

def klik(event):
    x,y=event.x,event.y
    print(x,y)

def kreslenie(event):
    x,y=event.x,event.y
    r=5
    c,d,e,f="red","yellow","green","blue"
    canvas.create_oval(x-r,y-r,x+r,y+r,width=3,fill=c,outline=d)
    a=x_max-x
    b=y_max-y
    canvas.create_oval(a-r,b-r,a+r,b+r,width=3,fill=d,outline=e)
    canvas.create_oval(x-r,b-r,x+r,b+r,width=3,fill=e,outline=f)
    canvas.create_oval(a-r,y-r,a+r,y+r,width=3,fill=f,outline=c)
    
canvas.bind('<Button-1>', klik)    
canvas.bind('<Motion>',kreslenie)
