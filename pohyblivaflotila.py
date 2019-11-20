import tkinter
import random
m,n=1000,1000
canvas=tkinter.Canvas(width=m,height=n,bg="white")
canvas.pack()

def more():
    canvas.create_rectangle(0,n/2,m,n,fill="blue")

def mesiac(x,y,r,a,b):
    canvas.create_oval(x-2*r,y,x,y-2*r,fill=a,outline=a)
    canvas.create_oval(x-r,y,x+r,y-2*r,fill=b,outline=b)

def odraz(x,y,r,a,b):
    canvas.create_oval(x-2*r,y,x,y+2*r,fill=a,outline=a)
    canvas.create_oval(x-r,y,x+r,y+2*r,fill=b,outline=b)
    
def vlajka(x,y,a):
    canvas.create_oval(x,y,x+300,y+300,fill="brown")
    canvas.create_line(x+125,y,x+125,y-400)
    canvas.create_rectangle(x+125,y-200,x+400,y-400,fill=a)

def obratenymesiac(x,y,r,a,b):
    mesiac(x,y,-r,a,b)

def logo(x,y,r,a,b):
    mesiac(x+2*r,y,r,a,b)
    obratenymesiac(x-2*r,y-2*r,r,a,b)

def mesiacaodraz():
    x=650
    y=450
    r=50
    odraz(x,n-y,r,"yellow","blue")
    mesiac(x,y,r,"yellow","white")

def lodicka(x,y,k,a,b):
    canvas.create_line(x,y,x,y-4*k,width=1/2*k,fill="brown")
    canvas.create_polygon(x-2*k,y-k,x-k,y+k,x+k,y+k,x+2*k,y-k,fill=b,outline="black")
    canvas.create_polygon(x,y-3/2*k,x,y-4*k,x+k,y-2*k,fill="white",outline="black")
    logo(x,y+k/3,k/3,a,b)

def flotila(x):
    y=n/2
    k=50
    a="light blue"
    b="sienna"
    i=10
    for _ in range(3):
        lodicka(x,y,k,a,b)
        x=x-2*k+i
        y=y+2*k
        k=3/2*k
        i+=10
        

def obraz():
    vlajka(0,n/2-50,"green")
    vlajka(m/10*6,n/2-50,"red")
    more()
    mesiacaodraz()
    mesiac(262,185,40,"red","green")
    logo(862,185,40,"light blue","red")

def flotila2():
    x=1
    k=50
    i=10
    for _ in range(500):
        canvas.delete("all")
        obraz()
        flotila(x)
        
        canvas.update()
        canvas.after(100)

flotila2()        
            
