from tkinter import *
import os

root = Tk(screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)

dir_path = os.path.dirname(os.path.realpath(__file__))
bg_path = dir_path + '\images\image.png'

filename =PhotoImage(file=bg_path, cnf={}, master=None)
C = Canvas(root, bg="blue", height=1300, width=750)
#filename = PhotoImage(file = "C:\\Users\\Omkar\\Downloads\\p1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
lbl2 = Button(master=root, cnf={},text='Hello',COMMAND=None)
lbl2.place(x=375, y=500, in_=root)
C.pack()

root.mainloop()