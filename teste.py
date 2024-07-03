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
            'doctor' : medico.get(),
            'age' : edad.get(),
            'medicine' : medicacion.get()
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
medico = StringVar()
edad = StringVar()
medicacion = StringVar()
pac = StringVar()
r = StringVar()
i = 70


root.title("Nuevo paciente")
root.geometry("640x480")  # set starting size of window
root.maxsize(640, 480)  # width x height
root.config(bg="lightgrey")

# creamos el primer marco con su entry y su label

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="Introduzca los datos del paciente: ", bg="lightgrey")
enter_info.grid(row=0, column=2, columnspan=4, padx=5, pady=5)

# Name label and entry widgets
Label(root, text="Nombre:", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5)

nombrem = Entry(root, textvariable = nombre, bd=3)
nombrem.grid(row=2, column=2,padx=5, pady=5)
nombrem.config(width=i)

# creamos el segundo marco con su entry y su label

Label(root, text="Médico", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5)
medicom = Entry(root, textvariable = medico, bd=3)
medicom.grid(row=3, column=2, padx=5, pady=5)
medicom.config(width=i)
# creamos el tercer marco con su entry y su label
Label(root, text="Edad", bg="lightgrey").grid(row=4, column=1, padx=5, pady=5)
#Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)

edadm = Entry(root, textvariable = edad, bd=3)
edadm.grid(row=4, column=2, padx=5, pady=5)
edadm.config(width=i)

Label(root, text="Medicación", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5)
#Label(root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)

# creamos el cuarto marco con su entry y su label
medicacionm = Entry(root, textvariable = medicacion, bd=3)
medicacionm.grid(row=5, column=2, padx=5, pady=5)
medicacionm.config(width=i)

# botones
Button(root, text='Hello', command = hola).grid(row=8, column=1, padx=5, pady=5)
Button(root, text='Salvar', command = nuevo).grid(row=9, column=1, padx=5, pady=5)

# monitor
Label(root, text='\nTeste Hello').grid(row=6, column=1, padx=5, pady=5)
Entry(root, justify='center', textvariable = r, state='disable').grid(row=6, column=2, padx=1, pady=1) # resultado

Label(root, text='\nTeste Paciente').grid(row=7, column=1, padx=5, pady=5)
Entry(root, justify='center', textvariable = pac, state='disable').grid(row=7, column=2, padx=1, pady=1) # resultado



# bucle de la aplicación
root.mainloop()