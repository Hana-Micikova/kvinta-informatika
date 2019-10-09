import tkinter
import random
canvas=tkinter.Canvas(width=1000,height=1000)
canvas.pack()

def panelacik(x,y,v,s):
    canvas.create_rectangle(x,y,x+s*40-30,y+v*40-20,fill="pink")
    b=y
    for i in range(1,s):
        for i in range(1,v):
            canvas.create_rectangle(x+10,y+10,x+40,y+40,fill="teal")
            y=y+40
        y=b
        x=x+40

def petrzalka():
    for i in range(1,11):
        panelacik(random.randint(0,1000),random.randint(0,1000),random.randint(1,31),random.randint(1,16))

petrzalka()        
