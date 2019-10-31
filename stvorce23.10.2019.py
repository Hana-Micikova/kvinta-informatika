import tkinter
import random

X_MAS,Y_MAS= 1800,1600

canvas=tkinter.Canvas(width=X_MAS,height=Y_MAS,bg="white")
canvas.pack()

def stvorce(x,y,r,m,p):
    for i in range (1,p):
        canvas.create_rectangle(x-r,y-r,x+r,y+r)
        r=r-m

x=random.randint(0,800)
y=random.randint(0,600)
r=random.randint(1,400)

stvorce(random.randint(0+x+r,X_MAS-x-r),random.randint(0+y+r,X_MAS-y-r),r,random.randint(5,15),random.randint(3,15))        
