import tkinter
import random
a,b=1000,1000
canvas=tkinter.Canvas(width=a,height=b,bg="lime")
canvas.pack()

def strom(x,y,r):
    canvas.create_rectangle(x+10,y+200,x-10,y,fill="brown",outline="brown")
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="green")

for i in range(1,11):
    strom(random.randint(0,a),random.randint(0,b),random.randint(30,180))

def stebla(x,y):
    for i in range(3,random.randint(4,21)):
        canvas.create_line(x,y,x+random.randint(-20,20),y-random.randint(0,30),fill="green",width=random.randint(1,4))

for i in range(0,20):
    stebla(random.randint(0,a),random.randint(0,b))
