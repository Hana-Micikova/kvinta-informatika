import tkinter
from random import randrange
x_max, y_max = 500, 500
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

r, g, b = randrange(256), randrange(256), randrange(256)
dr, dg, db = 1, 1, 1

while True:
    canvas.delete("all")
    color=f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(1,1,x_max+1,y_max+1,fill=color,outline=color)
    r+=dr
    g+=dg
    b+=db
    canvas.update()
    canvas.after(1)
    
    if r==0 or r==255:
        dr*=-1
    if g==0 or g==255:
        dg*=-1
    if b==0 or b==255:
        db*=-1
