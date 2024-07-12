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
        '''
            - Descripción:
            Pantalla del menu estadistica 
            - Entrada de datos:
            Los parametros de configuración de la pantalla como frame, buttons, title y combobox.
            - Salida de datos:
            Una pantalla en que se puede eligir 4 tipos distintos de histogramas y generalos.
        '''
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
        self.parametro.current(0)
        self.parametro.grid(row=0, column=0, ipadx=2, ipady=2)
        
        
        # bucle de la aplicación
        self.etop.mainloop()
    
    def generaselecion(self):
        '''
            - Descripción:
            Valores preestabelecidos del combobox para generación del histograma 
            - Entrada de datos:
            El usuario elige que parametro será presentado en el histograma junto con el numero de visitas registradas en el programa
            - Salida de datos:
            El histograma elegido por el usuario.
        '''
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
        '''
            - Descripción:
            Analisa el parametro elegido en el combobox para generar las lista que sirviran para crear el histograma.
            - Entrada de datos:
            Una clave de diccionário, para recoger los datos de las visitas registradas en el programa
            - Salida de datos:
            Dos lista que serán utilizadas por las funciones que crearán los graficos.
        '''
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
        '''
            - Descripción:
            Genera el histograma con el numero de médicos por numero de visitas registrada en el software.
            - Entrada de datos:
            Una lista con los medicos encontrados y una lista con la frequencia de visitas por médico.
            - Salida de datos:
            Un histograma generado con el matplotlib con los médicos registrados y la cantidad de visitas registradas.
        '''
        titulo = 'Cuantidad de visitas por médico'
        etiquetas = {
                        'x': 'Médicos',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()

    def generarhistnombres(self, lista1, lista2):
        '''
            - Descripción:
            Genera el histograma con el numero de pacientes por numero de visitas registrada en el software.
            - Entrada de datos:
            Una lista con los pacientes encontrados y una lista con la frequencia de visitas por médico.
            - Salida de datos:
            Un histograma generado con el matplotlib con los pacientes registrados y la cantidad de visitas registradas.
        '''
        titulo = 'Cuantidad de visitas por paciente'
        etiquetas = {
                        'x': 'Paciente',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()

    def generarhistequipo(self,lista1,lista2):
        '''
            - Descripción:
            Genera el histograma con el numero equipos por numero de visitas registrada en el software.
            - Entrada de datos:
            Una lista con los equipos encontrados y una lista con la frequencia de visitas por médico.
            - Salida de datos:
            Un histograma generado con el matplotlib con los equipos registrados y la cantidad de visitas registradas.
        '''
        titulo = 'Cuantidad de visitas por equipo'
        etiquetas = {
                        'x': 'Equipo',
                        'y' : 'Numero de visitas'
                    }
        fig = px.bar(x=lista1, y=lista2,title=titulo, labels=etiquetas)
        fig.show()    
        
    def generarhistmedicacion(self,lista1,lista2):
        '''
            - Descripción:
            Genera el histograma con el numero medicacion por numero de visitas registrada en el software.
            - Entrada de datos:
            Una lista con las medicaciones encontradas y una lista con la frequencia de visitas por médico.
            - Salida de datos:
            Un histograma generado con el matplotlib con las medicaciones registradas y la cantidad de visitas registradas.
        '''
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
        
        
        
        

        
        
        
        