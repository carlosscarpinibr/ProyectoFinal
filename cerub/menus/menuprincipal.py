from cerub.controles.controlar import Control
from cerub.registros.registrar import Register
from pathlib import Path
import json

class Menu():
    def __init__(self):
        return None
    
    def mainmenu(self):
        prompt = '''
                        Menu principal - CERUB 
            1. Registar paciente
            2. Registar visita
            3. Listar pacientes
            4. Listar visitas
            5. Salir
        '''

        opcion = 0

        while opcion != '5':
            metodoControle = Control()
            print(prompt)
            opcion = input('Introduzca la opción deseada:')
            if opcion == '1':
                print('Registar paciente')
                metodoRegistro = Register()
                nuevoPac = metodoRegistro.registrapac()
                database = metodoControle.leerdatabase()
                database.append(nuevoPac)
                metodoControle.escribir(database)
            elif opcion == '2':
                print('Registrar visita')
            elif opcion == '3':
                print('Listar pacientes')
                print(metodoControle.leerdatabase())
            elif opcion == '4':
                print('Listar visitas')
            elif opcion == '5':
                print('Fin del programa.')
            else:
                print('Opción inválida!')

if __name__ == '__main__':
            test = Menu()
            test.mainmenu()
            
