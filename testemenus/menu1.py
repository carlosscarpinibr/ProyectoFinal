from tkinter import *
from tkinter import ttk

class Menu():
    def __init__(self, root):
        frame1 = ttk.Frame(root, padding="6 6 6 6")
        frame1.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        frame2 = ttk.Frame(root, padding="6 6 6 6")
        frame2.grid(column=1, row=0)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        frame3 = ttk.Frame(root, padding="6 6 6 6")
        frame3.grid(column=2, row=0)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)

        frame4 = ttk.Frame(root, padding="6 6 6 6")
        frame4.grid(column=3, row=0)
        root.columnconfigure(3, weight=1)
        root.rowconfigure(0, weight=1)

        frame5 = ttk.Frame(root, padding="6 6 6 6")
        frame5.grid(column=4, row=0)
        root.columnconfigure(4, weight=1)
        root.rowconfigure(0, weight=1)

        root.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        root.geometry("900x200")  # set starting size of window
        root.maxsize(1366, 768)  # width x height
        #root.config(bg="lightgrey")
        self.r = StringVar()
        self.photo = PhotoImage(file='imagen.gif')
        #self.photoimage = self.photo.subsample(3)
        ttk.Button(frame1,  text='boton1',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        ttk.Button(frame2,  text='boton2',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        ttk.Button(frame3,  text='boton3',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        ttk.Button(frame4,  text='boton4',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        ttk.Button(frame5,  text='boton5',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        

    def hola(self,*args):
        self.r.set(f'Hola Mundo!!!')
    

    



# configuración de la raíz
root = Tk()
Menu(root)
root.mainloop()

