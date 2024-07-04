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
            'date': fecha.get(),
            'insurance' : seguro.get(),
            'seat' : poltrona.get(),
            'birthday' : fechaNasm.get(),
            'team' : equipo.get(),
            'doses' : dosis.get(),
            'TIME1' : horario1.get(),
            'TIME2' : horario2.get(),
            'TIME3' : horario3.get(),
            'PA1' : pa1.get(),
            'PA2' : pa2.get(),
            'PA3' : pa3.get(),
            'FC1' : fc1.get(),
            'FC2' : fc2.get(),
            'FC3' : fc3.get(),
            'FR1' : fr1.get(),
            'FR2' : fr2.get(),
            'FR3' : fr3.get(),
            'SPO21' : spo21.get(),
            'SPO22' : spo22.get(),
            'SPO23' : spo23.get(),
            'TEMP1' : temp1.get(),
            'TEMP2' : temp2.get(),
            'TEMP3' : temp3.get(),
            'FIRMA1' : firma1.get(),
            'FIRMA2' : firma2.get(),
            'FIRMA3' : firma3.get(),
            'admission' : admision.get(),
            'origin' : origin.get(),
            'arrive' : llegada.get(),
            'puncture' : puncion.get(),
            'procedure' : procedimiento.get()

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
edad = StringVar()
peso = StringVar()
fecha = StringVar()
medico = StringVar()
seguro = StringVar()
poltrona = StringVar()
fechaNas = StringVar()
medicacion = StringVar()
dosis = StringVar()
equipo = StringVar()
horario1 = StringVar()
horario2 = StringVar()
horario3 = StringVar()
pa1 = StringVar()
pa2 = StringVar()
pa3 = StringVar()
fc1 = StringVar()
fc2 = StringVar()
fc3 = StringVar()
fr1 = StringVar()
fr2 = StringVar()
fr3 = StringVar()
spo21 = StringVar()
spo22 = StringVar()
spo23 = StringVar()
temp1 = StringVar()
temp2 = StringVar()
temp3 = StringVar()
firma1 = StringVar()
firma2 = StringVar()
firma3 = StringVar()
admision = StringVar()
origin = StringVar()
procedimiento = StringVar()
llegada = StringVar()
puncion = StringVar()
pac = StringVar()
r = StringVar()
i = 50


root.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
root.geometry("1024x768")  # set starting size of window
root.maxsize(1024, 768)  # width x height
root.config(bg="lightgrey")



# titulo de la pantalla
enter_info = Label(root, text="NUEVA VISITA", bg="lightgrey")
enter_info.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

