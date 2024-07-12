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
                rutaRelat = 'relat'
                os.mkdir(rutaArchivos)
                os.mkdir(rutaRelat)
                lista = []
                archivo = Path('archivos/pacientes.json')
                contenidoLista = json.dumps(lista)
                archivo.write_text(contenidoLista)
    
    def leerdatabase(self):
        archivo = Path('archivos/pacientes.json')
        contenidoLista = archivo.read_text()
        lista = json.loads(contenidoLista)
        return lista
    
    def escribir(self, pacientes):
        archivo = Path('archivos/pacientes.json')
        contenidos = json.dumps(pacientes, indent=4, sort_keys=True)
        archivo.write_text(contenidos)
        
    