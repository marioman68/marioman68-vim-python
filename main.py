from Tkinter import *
import tkMessageBox
import sys
import pygame

pygame.init()

root = Tk()

root.geometry("500x100+200+200")

def quit1():
	quit()
	
def pause1():
	pygame.mixer.music.pause()

def play1():
	pygame.mixer.music.play()

def amy():
	pygame.mixer.Sound("amy.wav").play()
	
def cool():
	s = entry_1.get()
	answer = tkMessageBox.askquestion("Window Title", "%s, Do monkeys live forever?" % s)
	
	if answer == "yes":
		answe1 = tkMessageBox.askquestion("Window Title", "%s, So monkeys do live forever?" % s)
		
		if answe1 == "yes":
			tkMessageBox.showinfo("Window Title", "Monkeys are cool")
		else:
			tkMessageBox.showinfo("Window Title", "%s You do not believe" % s)
	else:
		tkMessageBox.showinfo("Window Title", "%s You do not believe :(" % s)
				
		
thelable = Label(root, text="Enter your name")
pygame.mixer.music.load("skyecuillin.ogg")
pygame.mixer.music.play()
entry_1 = Entry(root)

button1 = Button(root, text="Ask Question?", command=cool)
button2 = Button(root, text="Quit", command=quit1)
#button3 = Button(root, text="AMY", command=amy)
button4 = Button(root, text="Pause Music", command=pause1)
button5 = Button(root, text="Play Music", command=play1) 

thelable.pack()
button4.pack()
#button3.pack()
button1.pack()
button2.pack()
entry_1.pack()
entry_1.grid(row=0, column=1)
thelable.grid(row=0)
button1.grid(row=1)
button2.grid(row=1, column=1)
#button3.grid(row=1, column=2)
button4.grid(row=1, column=3)
button5.grid(row=2, column=3)
#thelable2.pack()
root.mainloop() 