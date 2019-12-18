import tkinter
x_max,y_max=1000,1000
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()


def kreslenie1(event):
    x,y=event.x,event.y
    global xx,yy
    xx,yy=x,y

def kreslenie2(event):
    x1,y1=event.x,event.y
    canvas.create_line(x1,y1,xx,yy)
    
canvas.bind('<Motion>', kreslenie2)

