import tkinter
import random
canvas=tkinter.Canvas(width=1000,height=1000,bg="lime")
canvas.pack()

def strom(x,y,r):
    canvas.create_rectangle(x+10,y+200,x-10,y,fill="brown",outline="brown")
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="green")

for i in range(1,11):
    strom(random.randint(0,1000),random.randint(0,1000),random.randint(30,180))

def stebla(x,y):
    for i in range(3,random.randint(4,21)):
        canvas.create_line(x,y,x+random.randint(-20,20),y-random.randint(0,30),fill="green")

for i in range(0,20):
    stebla(random.randint(0,1000),random.randint(0,1000))
