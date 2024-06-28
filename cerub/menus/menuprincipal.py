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
            print(prompt)
            opcion = input('Introduzca la opción deseada:')
            if opcion == '1':
                print('Registar paciente')
            elif opcion == '2':
                print('Registrar visita')
            elif opcion == '3':
                print('Listar pacientes')
            elif opcion == '4':
                print('Listar visitas')
            elif opcion == '5':
                print('Fin del programa.')
            else:
                print('Opción inválida!')

if __name__ == '__main__':
            test = Menu()
            test.mainmenu()
            
