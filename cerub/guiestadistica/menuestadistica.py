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
        self.etop = Tk()
        self.etop.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        self.etop.geometry("450x100")  # set starting size of window
        self.etop.maxsize(1366, 768)  # width x height
        
        self.frame1 = ttk.Frame(self.etop, padding="6 6 6 6")
        self.frame1.grid(column=0, row=0)
        ttk.Button(self.frame1,  text='Generar histograma', command=self.generaselecion).grid(row=0, column=0, ipadx=2, ipady=2)
        ttk.Button(self.frame1,  text='Salir', command = self.etop.destroy).grid(row=2, column=0, ipadx=2, ipady=2)
        
        self.opciones = ['Nombre','Médico','Equipo','Medicación']
        self.frame2 = ttk.Frame(self.etop, padding="6 6 6 6")
        self.frame2.grid(column=1, row=0)
        self.parametro = ttk.Combobox(self.frame2,  values = self.opciones, state='readyonly')
        self.parametro.grid(row=0, column=0, ipadx=2, ipady=2)
        
        # bucle de la aplicación
        self.etop.mainloop()
    
    def generaselecion(self):
        if self.parametro.get() == 'Nombre':
            campo = 'name'
            listaA, listaB = self.analisadatos(campo)
            self.generarhistnombres(listaA,listaB)
        elif self.parametro.get() == 'Médico':
            campo = 'doctor'
            listaA, listaB = self.analisadatos(campo)
            self.generarhistnombres(listaA,listaB)
        elif self.parametro.get() == 'Equipo':
            campo = 'team'
            listaA, listaB = self.analisadatos(campo)
            self.generarhistnombres(listaA,listaB)
        elif self.parametro.get() == 'Medicación':
            campo = 'medicine'
            listaA, listaB = self.analisadatos(campo)
            self.generarhistnombres(listaA,listaB)
        


    
    def analisadatos(self,campo):
        listaX = []
        listaY =[]
        frecuencias = []
        controle = Control()
        visitas = controle.leerdatabase()
        for visit in visitas:
            for self.key, self.value in visit.items():
                listaY.append(self.key)
                listaX.append(self.value[campo])
        for i in range(len(listaX)):
            frecuencias.append(1)
        return listaX, frecuencias
        
    def generarhistmedicos(self,lista1, lista2):
        titulo = 'Cuantidad de visitas por médico'
        etiquetas = {
                        'x': 'Médicos',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()

    def generarhistnombres(self, lista1, lista2):
        titulo = 'Cuantidad de visitas por paciente'
        etiquetas = {
                        'x': 'Paciente',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()

    def generarhistequipo(self,lista1,lista2):
        titulo = 'Cuantidad de visitas por equipo'
        etiquetas = {
                        'x': 'Equipo',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()    
        
    def generarhistmedicacion(self,lista1,lista2):
        titulo = 'Cuantidad de visitas por medicación'
        etiquetas = {
                        'x': 'Medicación',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()

if __name__ == '__main__':
    menu = Estadistica()
    menu.guiestadistica()
        
        
        
        

        
        
        
        