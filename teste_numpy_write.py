import numpy as np
import time

#creamos un array aleatorio de números enteros de dos dimensiones
archivo = np.load('pac.npz')
arr = archivo['pacientes']
print(arr)

nombre = input('Entra su nombre: ')
edad = int(input('Entra su edad: '))
timestamp = f'{time.strftime("%Y")}{time.strftime("%m")}{time.strftime("%d")}_{time.strftime("%H")}{time.strftime("%M")}{time.strftime("%S")}'



arr_1 = np.array([nombre,edad,timestamp])
print(arr_1)
arr_f = np.append(arr, arr_1)
print(arr_f)


np.savez('pac.npz', pacientes=arr_f)


