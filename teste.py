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
            'medicine' : medicacion.get(),
            'weight' : peso.get(),
            'date': fecha.get()
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
peso = StringVar()
fecha = StringVar()
medicacion = StringVar()
pac = StringVar()
r = StringVar()
i = 50


root.title("Nuevo paciente")
root.geometry("1024x768")  # set starting size of window
root.maxsize(1024, 768)  # width x height
root.config(bg="lightgrey")

# creamos el primer marco con su entry y su label

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="CENTRO DE INFUSÃO DE UBERLÂNDIA", bg="lightgrey")
enter_info.grid(row=0, column=3, columnspan=4, padx=5, pady=5)

# campo nombre
Label(root, text="Nombre:", bg="lightgrey").grid(row=2, column=1, padx=5, pady=5)
nombrem = Entry(root, textvariable = nombre, bd=3)
nombrem.grid(row=2, column=2,padx=5, pady=5)
nombrem.config(width=i)

# campo edad
Label(root, text="Edad:", bg="lightgrey").grid(row=2, column=3, padx=5, pady=5)
edadm = Entry(root, textvariable = edad, bd=3)
edadm.grid(row=2, column=4, padx=5, pady=5)
edadm.config(width=3)

# campo peso
Label(root, text="Peso:", bg="lightgrey").grid(row=2, column=5, padx=5, pady=5)
pesom = Entry(root, textvariable = peso, bd=3)
pesom.grid(row=2, column=6, padx=5, pady=5)
pesom.config(width=3)

# campo fecha
Label(root, text="Fecha:", bg="lightgrey").grid(row=2, column=7, padx=5, pady=5)
fecham = Entry(root, textvariable = fecha, bd=3)
fecham.grid(row=2, column=8, padx=5, pady=5)
fecham.config(width=11)


# creamos el segundo marco con su entry y su label

Label(root, text="Médico:", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5)
medicom = Entry(root, textvariable = medico, bd=3)
medicom.grid(row=3, column=2, padx=5, pady=5)
medicom.config(width=i)



# creamos el cuarto marco con su entry y su label
Label(root, text="Medicación:", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5)
medicacionm = Entry(root, textvariable = medicacion, bd=3)
medicacionm.grid(row=5, column=2, padx=5, pady=5)
medicacionm.config(width=i)

# botones
Button(root, text='Hello', command = hola).grid(row=8, column=1, padx=1, pady=1)
Button(root, text='Salvar', command = nuevo).grid(row=9, column=1, padx=1, pady=1)

# monitor
Label(root, text='\nTeste Hello:', bg="lightgrey").grid(row=6, column=1, padx=5, pady=5)
m1 = Entry(root, justify='center', textvariable = r, state='disable') # resultado
m1.grid(row=6, column=2, padx=5, pady=5)
m1.config(width=i)

Label(root, text='\nTeste Paciente:', bg="lightgrey").grid(row=7, column=1, padx=5, pady=5)
m2 = Entry(root, justify='center', textvariable = pac, state='disable') # resultado
m2.grid(row=7, column=2, padx=5, pady=5)
m2.config(width=i)


# bucle de la aplicación
root.mainloop()