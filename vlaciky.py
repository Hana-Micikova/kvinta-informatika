import tkinter
import random

X_MAX,Y_MAX= 1200,900

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
canvas.pack()

def vlacik(x,y,z,c,d,a,b,e,f,r):
    #x,y-stred, z-farba, a,b-spojnica vlacikov, c,d-vzdialenost rohov vlaciku od stredu,r-polomer kolies, e,f-vzdialenost klies od stredu
    canvas.create_line(x-a,y+b,x+a,y+b,width=10)
    canvas.create_rectangle(x-c,y-d,x+c,y+d,fill=z)
    canvas.create_oval(x-e-r,y+f-r,x-e+r,y+f+r,fill="black")
    canvas.create_oval(x+e-r,y+f-r,x+e+r,y+f+r,fill="black")

x,y=200,200
c,d=80,45
for _ in range(4):
     vlacik(x,y,"red",c,d,c/4*5,d/4*3,c/2,d,25)
     x+=200
     
x,y=200,400
for _ in range(2):
    vlacik(x,y,"green",c,d,c/4*5,d/4*3,c/2,d,25)
    x+=200

x,y=200,600
for _ in range(3):
    vlacik(x,y,"blue",c,d,c/4*5,d/4*3,c/2,d,25)
    x+=200
    

