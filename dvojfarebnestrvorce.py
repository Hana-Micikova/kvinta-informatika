import tkinter
from random import randrange,randint
x_max,y_max=500,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

r,g,b=randint(0,256),randint(0,256),randint(0,256)
dr,dg,db=1,1,1

r=50
x,y=r+randrange(x_max-2*r),r+randrange(y_max-2*r)
dx,dy=5,5


while True:
    canvas.delete("all")
    color= f'#(r:02x)(g:02x)(b:02x)'
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="pink")
    x+=dx
    y+=dy
    if x>x_max-r or x<r:
        dx*=-1
    if y>y_max-r or y<r:
        dy*=-1

    if x==r and (y==r or y==y_max-r):
        print("dvd time")

    if x==x_max-r and (y==r or y==y_max-r):
        print ("dvd out of time")
        
    canvas.update()
    canvas.after(1)
