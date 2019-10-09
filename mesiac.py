import tkinter
import random
canvas=tkinter.Canvas(width=1005,height=1000,bg="white")
canvas.pack()

def more():
    canvas.create_rectangle(0,500,1005,1000,fill="blue",outline="blue")
    
def mesiac(x,y):
    canvas.create_oval(x-100,500-y,x,400-y,fill="yellow",outline="yellow")
    canvas.create_oval(x-50,500-y,x+50,400-y,fill="white",outline="white")

def odraz(x,y):
    canvas.create_oval(x-100,500+y,x,600+y,fill="yellow",outline="yellow")
    canvas.create_oval(x-50,500+y,x+50,600+y,fill="blue",outline="blue")

def vlajka1():
    canvas.create_oval(0,450,200,650,fill="brown")
    canvas.create_line(100,450,100,250)
    canvas.create_rectangle(100,250,300,400,fill="green")

def vlajka2():
    canvas.create_oval(700,450,900,650,fill="brown")
    canvas.create_line(800,450,800,250)
    canvas.create_rectangle(800,250,1000,400,fill="red")


x=random.randint(100,900)
y=random.randint(50,950)
vlajka1()
vlajka2()
more()
mesiac(x,y)    
odraz(x,y)
