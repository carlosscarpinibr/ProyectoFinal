from pathlib import Path
import json
import os

class Control():
    def __init__(self):
        return None
    
    def controljson(self):
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
        while True:
            try:
                controltxt = Path('relat/controletxt.txt')
                contenido = controltxt.read_text(encoding='utf-8')
                break
            except FileNotFoundError:
                rutaRelat = 'relat'
                os.mkdir(rutaRelat)
                with open(f'relat/controletxt.txt', 'w') as archivotxt:
                    archivotxt.write('archivo de cotrole de la carpeta')
                break
        
    
    def leerdatabase(self):
        archivo = Path('archivos/pacientes.json')
        contenidoLista = archivo.read_text()
        lista = json.loads(contenidoLista)
        return lista
    
    def escribir(self, pacientes):
        archivo = Path('archivos/pacientes.json')
        contenidos = json.dumps(pacientes, indent=4, sort_keys=True)
        archivo.write_text(contenidos)
        
    