# campo nombre
Label(root, text="Nombre:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
nombrem = Entry(root, textvariable = nombre, bd=3)
nombrem.grid(row=2, column=1,padx=5, pady=5)
nombrem.config(width=i)

# campo edad
Label(root, text="Edad:", bg="lightgrey").grid(row=2, column=2, padx=5, pady=5)
edadm = Entry(root, textvariable = edad, bd=3)
edadm.grid(row=2, column=3, padx=5, pady=5)
edadm.config(width=6)

# campo peso
Label(root, text="Peso:", bg="lightgrey").grid(row=2, column=4, padx=5, pady=5)
pesom = Entry(root, textvariable = peso, bd=3)
pesom.grid(row=2, column=5, padx=5, pady=5)
pesom.config(width=3)

# campo fecha
Label(root, text="Fecha:", bg="lightgrey").grid(row=2, column=6, padx=5, pady=5)
fecham = Entry(root, textvariable = fecha, bd=3)
fecham.grid(row=2, column=7, padx=5, pady=5)
fecham.config(width=11)


# campo médico
Label(root, text="Médico:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
medicom = Entry(root, textvariable = medico, bd=3)
medicom.grid(row=3, column=1, padx=5, pady=5)
medicom.config(width=i)

# campo seguro
Label(root, text="Seguro:", bg="lightgrey").grid(row=3, column=2, padx=5, pady=5)
segurom = Entry(root, textvariable = seguro, bd=3)
segurom.grid(row=3, column=3, padx=5, pady=5, sticky=W)
segurom.config(width=6)

# campo poltrona
Label(root, text="Poltrona:", bg="lightgrey").grid(row=3, column=4, padx=5, pady=5)
poltronam = Entry(root, textvariable = poltrona, bd=3)
poltronam.grid(row=3, column=5, padx=5, pady=5)
poltronam.config(width=3)

# campo fecha nacimento
Label(root, text="F/N:", bg="lightgrey").grid(row=3, column=6, padx=5, pady=5)
fechaNasm = Entry(root, textvariable = fechaNas, bd=3)
fechaNasm.grid(row=3, column=7, padx=5, pady=5)
fechaNasm.config(width=11)

# campo medicación
Label(root, text="Medicación:", bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
medicacionm = Entry(root, textvariable = medicacion, bd=3)
medicacionm.grid(row=5, column=1, padx=5, pady=5)
medicacionm.config(width=i)

# campo dosis
Label(root, text="Dosis:", bg="lightgrey").grid(row=5, column=2, padx=5, pady=5)
dosism = Entry(root, textvariable = dosis, bd=3)
dosism.grid(row=5, column=3, padx=5, pady=5)
dosism.config(width=6)

# campo equipo
Label(root, text="Equipo:", bg="lightgrey").grid(row=6, column=0, padx=5, pady=5)
equipom = Entry(root, textvariable = equipo, bd=3)
equipom.grid(row=6, column=1, padx=5, pady=5)
equipom.config(width=i)

# campo admision
Label(root, text="Admisión:", bg="lightgrey").grid(row=7, column=0, padx=5, pady=5)
admisionm = Entry(root, textvariable = admision, bd=3)
admisionm.grid(row=7, column=1, padx=5, pady=5, sticky=W)
admisionm.config(width=5)

# campo origin
Label(root, text="Origin:", bg="lightgrey").grid(row=8, column=0, padx=5, pady=5)
originm = Entry(root, textvariable = origin, bd=3)
originm.grid(row=8, column=1, padx=5, pady=5)
originm.config(width=i)

# campo procedimento
Label(root, text="Procedimiento:", bg="lightgrey").grid(row=9, column=0, padx=5, pady=5)
procedimientom = Entry(root, textvariable = procedimiento, bd=3)
procedimientom.grid(row=9, column=1, padx=5, pady=5)
procedimientom.config(width=i)

# campo estado llegada
Label(root, text="Llegada:", bg="lightgrey").grid(row=10, column=0, padx=5, pady=5)
llegadam = Entry(root, textvariable = llegada, bd=3)
llegadam.grid(row=10, column=1, padx=5, pady=5)
llegadam.config(width=i)

# campo puncion
Label(root, text="Punción:", bg="lightgrey").grid(row=11, column=0, padx=5, pady=5)
puncionm = Entry(root, textvariable = puncion, bd=3)
puncionm.grid(row=11, column=1, padx=5, pady=5)
puncionm.config(width=i)




# titulo de SEÑALES VITALES
enter_info = Label(root, text="SEÑALES VITALES", bg="lightgrey")
enter_info.grid(row=7, column=5, columnspan=5, padx=5, pady=5,sticky=W)

# titulo de horário
enter_info = Label(root, text="Horário", bg="lightgrey")
enter_info.grid(row=8, column=3, padx=5, pady=5)

# titulo de PA
enter_info = Label(root, text="PA", bg="lightgrey")
enter_info.grid(row=8, column=4, padx=5, pady=5, sticky=N)

# titulo de FC
enter_info = Label(root, text="FC", bg="lightgrey")
enter_info.grid(row=8, column=5, padx=5, pady=5)

# titulo de FR
enter_info = Label(root, text="FR", bg="lightgrey")
enter_info.grid(row=8, column=6, padx=5, pady=5)

# titulo de Spo2
enter_info = Label(root, text="SpO2", bg="lightgrey")
enter_info.grid(row=8, column=7, padx=5, pady=5)

# titulo de Tº
enter_info = Label(root, text="Tº", bg="lightgrey")
enter_info.grid(row=8, column=8, padx=5, pady=5, sticky=W)

# titulo firma
enter_info = Label(root, text="Firma", bg="lightgrey")
enter_info.grid(row=8, column=9, padx=5, pady=5)

# campo horario 1
horario1m = Entry(root, textvariable = horario1, bd=3)
horario1m.grid(row=9, column=3, padx=5, pady=5)
horario1m.config(width=5)

# campo pa 1
pa1m = Entry(root, textvariable = pa1, bd=3)
pa1m.grid(row=9, column=4, padx=5, pady=5)
pa1m.config(width=5)

# campo fc 1
fc1m = Entry(root, textvariable = fc1, bd=3)
fc1m.grid(row=9, column=5, padx=5, pady=5)
fc1m.config(width=3)

# campo fr 1
fr1m = Entry(root, textvariable = fr1, bd=3)
fr1m.grid(row=9, column=6, padx=5, pady=5)
fr1m.config(width=3)

# campo spo2 1
spo21m = Entry(root, textvariable = spo21, bd=3)
spo21m.grid(row=9, column=7, padx=5, pady=5)
spo21m.config(width=11)

# campo Tº 1
temp1m = Entry(root, textvariable = temp1, bd=3)
temp1m.grid(row=9, column=8, padx=5, pady=5, sticky=W)
temp1m.config(width=3)

# campo firma 1
firma1m = Entry(root, textvariable = firma1, bd=3)
firma1m.grid(row=9, column=9, padx=5, pady=5)
firma1m.config(width=8)

# campo horario 2
horario2m = Entry(root, textvariable = horario2, bd=3)
horario2m.grid(row=10, column=3, padx=5, pady=5)
horario2m.config(width=5)

# campo pa 2
pa2m = Entry(root, textvariable = pa2, bd=3)
pa2m.grid(row=10, column=4, padx=5, pady=5)
pa2m.config(width=5)

# campo fc 2
fc2m = Entry(root, textvariable = fc2, bd=3)
fc2m.grid(row=10, column=5, padx=5, pady=5)
fc2m.config(width=3)

# campo fr 2
fr2m = Entry(root, textvariable = fr2, bd=3)
fr2m.grid(row=10, column=6, padx=5, pady=5)
fr2m.config(width=3)

# campo spo2 2
spo22m = Entry(root, textvariable = spo22, bd=3)
spo22m.grid(row=10, column=7, padx=5, pady=5)
spo22m.config(width=11)

# campo Tº 2
temp2m = Entry(root, textvariable = temp2, bd=3)
temp2m.grid(row=10, column=8, padx=5, pady=5, sticky=W)
temp2m.config(width=3)

# campo firma 2
firma2m = Entry(root, textvariable = firma2, bd=3)
firma2m.grid(row=10, column=9, padx=5, pady=5)
firma2m.config(width=8)

# campo horario 3
horario3m = Entry(root, textvariable = horario3, bd=3)
horario3m.grid(row=11, column=3, padx=5, pady=5)
horario3m.config(width=5)

# campo pa 3
pa3m = Entry(root, textvariable = pa3, bd=3)
pa3m.grid(row=11, column=4, padx=5, pady=5)
pa3m.config(width=5)

# campo fc 3
fc3m = Entry(root, textvariable = fc3, bd=3)
fc3m.grid(row=11, column=5, padx=5, pady=5)
fc3m.config(width=3)

# campo fr 3
fr3m = Entry(root, textvariable = fr3, bd=3)
fr3m.grid(row=11, column=6, padx=5, pady=5)
fr3m.config(width=3)

# campo spo2 3
spo23m = Entry(root, textvariable = spo23, bd=3)
spo23m.grid(row=11, column=7, padx=5, pady=5)
spo23m.config(width=11)

# campo Tº 3
temp3m = Entry(root, textvariable = temp3, bd=3)
temp3m.grid(row=11, column=8, padx=5, pady=5, sticky=W)
temp3m.config(width=3)

# campo firma 3
firma3m = Entry(root, textvariable = firma3, bd=3)
firma3m.grid(row=11, column=9, padx=5, pady=5)
firma3m.config(width=8)




# campo horario 4
horario4m = Entry(root, textvariable = horario4, bd=3)
horario4m.grid(row=12, column=3, padx=5, pady=5)
horario4m.config(width=5)

# campo pa 4
pa4m = Entry(root, textvariable = pa4, bd=3)
pa4m.grid(row=12, column=4, padx=5, pady=5)
pa4m.config(width=5)

# campo fc 4
fc4m = Entry(root, textvariable = fc4, bd=3)
fc4m.grid(row=12, column=5, padx=5, pady=5)
fc4m.config(width=3)

# campo fr 4
fr4m = Entry(root, textvariable = fr4, bd=3)
fr4m.grid(row=12, column=6, padx=5, pady=5)
fr4m.config(width=3)

# campo spo2 4
spo24m = Entry(root, textvariable = spo24, bd=3)
spo24m.grid(row=12, column=7, padx=5, pady=5)
spo24m.config(width=11)

# campo Tº 4
temp4m = Entry(root, textvariable = temp4, bd=3)
temp4m.grid(row=12, column=8, padx=5, pady=5, sticky=W)
temp4m.config(width=3)

# campo firma 4
firma4m = Entry(root, textvariable = firma4, bd=3)
firma4m.grid(row=12, column=9, padx=5, pady=5)
firma4m.config(width=8)



# titulo de ANOTACIÓN / EVOLUCIÓN DE ENFERMAGEM
enter_info = Label(root, text="ANOTACIÓN / EVOLUCIÓN DE ENFERMAGEM", bg="lightgrey")
enter_info.grid(row=12, column=0, columnspan=3, padx=5, pady=5)

# campo ANOTACIÓN / EVOLUCIÓN DE ENFERMAGEM
texto = Text(root)
texto.grid(row=13, column=0, columnspan=3, padx=5, pady=5)
texto.config(width=i, height= 5) # carácteres
texto.config(font=('Arial', 12),padx=5, pady=5,selectbackground='red')



# botones
Button(root, text='Hello', command = hola).grid(row=17, column=1, padx=1, pady=1)
Button(root, text='Salvar', command = nuevo).grid(row=18, column=1, padx=1, pady=1)

# monitores
Label(root, text='\nTeste Hello:', bg="lightgrey").grid(row=19, column=0, padx=5, pady=5)
m1 = Entry(root, justify='center', textvariable = r, state='disable')
m1.grid(row=19, column=1, padx=5, pady=5)
m1.config(width=i)

Label(root, text='\nTeste Paciente:', bg="lightgrey").grid(row=20, column=0, padx=5, pady=5)
m2 = Entry(root, justify='center', textvariable = pac, state='disable')
m2.grid(row=20, column=1, padx=5, pady=5)
m2.config(width=i)


# bucle de la aplicación
root.mainloop()