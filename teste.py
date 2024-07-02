from tkinter import *
from pathlib import Path
import json
import time

def hola():
    r.set(f'Hola Mundo!!!')
    return r


def nuevo():
    archivo = Path('cerub/archivos/pacientes.json')
    contenidoLista = archivo.read_text()
    lista = json.loads(contenidoLista)
    timestamp = f'{time.strftime("%Y")}{time.strftime("%m")}{time.strftime("%d")}_{time.strftime("%H")}{time.strftime("%M")}{time.strftime("%S")}'
    nuevoPaciente = {timestamp:{
            'name' : nombre.get(),
            'surename' : apellido.get(),
            'age' : edad.get(),
            'mail' : email.get()
        }}
    #pac.set(f'{nombre.get()},{apellido.get()},{edad.get()},{email.get()}')
    #pac.set(f'{timestamp},{nuevoPaciente['name']},{nuevoPaciente['surename']},{nuevoPaciente['age']},{nuevoPaciente['mail']}')
    pac.set(f'Paciente salvo')
    lista.append(nuevoPaciente)
    contenidos = json.dumps(lista, indent=4, sort_keys=True)
    archivo.write_text(contenidos)
    return pac




# configuración de la raíz
root = Tk()

# creamos las variables de texto
nombre = StringVar()
apellido = StringVar()
edad = StringVar()
email = StringVar()
pac = StringVar()
r = StringVar()


root.title("Nuevo paciente")
root.geometry("640x480")  # set starting size of window
root.maxsize(640, 480)  # width x height
root.config(bg="lightgrey")

# creamos el primer marco con su entry y su label

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="Introduzca los datos del paciente: ", bg="lightgrey")
enter_info.grid(row=0, column=2, columnspan=4, padx=5, pady=5)

# Name label and entry widgets
Label(root, text="Nombre", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5, sticky=E)

nombrem = Entry(root, textvariable = nombre, bd=3)
nombrem.grid(row=2, column=2, padx=5, pady=5)

# creamos el segundo marco con su entry y su label

Label(root, text="Apellido", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5, sticky=E)
apellidom = Entry(root, textvariable = apellido, bd=3)
apellidom.grid(row=3, column=2, padx=5, pady=5)

# creamos el tercer marco con su entry y su label
Label(root, text="Edad", bg="lightgrey").grid(row=4, column=1, padx=5, pady=5, sticky=E)
#Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)

edadm = Entry(root, textvariable = edad, bd=3)
edadm.grid(row=4, column=2, padx=5, pady=5)

Label(root, text="E-mail", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5, sticky=E)
#Label(root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)

# creamos el cuarto marco con su entry y su label
emailm = Entry(root, textvariable = email, bd=3)
emailm.grid(row=5, column=2, padx=5, pady=5)

# botones
Button(root, text='Hello', command = hola).grid(row=6, column=2, padx=5, pady=5, sticky=E)
Button(root, text='Salvar', command = nuevo).grid(row=9, column=2, padx=5, pady=5, sticky=E)

# monitor
Label(root, text='\nTeste Hello').grid(row=7, column=2, padx=5, pady=5, sticky=E)
Entry(root, justify='center', textvariable = r, state='disable').grid(row=8, column=2, padx=5, pady=5, sticky=E) # resultado

Label(root, text='\nTeste Paciente').grid(row=10, column=2, padx=5, pady=5, sticky=E)
Entry(root, justify='center', textvariable = pac, state='disable').grid(row=11, column=2, padx=5, pady=5, sticky=E) # resultado



# bucle de la aplicación
root.mainloop()