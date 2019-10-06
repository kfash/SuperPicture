from graph import *
from tkinter import*
Sizex = 2000
Sizey = 2000
windowSize(Sizex,Sizey)
canvasSize(Sizex,Sizey)
c=canvas()

def Back_Ground ():
	brushColor(200,100,0)
	penColor(200,100,0)
	rectangle(0,0,Sizex,Sizey*5/14)
	brushColor(100,100,0)
	rectangle(0,Sizey*5/14,Sizex,Sizey)
	Window()
	
def Window ():
	brushColor("white")
	penColor("white")
	rectangle(Sizex*3/7,Sizey/35,Sizex*24/35,Sizey*23/70)
	brushColor("lightBlue")
	penColor("lightBlue")
	rectangle(Sizex*31/70,Sizey*3/70, Sizex*19/35,Sizey*6/35)
	rectangle(Sizex*31/70,Sizey*13/70,Sizex*19/35,Sizey*11/35)
	rectangle(Sizex*39/70,Sizey*3/70, Sizex*47/70,Sizey*6/35)
	rectangle(Sizex*39/70,Sizey*13/70,Sizex*47/70,Sizey*11/35)
	
def Cat ():
	Ears()
	c.create_oval(Sizex*27/70,Sizey*39/70,Sizex*9/14,  Sizey*22/35,fill="brown")
	c.create_oval(Sizex/14,   Sizey*37/70,Sizex*3/7,   Sizey*5/7,fill="brown")
	c.create_oval(Sizex/35,   Sizey*4/7,  Sizex*9/140, Sizey*47/70,fill="brown")
	c.create_oval(0,          Sizey*37/70,Sizex/7,     Sizey*9/14,fill="brown")
	c.create_oval(Sizex*2/35, Sizey*23/35,Sizex*11/70, Sizey*5/7,fill="brown")
	c.create_oval(Sizex*23/70,Sizey*43/70,Sizex*3/7,   Sizey*5/7,fill="brown")
	c.create_oval(Sizex*2/5,  Sizey*24/35,Sizex*61/140,Sizey*27/35,fill="brown")
	Eyes()
	Face()
	
	
def Ravel ():
	c.create_oval(Sizex*11/14,Sizey*11/14,Sizex*13/14,  Sizey*13/14,fill="grey")
	penColor("Black")
	polyline([(Sizex*111/140,Sizey*117/140),(Sizex*117/140,Sizey*115/140),(Sizex*123/140,Sizey*120/140),(Sizex*127/140,Sizey*127/140)])
	polyline([(Sizex*113/140,Sizey*114/140),(Sizex*117/140,Sizey*112/140),(Sizex*125/140,Sizey*117/140),(Sizex*129/140,Sizey*124/140)])
	polyline([(Sizex*113/140,Sizey*120/140),(Sizex*117/140,Sizey*123/140),(Sizex*123/140,Sizey*123/140)])
	polyline([(Sizex*113/140,Sizey*124/140),(Sizex*117/140,Sizey*127/140),(Sizex*123/140,Sizey*127/140)])

def Eyes ():
	c.create_oval(Sizex*43/500,Sizey*280/500,Sizex*63/500,Sizey*300/500,fill="limegreen")
	c.create_oval(Sizex*11/500,Sizey*280/500,Sizex*31/500,Sizey*300/500,fill="limegreen")
	c.create_oval(Sizex*19/500,Sizey*281/500,Sizex*24/500,Sizey*299/500,fill="black")
	c.create_oval(Sizex*51/500,Sizey*281/500,Sizex*56/500,Sizey*299/500,fill="black")
	
def Ears ():
	penColor("black")
	brushColor("brown")
	polygon([(Sizex*90/1000, Sizey*530/1000),(Sizex*110/1000, Sizey*500/1000),(Sizex*130/1000, Sizey*550/1000),(Sizex*90/1000, Sizey*530/1000)])
	polygon([(Sizex*60/1000, Sizey*530/1000),(Sizex*40/1000, Sizey*500/1000),(Sizex*20/1000, Sizey*550/1000),(Sizex*60/1000, Sizey*530/1000)])
	brushColor("Sienna")
	polygon([(Sizex*95/1000, Sizey*530/1000),(Sizex*110/1000, Sizey*508/1000),(Sizex*125/1000, Sizey*546/1000),(Sizex*95/1000, Sizey*530/1000)])
	polygon([(Sizex*55/1000, Sizey*530/1000),(Sizex*40/1000, Sizey*508/1000),(Sizex*25/1000, Sizey*546/1000),(Sizex*55/1000, Sizey*530/1000)])

def Face ():
	brushColor ("LightSalmon")
	polygon([(Sizex*65/1000, Sizey*600/1000),(Sizex*85/1000, Sizey*600/1000),(Sizex*75/1000, Sizey*620/1000),(Sizex*65/1000, Sizey*600/1000)])
	polyline([(Sizex*75/1000,Sizey*620/1000),(Sizex*75/1000,Sizey*625/1000)])
	c.create_arc(Sizex*75/1000,Sizey*620/1000,Sizex*65/1000,Sizey*630/1000,start=0,extent=-180,style=ARC,outline='black',width=1)
	c.create_arc(Sizex*75/1000,Sizey*620/1000,Sizex*85/1000,Sizey*630/1000,start=0,extent=-180,style=ARC,outline='black',width=1)



Back_Ground()
Cat()
Ravel()

run()

