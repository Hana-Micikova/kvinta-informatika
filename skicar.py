import tkinter
x_max,y_max=500,500
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

global hrubka,farba
hrubka=1
farba="black"

cast=x_max/10
def obraz():
    a=0
    for _ in range(5):
        canvas.create_rectangle(cast*a,y_max/10*9,cast*(a+1),y_max,fill="white")
        a+=1
        
    canvas.create_rectangle(cast*a,y_max/10*9,cast*(a+1),y_max,fill="red")
    a+=1
    canvas.create_rectangle(cast*a,y_max/10*9,cast*(a+1),y_max,fill="yellow")
    a+=1
    canvas.create_rectangle(cast*a,y_max/10*9,cast*(a+1),y_max,fill="green")
    a+=1
    canvas.create_rectangle(cast*a,y_max/10*9,cast*(a+1),y_max,fill="blue")
    a+=1
    canvas.create_rectangle(cast*a,y_max/10*9,cast*(a+1),y_max,fill="black")

    b=1
    c=1
    for _ in range(3):
        canvas.create_oval(x_max/20*b-c,y_max/20*19-c,x_max/20*b+c,y_max/20*19+c,fill="black")
        b+=2
        c+=4

    canvas.create_text(x_max/20*7,y_max/20*19,font=("Wingdings 2", 40), text="3")
    canvas.create_text(x_max/20*9,y_max/20*19, font=("Arial", 12), text="guma")
    

def zmena(event):
    global hrubka,farba
    x,y=event.x,event.y
    if y<y_max/10*9 or y>y_max:
        pass
    
    elif x>0 and x<cast:
        hrubka=1

    elif x>cast and x<cast*2:
        hrubka=5
        
    elif x>cast*2 and x<cast*3:
        hrubka=9

    elif x>cast*3 and x<cast*4:
        canvas.delete("all")
        obraz()

    elif x>cast*4 and x<cast*5:
        farba="white"
        obraz()

    elif x>cast*5 and x<cast*6:
        farba="red"

    elif x>cast*6 and x<cast*7:
        farba="yellow"

    elif x>cast*7 and x<cast*8:
        farba="green"

    elif x>cast*8 and x<cast*9:
        farba="blue"

    elif x>cast*9 and x<cast*10:
        farba="black"

    else:
        print('to je ohranicenie, nie policko')
    

def kreslenie(event):
    global x1,y1
    x2,y2=event.x,event.y
    canvas.create_line(x1,y1,x2,y2,width=hrubka,fill=farba)
    x1,y1=x2,y2

def zaciatok(event):
    global x1,y1
    canvas.bind('<B1-Motion>',kreslenie)
    x1,y1=event.x,event.y    

canvas.bind('<Button-1>',zaciatok)
    

obraz()
canvas.bind('<Button-3>',zmena)
    
