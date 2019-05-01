from tkinter import *
import driver
import os

def ignite():
    symb = txt.get()
    root.destroy()
    driver.master_process(symb)
    
root = Tk()
root.title(string='Stock Market Prediction Using Artificial Neural Network- Omkar, Shrutika, Vanishree')

dir_path = os.path.dirname(os.path.realpath(__file__))
bg_path = dir_path + '\images\image.png'

filename =PhotoImage(file=bg_path)
C = Canvas(root, bg="blue", height=1300, width=750)
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl1 = Label(root, text = 'Enter Company Symbol', font='Times 10 bold')
lbl1.place(x=330,y=500, in_=root)

txt = Entry(root)
txt.place(x=330,y=530,in_=root)

button1 = Button(root,text= 'Predict', command = ignite, font='Times 10 bold')
button1.place(x=365,y=560,in_=root)

C.pack()

root.geometry("800x800") 
root.resizable(0,0)

root.mainloop()