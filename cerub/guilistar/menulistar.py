from tkinter import *
from tkinter import ttk
from cerub.guirevision.menurevison import Revision
from pathlib import Path
import json

class Listar():
    def __init__(self):
        return None
    
    def indicelista(self):
        indice = self.Lb1.curselection()
        self.r = Revision()
        self.r.guirevision(indice[0],self.lista[indice[0]])

    def crearlista(self):
        self.frame1 = ttk.Frame(self.top, padding="6 6 6 6")
        self.frame1.grid(column=0, row=0)
        self.archivo = Path('cerub/archivos/pacientes.json')
        self.contenidoLista = self.archivo.read_text()
        self.lista = json.loads(self.contenidoLista)
        self.Lb1 = Listbox(self.frame1, selectmode=SINGLE, height=40, width=60, yscrollcommand = self.scrollbarV.set, xscrollcommand = self.scrollbarH.set)
        i=1
        for visita in self.lista:
            for key, value in visita.items():
                fecha = f'{key[6]}{key[7]}/{key[4]}{key[5]}/{key[0]}{key[1]}{key[2]}{key[3]}'
                hora = f'{key[9]}{key[10]}:{key[11]}{key[12]}:{key[13]}{key[14]}'
                self.Lb1.insert(i,f'{fecha} - {hora} - {value['name']}')
                i = i+1
        self.Lb1.pack()

    def actualizarlista(self):
        print('Actualizando lista')
        self.Lb1.destroy()
        self.crearlista()



    def guilista(self):
        
        self.top = Tk()
        self.top.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        self.top.geometry("720x720")  # set starting size of window
        self.top.maxsize(1366, 768)  # width x height

        # scrollbar
        self.scrollbarV = Scrollbar(self.top, orient=VERTICAL)
        self.scrollbarV.grid(column=1, row=0, ipady=300)
        self.scrollbarH = Scrollbar(self.top, orient=HORIZONTAL)
        self.scrollbarH.grid(column=0, row=1, ipadx=150)
        
        
        self.frame1 = ttk.Frame(self.top, padding="6 6 6 6")
        self.frame1.grid(column=0, row=0)
        self.crearlista()

        self.scrollbarV.config(command= self.Lb1.yview)
        self.scrollbarH.config(command= self.Lb1.xview)


        frame2 = ttk.Frame(self.top, padding="6 6 6 6")
        frame2.grid(column=2, row=0)
        ttk.Button(frame2,  text='Visualizar visita', command =self.indicelista).grid(row=1, column=0, ipadx=2, ipady=2)
        ttk.Button(frame2,  text='Actualizar lista de visitas', command =self.actualizarlista).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(frame2,  text='Salir', command = self.top.destroy).grid(row=2, column=0, ipadx=2, ipady=2)
        
        self.top.mainloop()

if __name__ == '__main__':
    menu = Listar()
    menu.guilista()