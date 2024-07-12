from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from cerub.guirevision.menurevison import Revision
from cerub.controles.controlar import Control
from pathlib import Path
import json
import os

class Listar():
    def __init__(self):
        return None
    
    def indicelista(self):
        indice = self.Lb1.curselection()
        self.r = Revision()
        while True:
            try:
                self.r.guirevision(indice[0],self.lista[indice[0]])
                break
            except IndexError:
                MessageBox.showerror("Atención","Seleccione una visita en la lista para visualízala.")
                break
        

    def crearlista(self):
        self.frame1 = ttk.Frame(self.top, padding="6 6 6 6")
        self.frame1.grid(column=0, row=0)
        self.controle = Control()
        self.lista = self.controle.leerdatabase()
        self.Lb1 = Listbox(self.frame1, selectmode=SINGLE, height=40, width=60, yscrollcommand = self.scrollbarV.set, xscrollcommand = self.scrollbarH.set)
        i=0
        for visita in self.lista:
            for key, value in visita.items():
                fecha = f'{key[6]}{key[7]}/{key[4]}{key[5]}/{key[0]}{key[1]}{key[2]}{key[3]}'
                hora = f'{key[9]}{key[10]}:{key[11]}{key[12]}:{key[13]}{key[14]}'
                self.Lb1.insert(i,f'{fecha} - {hora} - {value['name']}')
                i = i+1
        self.Lb1.pack()

    def actualizarlista(self):
        self.Lb1.destroy()
        self.crearlista()
        MessageBox.showinfo("Atualiza lista","Lista actualizada con exito!")
        
    def borrarvisita(self):
        indice = self.Lb1.curselection()
        #indice=indice[0]
        controle = Control()
        visitas = controle.leerdatabase()
        #print(indice)
        del visitas[indice[0]]
        controle.escribir(visitas)
        print('Deletando item')
        self.crearlista()
        
    def creartxt(self):
        indice = self.Lb1.curselection()
        indice = indice[0]
        controle = Control()
        visitas = controle.leerdatabase()
        for key, value in visitas[indice].items():
            nametxt= key
        print(f'{nametxt}.txt')
        with open(f'cerub/archivos/{nametxt}.txt', 'w') as f:
            f.write(f'\t\t\tRelatório Médico:\n')
            i = 0
            for key, value in visitas[indice].items():
                f.write(f'Nombre: {value['name']}\nMédico: {value['doctor']}')
            os.system(f'notepad.exe cerub/archivos/{nametxt}.txt')
            os.system(f'open -a TextEdit cerub/archivos/{nametxt}.txt')



    def guilista(self):
        
        self.top = Tk()
        self.top.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        self.top.geometry("800x720")  # set starting size of window
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
        ttk.Button(frame2, text='Imprimir', command=self.creartxt).grid(row=2, column=0, ipadx=2, ipady=2)
        ttk.Button(frame2, text='Borrar visita', command=self.borrarvisita).grid(row=3, column=0, ipadx=2, ipady=2)
        ttk.Button(frame2,  text='Salir', command = self.top.destroy).grid(row=4, column=0, ipadx=2, ipady=2)
        
        self.top.mainloop()

if __name__ == '__main__':
    menu = Listar()
    menu.guilista()