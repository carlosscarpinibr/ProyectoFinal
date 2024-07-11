from tkinter import *
from tkinter import ttk
from pathlib import Path
from cerub.controles.controlar import Control
import plotly.express as px
import json



class Estadistica():
    def __init__(self):
        return None
    
    def guiestadistica(self):
        # pantalla base
        etop = Tk()
        etop.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        etop.geometry("450x100")  # set starting size of window
        etop.maxsize(1366, 768)  # width x height
        
        frame1 = ttk.Frame(etop, padding="6 6 6 6")
        frame1.grid(column=0, row=0)
        ttk.Button(frame1,  text='Visualizar visita', command =self.generarhist).grid(row=1, column=0, ipadx=2, ipady=2)
        ttk.Button(frame1,  text='Actualizar lista de visitas', command =self.generarhist).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(frame1,  text='Salir', command = etop.destroy).grid(row=2, column=0, ipadx=2, ipady=2)
        
        # frame2 = ttk.Frame(etop, padding="6 6 6 6")
        # frame2.grid(column=1, row=0)
        # ttk.Button(frame2,  text='Visualizar visita', command =etop.destroy).grid(row=1, column=0, ipadx=2, ipady=2)
        # ttk.Button(frame2,  text='Actualizar lista de visitas', command =etop.destroy).grid(row=0, column=0, ipadx=2, ipady=2)
        # ttk.Button(frame2,  text='Salir', command = etop.destroy).grid(row=2, column=0, ipadx=2, ipady=2)
        
        # bucle de la aplicación
        etop.mainloop()
    
    def analisadatos(self):
        listaVisitas = []
        listaMedicos =[]
        #frecuencias1 = [4,1,3,2] 
        frecuencias = []
        controle = Control()
        visitas = controle.leerdatabase()
        # leitura de la visita
        for visit in visitas:
            for self.key, self.value in visit.items():
                listaVisitas.append(self.key)
                listaMedicos.append(self.value['doctor'])
                #print(f'{self.key}: {self.value['medicine']}')
        #print(len(listaMedicos))
        # frec = listaMedicos.count(listaMedicos[0])
        # print(f1)
        for i in range(len(listaMedicos)): 
            frec = listaMedicos.count(listaMedicos[i])
            frecuencias.append(frec)
        print(frecuencias)
        return listaMedicos, frecuencias
        
    def generarhist(self):
        titulo = 'Cuantidad de visitas por médico'
        etiquetas = {
                        'x': 'Médicos',
                        'y' : 'Numero de visitas'
                    }
        lista1, lista2 = self.analisadatos()
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()
        
        
if __name__ == '__main__':
    menu = Estadistica()
    menu.guiestadistica()
        
        
        
        

        
        
        
        