from tkinter import *
from tkinter import ttk
from pathlib import Path
import json

class Listar():
    def __init__(self):
        return None
    
    def guilista(self):
        
        top = Tk()
        top.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        top.geometry("1280x720")  # set starting size of window
        top.maxsize(1366, 768)  # width x height
        
        self.archivo = Path('cerub/archivos/pacientes.json')
        self.contenidoLista = self.archivo.read_text()
        self.lista = json.loads(self.contenidoLista)
        frame1 = ttk.Frame(top, padding="6 6 6 6")
        frame1.grid(column=0, row=0)
        self.Lb1 = Listbox(frame1, height=40, width=50)
        i=1
        for visita in self.lista:
            for key, value in visita.items():
                fecha = f'{key[6]}{key[7]}/{key[4]}{key[5]}/{key[0]}{key[1]}{key[2]}{key[3]}'
                hora = f'{key[9]}{key[10]}:{key[11]}{key[12]}:{key[13]}{key[14]}'
                self.Lb1.insert(i,f'{fecha} - {hora} - {value['name']}')
                i = i+1
        self.Lb1.pack()
        
        top.mainloop()

if __name__ == '__main__':
    menu = Listar()
    menu.guilista()