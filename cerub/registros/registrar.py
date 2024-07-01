class Register():
    def __init__(self):
        return None
    
    def registrapac(self):
        while True:
            nombre = input('Introduzca el nombre del paciente: ').title()
            if nombre == '':
                print('Este campo no puede estar vacio, intente nuevamente')
            else:
                break
        while True:
            apellido = input('Introduzca el apellido del paciente: ').title()
            if apellido == '':
                print('Este campo no puede estar vacio, intente nuevamente')
            else:
                break
        while True:
            try:
                edad = int(input('Introduzca la edad del paciente:'))
                break
            except ValueError:
                print('Introduzca una edad válida')
        while True:
            email = input('Introduzca el e-mail del paciente: ')
            if email == '':
                print('Este campo no puede estar vacio, intente nuevamente')
            else:
                break
        codPaciente = f'{apellido[0]}{apellido[1]}{nombre[0]}{nombre[1]}{edad}2024'.upper()
        nuevoPaciente = {codPaciente : {
            'name' : nombre,
            'surename' : apellido,
            'age' : edad,
            'mail' : email
        }}
        return nuevoPaciente