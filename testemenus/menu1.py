from tkinter import *
from tkinter import ttk
from menunvisita import Visita
from menulistar import Listar

class Menu():
    def __init__(self, mroot):
        frame1 = ttk.Frame(mroot, padding="6 6 6 6")
        frame1.grid(column=0, row=0)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)
        self.v = Visita()

        frame2 = ttk.Frame(mroot, padding="6 6 6 6")
        frame2.grid(column=1, row=0)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)
        self.l = Listar()

        frame3 = ttk.Frame(mroot, padding="6 6 6 6")
        frame3.grid(column=2, row=0)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        frame4 = ttk.Frame(mroot, padding="6 6 6 6")
        frame4.grid(column=3, row=0)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        frame5 = ttk.Frame(mroot, padding="6 6 6 6")
        frame5.grid(column=4, row=0)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        mroot.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        mroot.geometry("650x50")  # set starting size of window
        mroot.maxsize(1366, 768)  # width x height
        #root.config(bg="lightgrey")
        self.r = StringVar()
        self.photo = PhotoImage(file='imagen.gif')
        self.photoimage = self.photo.subsample(3)
        ttk.Button(frame1,  text='Nueva Visita', command = self.v.guivisita).grid(row=0, column=0, ipadx=2, ipady=2)
        #ttk.Label(frame1,   image= self.photo, compound=TOP).grid(row=1, column=0)
        ttk.Button(frame2,  text='Listar Visitas', command = self.l.guilista).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(frame3,  text='b3', command = self.holas).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(frame4,  text='b4', command = self.holas).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(frame5,  text='Salir', command = mroot.destroy).grid(row=0, column=0, ipadx=2, ipady=2)
        
        # ttk.Button(frame1,  text='boton1',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        # ttk.Button(frame2,  text='boton2',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        # ttk.Button(frame3,  text='boton3',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        # ttk.Button(frame4,  text='boton4',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        # ttk.Button(frame5,  text='boton5',image=self.photo, compound=TOP, command = self.hola).grid(row=0, column=0, ipadx=20, ipady=10)
        

    def holas(self):
        self.r.set(f'Hola Mundo!!!')
    

    



# configuración de la raíz
mroot = Tk()
Menu(mroot)
mroot.mainloop()

