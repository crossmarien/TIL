from tkinter import *
main= Tk()
c= Canvas(main, width=400, height=200)
c.pack()

c.create_rectangle(0,0,0,0,outline="red", width=5)

c.create_rectangle(0,0,50,90)
