from tkinter import *
from tkinter import ttk
from pathlib import Path
import json
import time

class Revision():
    def __init__(self):
        return None
    
    def nuevo(self):
        self.archivo = Path('cerub/archivos/pacientes.json')
        self.contenidoLista = self.archivo.read_text()
        self.lista = json.loads(self.contenidoLista)
        self.timestamp = f'{time.strftime("%Y")}{time.strftime("%m")}{time.strftime("%d")}_{time.strftime("%H")}{time.strftime("%M")}{time.strftime("%S")}'
        #print("aqui", self.nombre.get())
        self.nuevoPaciente = {self.timestamp:{
                'name' : self.nombrem.get(),
                'doctor' : self.medicom.get(),
                'age' : self.edadm.get(),
                'medicine' : self.medicacionm.get(),
                'weight' : self.pesom.get(),
                'date': self.fecham.get(),
                'insurance' : self.segurom.get(),
                'seat' : self.poltronam.get(),
                'birthday' : self.fechaNasm.get(),
                'team' : self.equipom.get(),
                'doses' : self.dosism.get(),
                'TIME1' : self.horario1m.get(),
                'TIME2' : self.horario2m.get(),
                'TIME3' : self.horario3m.get(),
                'TIME4' : self.horario4m.get(),
                'PA1' : self.pa1m.get(),
                'PA2' : self.pa2m.get(),
                'PA3' : self.pa3m.get(),
                'PA4' : self.pa4m.get(), 
                'FC1' : self.fc1m.get(),
                'FC2' : self.fc2m.get(),
                'FC3' : self.fc3m.get(),
                'FC4' : self.fc4m.get(),
                'FR1' : self.fr1m.get(),
                'FR2' : self.fr2m.get(),
                'FR3' : self.fr3m.get(),
                'FR4' : self.fr4m.get(),
                'SPO21' : self.spo21m.get(),
                'SPO22' : self.spo22m.get(),
                'SPO23' : self.spo23m.get(),
                'SPO24' : self.spo24m.get(),
                'TEMP1' : self.temp1m.get(),
                'TEMP2' : self.temp2m.get(),
                'TEMP3' : self.temp3m.get(),
                'TEMP4' : self.temp4m.get(),
                'FIRMA1' : self.firma1m.get(),
                'FIRMA2' : self.firma2m.get(),
                'FIRMA3' : self.firma3m.get(),
                'FIRMA4' : self.firma4m.get(),
                'admission' : self.admisionm.get(),
                'origin' : self.originm.get(),
                'arrive' : self.llegadam.get(),
                'puncture' : self.puncionm.get(),
                'procedure' : self.procedimientom.get()

            }}
        
        #pac.set(f'{nombre.get()},{apellido.get()},{edad.get()},{email.get()}')
        #pac.set(f'{timestamp},{nuevoPaciente['name']},{nuevoPaciente['surename']},{nuevoPaciente['age']},{nuevoPaciente['mail']}')
        #self.pac = StringVar()
        #time.sleep(5)
        #self.pac.set(f'Paciente salvo')
        self.lista[self.indice] = self.nuevoPaciente
        self.contenidos = json.dumps(self.lista, indent=4, sort_keys=True)
        self.archivo.write_text(self.contenidos)
        #return self.pac

    # def hola(self):
    #     #self.r = StringVar()
    #     self.r.set(f'Hola Mundo!!!')
    #     return self.r

    def guirevision(self, indice, visit):
        # configuración de la raíz
        self.root = Tk()
        #time.sleep(5)
        for key, value in visit.items():
            pass
        self.indice = indice
        #print(type(value['name']))



        # creamos las variables de texto
        self.nombre = StringVar()
        self.edad = StringVar()
        self.peso = StringVar()
        self.fecha = StringVar()
        self.medico = StringVar()
        self.seguro = StringVar()
        self.poltrona = StringVar()
        self.fechaNas = StringVar()
        self.medicacion = StringVar()
        self.dosis = StringVar()
        self.equipo = StringVar()
        self.horario1 = StringVar()
        self.horario2 = StringVar()
        self.horario3 = StringVar()
        self.horario4 = StringVar()
        self.pa1 = StringVar()
        self.pa2 = StringVar()
        self.pa3 = StringVar()
        self.pa4 = StringVar()
        self.fc1 = StringVar()
        self.fc2 = StringVar()
        self.fc3 = StringVar()
        self.fc4 = StringVar()
        self.fr1 = StringVar()
        self.fr2 = StringVar()
        self.fr3 = StringVar()
        self.fr4 = StringVar()
        self.spo21 = StringVar()
        self.spo22 = StringVar()
        self.spo23 = StringVar()
        self.spo24 = StringVar()
        self.temp1 = StringVar()
        self.temp2 = StringVar()
        self.temp3 = StringVar()
        self.temp4 = StringVar()
        self.firma1 = StringVar()
        self.firma2 = StringVar()
        self.firma3 = StringVar()
        self.firma4 = StringVar()
        self.admision = StringVar()
        self.origin = StringVar()
        self.procedimiento = StringVar()
        self.llegada = StringVar()
        self.puncion = StringVar()
        self.pac = StringVar()
        self.r = StringVar()
        self.i = 50
        
        


        self.root.title("CENTRO DE INFUSÃO DE UBERLÂNDIA")
        self.root.geometry("1366x768")  # set starting size of window
        self.root.maxsize(1366, 768)  # width x height
        self.root.config(bg="lightgrey")



        # titulo de la pantalla
        enter_info = Label(self.root, text="Revision Visita", bg="lightgrey")
        enter_info.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

        # campo nombre
        Label(self.root, text="Nombre:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        self.nombrem = Entry(self.root, textvariable = self.nombre, bd=3)
        self.nombrem.grid(row=2, column=1,padx=5, pady=5)
        self.nombrem.config(width=self.i)
        self.nombrem.insert(0,value['name'])

        # campo edad
        Label(self.root, text="Edad:", bg="lightgrey").grid(row=2, column=2, padx=5, pady=5)
        self.edadm = Entry(self.root, textvariable = self.edad, bd=3)
        self.edadm.grid(row=2, column=3, padx=5, pady=5)
        self.edadm.config(width=6)
        self.edadm.insert(0,value['age'])

        # campo peso
        Label(self.root, text="Peso:", bg="lightgrey").grid(row=2, column=4, padx=5, pady=5)
        self.pesom = Entry(self.root, textvariable = self.peso, bd=3)
        self.pesom.grid(row=2, column=5, padx=5, pady=5)
        self.pesom.config(width=3)
        self.pesom.insert(0,value['weight'])

        # campo fecha
        Label(self.root, text="Fecha:", bg="lightgrey").grid(row=2, column=6, padx=5, pady=5)
        self.fecham = Entry(self.root, textvariable = self.fecha, bd=3)
        self.fecham.grid(row=2, column=7, padx=5, pady=5)
        self.fecham.config(width=11)
        self.fecham.insert(0,value['date'])


        # campo médico
        Label(self.root, text="Médico:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        self.medicom = Entry(self.root, textvariable = self.medico, bd=3)
        self.medicom.grid(row=3, column=1, padx=5, pady=5)
        self.medicom.config(width=self.i)
        self.medicom.insert(0,value['doctor'])

        # campo seguro
        Label(self.root, text="Seguro:", bg="lightgrey").grid(row=3, column=2, padx=5, pady=5)
        self.segurom = Entry(self.root, textvariable = self.seguro, bd=3)
        self.segurom.grid(row=3, column=3, padx=5, pady=5, sticky=W)
        self.segurom.config(width=6)
        self.segurom.insert(0,value['insurance'])

        # campo poltrona
        Label(self.root, text="Poltrona:", bg="lightgrey").grid(row=3, column=4, padx=5, pady=5)
        self.poltronam = Entry(self.root, textvariable = self.poltrona, bd=3)
        self.poltronam.grid(row=3, column=5, padx=5, pady=5)
        self.poltronam.config(width=3)
        self.poltronam.insert(0,value['seat'])

        # campo fecha nacimento
        Label(self.root, text="F/N:", bg="lightgrey").grid(row=3, column=6, padx=5, pady=5)
        self.fechaNasm = Entry(self.root, textvariable = self.fechaNas, bd=3)
        self.fechaNasm.grid(row=3, column=7, padx=5, pady=5)
        self.fechaNasm.config(width=11)
        self.fechaNasm.insert(0,value['birthday'])

        # campo medicación
        Label(self.root, text="Medicación:", bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        self.medicacionm = Entry(self.root, textvariable = self.medicacion, bd=3)
        self.medicacionm.grid(row=5, column=1, padx=5, pady=5)
        self.medicacionm.config(width=self.i)
        self.medicacionm.insert(0,value['medicine'])

        # campo dosis
        Label(self.root, text="Dosis:", bg="lightgrey").grid(row=5, column=2, padx=5, pady=5)
        self.dosism = Entry(self.root, textvariable = self.dosis, bd=3)
        self.dosism.grid(row=5, column=3, padx=5, pady=5)
        self.dosism.config(width=6)
        self.dosism.insert(0,value['doses'])

        # campo equipo
        Label(self.root, text="Equipo:", bg="lightgrey").grid(row=6, column=0, padx=5, pady=5)
        self.equipom = Entry(self.root, textvariable = self.equipo, bd=3)
        self.equipom.grid(row=6, column=1, padx=5, pady=5)
        self.equipom.config(width=self.i)
        self.equipom.insert(0,value['team'])

        # campo admision
        Label(self.root, text="Admisión:", bg="lightgrey").grid(row=7, column=0, padx=5, pady=5)
        self.admisionm = Entry(self.root, textvariable = self.admision, bd=3)
        self.admisionm.grid(row=7, column=1, padx=5, pady=5, sticky=W)
        self.admisionm.config(width=5)
        self.admisionm.insert(0,value['admission'])

        # campo origin
        Label(self.root, text="Origin:", bg="lightgrey").grid(row=8, column=0, padx=5, pady=5)
        self.originm = Entry(self.root, textvariable = self.origin, bd=3)
        self.originm.grid(row=8, column=1, padx=5, pady=5)
        self.originm.config(width=self.i)
        self.originm.insert(0,value['origin'])

        # campo procedimento
        Label(self.root, text="Procedimiento:", bg="lightgrey").grid(row=9, column=0, padx=5, pady=5)
        self.procedimientom = Entry(self.root, textvariable = self.procedimiento, bd=3)
        self.procedimientom.grid(row=9, column=1, padx=5, pady=5)
        self.procedimientom.config(width=self.i)
        self.procedimientom.insert(0,value['procedure'])

        # campo estado llegada
        Label(self.root, text="Llegada:", bg="lightgrey").grid(row=10, column=0, padx=5, pady=5)
        self.llegadam = Entry(self.root, textvariable = self.llegada, bd=3)
        self.llegadam.grid(row=10, column=1, padx=5, pady=5)
        self.llegadam.config(width=self.i)
        self.llegadam.insert(0,value['arrive'])

        # campo puncion
        Label(self.root, text="Punción:", bg="lightgrey").grid(row=11, column=0, padx=5, pady=5)
        self.puncionm = Entry(self.root, textvariable = self.puncion, bd=3)
        self.puncionm.grid(row=11, column=1, padx=5, pady=5)
        self.puncionm.config(width=self.i)
        self.puncionm.insert(0,value['puncture'])


        # titulo de SEÑALES VITALES
        enter_info = Label(self.root, text="SEÑALES VITALES", bg="lightgrey")
        enter_info.grid(row=7, column=5, columnspan=5, padx=5, pady=5,sticky=W)

        # titulo de horário
        enter_info = Label(self.root, text="Horário", bg="lightgrey")
        enter_info.grid(row=8, column=3, padx=5, pady=5)

        # titulo de PA
        enter_info = Label(self.root, text="PA", bg="lightgrey")
        enter_info.grid(row=8, column=4, padx=5, pady=5)

        # titulo de FC
        enter_info = Label(self.root, text="FC", bg="lightgrey")
        enter_info.grid(row=8, column=5, padx=5, pady=5)

        # titulo de FR
        enter_info = Label(self.root, text="FR", bg="lightgrey")
        enter_info.grid(row=8, column=6, padx=5, pady=5)

        # titulo de Spo2
        enter_info = Label(self.root, text="SpO2", bg="lightgrey")
        enter_info.grid(row=8, column=7, padx=5, pady=5)

        # titulo de Tº
        enter_info = Label(self.root, text="Tº", bg="lightgrey")
        enter_info.grid(row=8, column=8, padx=5, pady=5, sticky=W)

        # titulo firma
        enter_info = Label(self.root, text="Firma", bg="lightgrey")
        enter_info.grid(row=8, column=9, padx=5, pady=5)

        # campo horario 1
        self.horario1m = Entry(self.root, textvariable = self.horario1, bd=3)
        self.horario1m.grid(row=9, column=3, padx=5, pady=5)
        self.horario1m.config(width=5)
        self.horario1m.insert(0,value['TIME1'])

        # campo pa 1
        self.pa1m = Entry(self.root, textvariable = self.pa1, bd=3)
        self.pa1m.grid(row=9, column=4, padx=5, pady=5)
        self.pa1m.config(width=5)
        self.pa1m.insert(0,value['PA1'])

        # campo fc 1
        self.fc1m = Entry(self.root, textvariable = self.fc1, bd=3)
        self.fc1m.grid(row=9, column=5, padx=5, pady=5)
        self.fc1m.config(width=3)
        self.fc1m.insert(0,value['FC1'])

        # campo fr 1
        self.fr1m = Entry(self.root, textvariable = self.fr1, bd=3)
        self.fr1m.grid(row=9, column=6, padx=5, pady=5)
        self.fr1m.config(width=3)
        self.fr1m.insert(0,value['FR1'])

        # campo spo2 1
        self.spo21m = Entry(self.root, textvariable = self.spo21, bd=3)
        self.spo21m.grid(row=9, column=7, padx=5, pady=5)
        self.spo21m.config(width=11)
        self.spo21m.insert(0,value['SPO21'])

        # campo Tº 1
        self.temp1m = Entry(self.root, textvariable = self.temp1, bd=3)
        self.temp1m.grid(row=9, column=8, padx=5, pady=5, sticky=W)
        self.temp1m.config(width=3)
        self.temp1m.insert(0,value['TEMP1'])

        # campo firma 1
        self.firma1m = Entry(self.root, textvariable = self.firma1, bd=3)
        self.firma1m.grid(row=9, column=9, padx=5, pady=5)
        self.firma1m.config(width=8)
        self.firma1m.insert(0,value['FIRMA1'])

        # campo horario 2
        self.horario2m = Entry(self.root, textvariable = self.horario2, bd=3)
        self.horario2m.grid(row=10, column=3, padx=5, pady=5)
        self.horario2m.config(width=5)
        self.horario2m.insert(0,value['TIME2'])

        # campo pa 2
        self.pa2m = Entry(self.root, textvariable = self.pa2, bd=3)
        self.pa2m.grid(row=10, column=4, padx=5, pady=5)
        self.pa2m.config(width=5)
        self.pa2m.insert(0,value['PA2'])

        # campo fc 2
        self.fc2m = Entry(self.root, textvariable = self.fc2, bd=3)
        self.fc2m.grid(row=10, column=5, padx=5, pady=5)
        self.fc2m.config(width=3)
        self.fc2m.insert(0,value['FC2'])

        # campo fr 2
        self.fr2m = Entry(self.root, textvariable = self.fr2, bd=3)
        self.fr2m.grid(row=10, column=6, padx=5, pady=5)
        self.fr2m.config(width=3)
        self.fr2m.insert(0,value['FR2'])

        # campo spo2 2
        self.spo22m = Entry(self.root, textvariable = self.spo22, bd=3)
        self.spo22m.grid(row=10, column=7, padx=5, pady=5)
        self.spo22m.config(width=11)
        self.spo22m.insert(0,value['SPO22'])

        # campo Tº 2
        self.temp2m = Entry(self.root, textvariable = self.temp2, bd=3)
        self.temp2m.grid(row=10, column=8, padx=5, pady=5, sticky=W)
        self.temp2m.config(width=3)
        self.temp2m.insert(0,value['TEMP2'])

        # campo firma 2
        self.firma2m = Entry(self.root, textvariable = self.firma2, bd=3)
        self.firma2m.grid(row=10, column=9, padx=5, pady=5)
        self.firma2m.config(width=8)
        self.firma2m.insert(0,value['FIRMA2'])

        # campo horario 3
        self.horario3m = Entry(self.root, textvariable = self.horario3, bd=3)
        self.horario3m.grid(row=11, column=3, padx=5, pady=5)
        self.horario3m.config(width=5)
        self.horario3m.insert(0,value['TIME3'])

        # campo pa 3
        self.pa3m = Entry(self.root, textvariable = self.pa3, bd=3)
        self.pa3m.grid(row=11, column=4, padx=5, pady=5)
        self.pa3m.config(width=5)
        self.pa3m.insert(0,value['PA3'])

        # campo fc 3
        self.fc3m = Entry(self.root, textvariable = self.fc3, bd=3)
        self.fc3m.grid(row=11, column=5, padx=5, pady=5)
        self.fc3m.config(width=3)
        self.fc3m.insert(0,value['FC3'])

        # campo fr 3
        self.fr3m = Entry(self.root, textvariable = self.fr3, bd=3)
        self.fr3m.grid(row=11, column=6, padx=5, pady=5)
        self.fr3m.config(width=3)
        self.fr3m.insert(0,value['FR3'])

        # campo spo2 3
        self.spo23m = Entry(self.root, textvariable = self.spo23, bd=3)
        self.spo23m.grid(row=11, column=7, padx=5, pady=5)
        self.spo23m.config(width=11)
        self.spo23m.insert(0,value['SPO23'])

        # campo Tº 3
        self.temp3m = Entry(self.root, textvariable = self.temp3, bd=3)
        self.temp3m.grid(row=11, column=8, padx=5, pady=5, sticky=W)
        self.temp3m.config(width=3)
        self.temp3m.insert(0,value['TEMP3'])

        # campo firma 3
        self.firma3m = Entry(self.root, textvariable = self.firma3, bd=3)
        self.firma3m.grid(row=11, column=9, padx=5, pady=5)
        self.firma3m.config(width=8)
        self.firma3m.insert(0,value['FIRMA3'])


        # campo horario 4
        self.horario4m = Entry(self.root, textvariable = self.horario4, bd=3)
        self.horario4m.grid(row=12, column=3, padx=5, pady=5)
        self.horario4m.config(width=5)
        self.horario4m.insert(0,value['TIME4'])

        # campo pa 4
        self.pa4m = Entry(self.root, textvariable = self.pa4, bd=3)
        self.pa4m.grid(row=12, column=4, padx=5, pady=5)
        self.pa4m.config(width=5)
        self.pa4m.insert(0,value['PA4'])

        # campo fc 4
        self.fc4m = Entry(self.root, textvariable = self.fc4, bd=3)
        self.fc4m.grid(row=12, column=5, padx=5, pady=5)
        self.fc4m.config(width=3)
        self.fc4m.insert(0,value['FC4'])

        # campo fr 4
        self.fr4m = Entry(self.root, textvariable = self.fr4, bd=3)
        self.fr4m.grid(row=12, column=6, padx=5, pady=5)
        self.fr4m.config(width=3)
        self.fr4m.insert(0,value['FR4'])

        # campo spo2 4
        self.spo24m = Entry(self.root, textvariable = self.spo24, bd=3)
        self.spo24m.grid(row=12, column=7, padx=5, pady=5)
        self.spo24m.config(width=11)
        self.spo24m.insert(0,value['SPO24'])

        # campo Tº 4
        self.temp4m = Entry(self.root, textvariable = self.temp4, bd=3)
        self.temp4m.grid(row=12, column=8, padx=5, pady=5, sticky=W)
        self.temp4m.config(width=3)
        self.temp4m.insert(0,value['TEMP4'])

        # campo firma 4
        self.firma4m = Entry(self.root, textvariable = self.firma4, bd=3)
        self.firma4m.grid(row=12, column=9, padx=5, pady=5)
        self.firma4m.config(width=8)
        self.firma4m.insert(0,value['FIRMA4'])



        # titulo de ANOTACIÓN / EVOLUCIÓN DE ENFERMAGEM
        enter_info = Label(self.root, text="ANOTACIÓN / EVOLUCIÓN DE ENFERMAGEM", bg="lightgrey")
        enter_info.grid(row=12, column=0, columnspan=3, padx=5, pady=5)

        # campo ANOTACIÓN / EVOLUCIÓN DE ENFERMAGEM
        self.texto = Text(self.root)
        self.texto.grid(row=13, column=0, columnspan=3, padx=5, pady=5)
        self.texto.config(width=self.i, height= 5) # carácteres
        self.texto.config(font=('Arial', 12),padx=5, pady=5,selectbackground='red')
        #self.texto.insert(0,'value[FIRMA4]')


        # botones
        #Button(self.root, text='Hello', command = self.hola).grid(row=14, column=1, padx=1, pady=1)
        Button(self.root, text='Salvar', command = self.nuevo).grid(row=14, column=1, padx=1, pady=1)

        # bucle de la aplicación
        self.root.mainloop()

if __name__ == '__main__':
    menu = Revision()
    menu.guirevision()