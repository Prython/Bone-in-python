from random import randint
from tkinter import *
tk = Tk()
tk.title('Кость')
tk.geometry(f"240x260+100+200")
tk['bg']='black'
def f(key):
    def img(k):
        img = PhotoImage(file=k)
        label = Label(tk, image=img).grid(row=6, column=8)
        label.image_type = img
        label.pack()
    if key == 'play':
        r = randint(1, 6)
        if r == 1:
            img('l.png')
        elif r == 2:
            img('ll.png')
        elif r == 3:
            img('lll.png')
        elif r == 4:
            img('lV.png')
        elif r == 5:
            img('V.png')
        elif r ==6:
            img('Vl.png')
    elif key == 'exit':
        exit()
Button(text='Play', command=lambda: f('play'), bg='silver').grid(row=7, column=5)
Button(text='X', command=lambda: f('exit'), bg='red').grid(row=0, column=1050)
tk.mainloop()