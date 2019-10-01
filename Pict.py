from graph import *
Sizex = 1000
Sizey = 1000
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
	c.create_oval(Sizex*27/70,Sizey*39/70,Sizex*9/14,  Sizey*22/35,fill="brown")
	c.create_oval(Sizex/14,   Sizey*37/70,Sizex*3/7,   Sizey*5/7,fill="brown")
	c.create_oval(Sizex/35,   Sizey*4/7,  Sizex*9/140, Sizey*47/70,fill="brown")
	c.create_oval(0,          Sizey*37/70,Sizex/7,     Sizey*9/14,fill="brown")
	c.create_oval(Sizex*2/35, Sizey*23/35,Sizex*11/70, Sizey*5/7,fill="brown")
	c.create_oval(Sizex*23/70,Sizey*43/70,Sizex*3/7,   Sizey*5/7,fill="brown")
	c.create_oval(Sizex*2/5,  Sizey*24/35,Sizex*61/140,Sizey*27/35,fill="brown")


Back_Ground()
Cat()

run()
