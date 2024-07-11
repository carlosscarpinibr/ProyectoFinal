from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from cerub.guinvisita.menunvisita import Visita
from cerub.guilistar.menulistar import Listar
from cerub.guiestadistica.menuestadistica import Estadistica

class MenuP():
    def about(self):
            MessageBox.showinfo("Acerca de...","Este programa fue desarrollado por Carlos Scarpini.     Contacto: carlosscarpinibr@gmail.com")

    def __init__(self):
        self.mroot = Tk()

        frame1 = ttk.Frame(self.mroot, padding="6 6 6 6")
        frame1.grid(column=0, row=0)
        self.v = Visita()

        frame2 = ttk.Frame(self.mroot, padding="6 6 6 6")
        frame2.grid(column=1, row=0)
        self.l = Listar()

        frame3 = ttk.Frame(self.mroot, padding="6 6 6 6")
        frame3.grid(column=2, row=0)
        self.e = Estadistica()

        frame4 = ttk.Frame(self.mroot, padding="6 6 6 6")
        frame4.grid(column=3, row=0)

        frame5 = ttk.Frame(self.mroot, padding="6 6 6 6")
        frame5.grid(column=4, row=0)

        self.mroot.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        self.mroot.geometry("600x65")  # set starting size of window
        self.mroot.maxsize(1366, 768)  # width x height
        #root.config(bg="lightgrey")

        # configuración de la barra de menú principal (menubar)
        self.menubar = Menu()
        self.mroot.config(menu = self.menubar)


        helpmenu = Menu(self.menubar, tearoff = 0)
        #helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...", command=self.about)
        self.menubar.add_cascade(label = 'Ayuda', menu = helpmenu)


        ttk.Button(frame1,  text='Nueva Visita', command = self.v.guivisita).grid(row=0, column=0, ipadx=10, ipady=10)
        ttk.Button(frame2,  text='Gerenciar Visitas', command = self.l.guilista).grid(row=0, column=0, ipadx=10, ipady=10)
        ttk.Button(frame3,  text='Estadísticas', command = self.e.guiestadistica).grid(row=0, column=0, ipadx=10, ipady=10)
        ttk.Button(frame5,  text='Salir', command = self.mroot.destroy).grid(row=0, column=0, ipadx=10, ipady=10)

        self.mroot.mainloop()

        