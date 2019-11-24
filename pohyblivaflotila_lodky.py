import tkinter
import random
m,n=1000,1000
canvas=tkinter.Canvas(width=m,height=n,bg="white")
canvas.pack()


def lodicka(x,y,k,a,b):
    canvas.create_line(x,y,x,y-4*k,width=1/2*k,fill="brown")
    canvas.create_polygon(x-2*k,y-k,x-k,y+k,x+k,y+k,x+2*k,y-k,fill=b,outline="black")
    canvas.create_polygon(x,y-3/2*k,x,y-4*k,x+k,y-2*k,fill="white",outline="black")
    #logo(x,y+k/3,k/3,a,b)

def lodicka1(d,q):
    lodicka(d,500,50,"light blue","sienna")
    q*=1


def lodicka2 (e,q):
    lodicka(e,600,75,"light blue","sienna")
    q*=2
    
    
def lodicka3(f,q):
    lodicka(f,720,113,"light blue","sienna")
    q*=3

def flotila2():     
    d,e,f=1,1,1
    for _ in range(500):
        q=10
        canvas.delete("all")
        lodicka1(d,q)
        d+=q
        lodicka2(e,q)
        e+=2*q
        lodicka3(f,q)
        f+=3*q
        canvas.update()
        canvas.after(100)

flotila2()        
