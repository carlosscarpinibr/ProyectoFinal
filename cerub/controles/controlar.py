from pathlib import Path
import json
import os

class Control():
    def __init__(self):
        return None
    
    def controljson(self):
        '''
            - Descripción:
            Verifica si la carpeta con el archivo .json existe, si no existe crea la carpeta y el archivo. 
            - Entrada de datos:
            Leitura de los contenidos del archivo pacientes.json
            - Salida de datos:
            Una de las verificaciones para empezar el progama principal.
        '''
        while True:
            try:
                archivo = Path('archivos/pacientes.json')
                contenidoLista = archivo.read_text()
                break
            except FileNotFoundError:
                rutaArchivos ='archivos'
                os.mkdir(rutaArchivos)
                lista = []
                archivo = Path('archivos/pacientes.json')
                contenidoLista = json.dumps(lista)
                archivo.write_text(contenidoLista)
    
    def controlrelat(self):
        '''
            - Descripción:
            Verifica si la carpeta con el archivo .txt existe, si no existe crea la carpeta y el archivo. 
            - Entrada de datos:
            Leitura del contenido del archivo conteletxt.txt verificando la existencia de la carpeta.
            - Salida de datos:
            Una de las verificaciones para empezar el progama principal.
        '''
        while True:
            try:
                controltxt = Path('relat/controletxt.txt')
                contenido = controltxt.read_text(encoding='utf-8')
                break
            except FileNotFoundError:
                rutaRelat = 'relat'
                os.mkdir(rutaRelat)
                with open(f'relat/controletxt.txt', 'w') as archivotxt:
                    archivotxt.write('archivo de control de la carpeta')
        
    
    def leerdatabase(self):
        '''
            - Descripción:
            Rutina de leitura del archivo .json que es llamada por outras subrutinas del programa  
            - Entrada de datos:
            Realiza la leitura del archivo .json y lo almacena en una variable(list).
            - Salida de datos:
            Retorna la variable lista.
        '''
        archivo = Path('archivos/pacientes.json')
        contenidoLista = archivo.read_text()
        lista = json.loads(contenidoLista)
        return lista
    
    def escribir(self, pacientes):
        '''
            - Descripción:
            Rutina de escrita en el archivo .json que es llamada por outras subrutinas del programa  
            - Entrada de datos:
            Recibe una variable lista y la cpoia para el archivo .json
            - Salida de datos:
            El archivo .json actualizado.
        '''
        archivo = Path('archivos/pacientes.json')
        contenidos = json.dumps(pacientes, indent=4, sort_keys=True)
        archivo.write_text(contenidos)
        
    