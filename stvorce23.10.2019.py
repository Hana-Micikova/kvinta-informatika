import tkinter
import random

X_MAX,Y_MAX= 1200,900

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
canvas.pack()

def stvorce(x,y,r,m,p):
    for _ in range (1,p):
        canvas.create_rectangle(x-r,y-r,x+r,y+r)
        r=r-m

x=random.randint(0,150)
y=random.randint(0,150)
r=random.randint(75,150)
for _ in range(10):
      stvorce(random.randint(0+x+r,X_MAX-x-r),random.randint(0+y+r,Y_MAX-y-r),r,random.randint(5,15),random.randint(6,11))        
