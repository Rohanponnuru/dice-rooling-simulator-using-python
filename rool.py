from tkinter import*
import random

root=Tk()
root.geometry("700x450")

label1=Label(root,font=("comic sans ms",260))

def rool():
    dice =['\u2680','\u2682','\u2683','\u2684','\u2685']

    label1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    label1.pack()

b1=Button(root,text="Roll the dice!",foreground='blue',command=rool)
b1.place(x=300,y=0)
b1.pack()

root.mainloop()