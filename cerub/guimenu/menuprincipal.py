from tkinter import *
from tkinter import ttk
from cerub.guinvisita.menunvisita import Visita
from cerub.guilistar.menulistar import Listar
from cerub.guiestadistica.menuestadistica import Estadistica

class Menu():
    def __init__(self):
        mroot = Tk()

        frame1 = ttk.Frame(mroot, padding="6 6 6 6")
        frame1.grid(column=0, row=0)
        self.v = Visita()

        frame2 = ttk.Frame(mroot, padding="6 6 6 6")
        frame2.grid(column=1, row=0)
        self.l = Listar()

        frame3 = ttk.Frame(mroot, padding="6 6 6 6")
        frame3.grid(column=2, row=0)
        self.e = Estadistica()

        frame4 = ttk.Frame(mroot, padding="6 6 6 6")
        frame4.grid(column=3, row=0)

        frame5 = ttk.Frame(mroot, padding="6 6 6 6")
        frame5.grid(column=4, row=0)

        mroot.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        mroot.geometry("600x65")  # set starting size of window
        mroot.maxsize(1366, 768)  # width x height
        #root.config(bg="lightgrey")
        self.r = StringVar()

        ttk.Button(frame1,  text='Nueva Visita', command = self.v.guivisita).grid(row=0, column=0, ipadx=10, ipady=10)
        ttk.Button(frame2,  text='Gerenciar Visitas', command = self.l.guilista).grid(row=0, column=0, ipadx=10, ipady=10)
        ttk.Button(frame3,  text='Estadísticas', command = self.e.guiestadistica).grid(row=0, column=0, ipadx=10, ipady=10)
        #ttk.Button(frame4,  text='b4', command = mroot.destroy).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(frame5,  text='Salir', command = mroot.destroy).grid(row=0, column=0, ipadx=10, ipady=10)

        mroot.mainloop()