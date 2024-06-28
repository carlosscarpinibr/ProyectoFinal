from pathlib import Path
import json

class Control():
    def __init__(self):
        return None
    
    def controljson(self):
        while True:
            try:
                archivo = Path('cerub/archivos/pacientes.json')
                contenidoLista = archivo.read_text()
                break
            except FileNotFoundError:
                lista = []
                archivo = Path('cerub/archivos/pacientes.json')
                contenidoLista = json.dumps(lista)
                archivo.write_text(contenidoLista)
    
    def leerdatabase(self):
        archivo = Path('cerub/archivos/pacientes.json')
        contenidoLista = archivo.read_text()
        return contenidoLista
    
    def escribir(self, pacientes):
        archivo = Path('cerub/archivos/pacientes.json')
        contenidos = json.dumps(pacientes, indent=4, sort_keys=True)
        archivo.write_text(contenidos)