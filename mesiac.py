import tkinter
import random
canvas=tkinter.Canvas(width=1000,height=1000,bg="white")
canvas.pack()

def more():
    canvas.create_rectangle(0,500,1000,1000,fill="blue",outline="blue")

def mesiac(x,y,r,a,b):
    for i in range(1,3):
        canvas.create_oval(x-2*r,500+y,x,400+y,fill=a,outline=a)
        canvas.create_oval(x-r,500+y,x+r,400+y,fill=b,outline=b)
        y=-1*y
        b="white"
        
def vlajka1():
    canvas.create_oval(0,450,200,650,fill="brown")
    canvas.create_line(100,450,100,250)
    canvas.create_rectangle(100,250,300,400,fill="green")

def vlajka2():
    canvas.create_oval(700,450,900,650,fill="brown")
    canvas.create_line(800,450,800,250)
    canvas.create_rectangle(800,250,1000,400,fill="red")



vlajka1()
vlajka2()
more()
mesiac(random.randint(100,900),random.randint(50,450),50,"yellow","blue")    


