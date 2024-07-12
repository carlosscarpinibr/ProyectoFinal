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
        '''
            - Descripción:
            Recoge el indice de una visita de la lista y envia para la revision de visita.
            - Entrada de datos:
            Una tupla con el valor del indice de la lista de visistas
            - Salida de datos:
            El valor del indice de la lista de visitas y la visita(dict) correspondiente para abrir la pantalla de revisión de visita.
        '''
        indice = self.Lb1.curselection()
        self.r = Revision()
        while True:
            try:
                self.r.guirevision(indice[0],self.lista[indice[0]])
                break
            except IndexError:
                MessageBox.showerror("Atención","Seleccione una visita en la lista para visualizar.")
                break
        

    def crearlista(self):
        '''
            - Descripción:
            Crea en pantalla la lista de visitas registrada en el programa.
            - Entrada de datos:
            Una lista adquirida en la clase Control correspondiente ao datos del archivo .json.
            - Salida de datos:
            Un listbox en pantalla con las visitas organizadas por fecha y hora de registro.
        '''
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
        '''
            - Descripción:
            Actualiza el listbox en pantalla.
            - Entrada de datos:
            Con un click en el boton Actualiza lista elimina el listbox.
            - Salida de datos:
            Crea un nuevo lisbox actualizado.
        '''
        self.Lb1.destroy()
        self.crearlista()
        MessageBox.showinfo("Atualiza lista","Lista actualizada con exito!")
        
    def borrarvisita(self):
        '''
            - Descripción:
           Borra una visita de la lista de vistas.
            - Entrada de datos:
            Con un click en borra visita elimina la vista del programa.
            - Salida de datos:
            Crea un nuevo lisbox actualizado.
        '''
        indice = self.Lb1.curselection()
        controle = Control()
        visitas = controle.leerdatabase()
        while True:
            try:
                del visitas[indice[0]]
                controle.escribir(visitas)
                self.crearlista()
                MessageBox.showinfo("Visita borrada","Visita borrada con exito!")
                break
            except IndexError:
                MessageBox.showerror("Atención","Seleccione una visita en la lista para borrar.")
                break
        
        
        
    def imprimirvisita(self):
        '''
            - Descripción:
           Crea un archivo de texto con los datos de la visita para impresión.
            - Entrada de datos:
            Con un click en el boton imprimir visita genera el archivo .txt en la carpeta relat.
            - Salida de datos:
            Presenta el archivo en pantalla para impresión.
        '''
        controle = Control()
        visitas = controle.leerdatabase()
        while True:
            try:
                indice = self.Lb1.curselection()
                indice = indice[0]
                for key, value in visitas[indice].items():
                    nombretxt = key
                with open(f'relat/{nombretxt}.txt', 'w') as f:
                    f.write(f'\t\t\tCERUB - CENTRO DE INFUSÃO DE UBERLÂNDIA\n\n\t\t\t\tRelatório Médico\n\n\n')
                    for key, value in visitas[indice].items():
                        f.write(f'Nombre: {value['name']}\t\tEdad: {value['age']}\tFecha: {value['date']}\nMédico: {value['doctor']}\t\t\tSeguro: {value['insurance']}\nMedicación: {value['medicine']}\t\t\tDosis: {value['doses']}\nEquipo: {value['team']}\nAdmisión: {value['admission']}')
                os.system(f'notepad.exe relat/{nombretxt}.txt')
                os.system(f'open -a TextEdit relat/{nombretxt}.txt')
                break
            except IndexError:
                MessageBox.showerror("Atención","Seleccione una visita en la lista para imprimir.")
                break



    def guilista(self):
        '''
            - Descripción:
            Pantalla del menu gerenciar vistas
            - Entrada de datos:
            Los parametros de configuración de la pantalla como frame, buttons, title y listbox.
            - Salida de datos:
            Una pantalla en que se puede seleccionar una visita y revisala, imprimila, borrala.
            Hay también un boton para actualizar la lista y salir da pantalla.
        '''
        
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
        ttk.Button(frame2, text='Imprimir visita', command=self.imprimirvisita).grid(row=2, column=0, ipadx=2, ipady=2)
        ttk.Button(frame2, text='Borrar visita', command=self.borrarvisita).grid(row=3, column=0, ipadx=2, ipady=2)
        ttk.Button(frame2,  text='Salir', command = self.top.destroy).grid(row=4, column=0, ipadx=2, ipady=2)
        
        self.top.mainloop()

if __name__ == '__main__':
    menu = Listar()
    menu.guilista()