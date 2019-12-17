import tkinter
x_max,y_max=1000,1000
canvas=tkinter.Canvas(width=x_max,height=y_max,background="white")
canvas.pack()
import random

def kvapka(x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="light blue")

for _ in range(1000):
    canvas.delete("all")
    for _ in range(200):
        r=5
        kvapka(random.randrange(x_max-5),random.randrange(y_max-5),r)
    canvas.update()
    canvas.after(50)
