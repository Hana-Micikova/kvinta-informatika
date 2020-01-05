import tkinter
x_max,y_max=500,500
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()
    
def kreslenie(event):
    global x1,y1
    x2,y2=event.x,event.y
    canvas.create_line(x1,y1,x2,y2)
    x1,y1=x2,y2

def zaciatok(event):
    global x1,y1
    canvas.bind('<B1-Motion>',kreslenie)
    x1,y1=event.x,event.y    

canvas.bind('<Button-1>',zaciatok)

