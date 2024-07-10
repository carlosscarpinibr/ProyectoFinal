from tkinter import *

root = Tk()
root.title("Nuevo paciente")
root.geometry("800x600")  # set starting size of window
root.maxsize(800, 600)  # width x height
root.config(bg="lightgrey")

# Profile picture
image = PhotoImage(file="imagen.gif")
small_img = image.subsample(4,4)

img = Label(root, image=small_img)
img.grid(row=0, column=0, rowspan=6, padx=5, pady=5)

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="Introduzca los datos del paciente: ", bg="lightgrey")
enter_info.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

# Name label and entry widgets
Label(root, text="Nombre", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5, sticky=E)

nombre = Entry(root, bd=3)
nombre.grid(row=1, column=2, padx=5, pady=5)

# Gender label and dropdown widgets
""" gender = Menubutton(root, text="Gender")
gender.grid(row=2, column=2, padx=5, pady=5, sticky=W)
gender.menu = Menu(gender, tearoff=0)
gender["menu"] = gender.menu

# choices in gender dropdown menu
gender.menu.add_cascade(label="Male")
gender.menu.add_cascade(label="Female")
gender.menu.add_cascade(label="Other")
gender.grid() """

# Eyecolor label and entry widgets
Label(root, text="Apellido", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5, sticky=E)
apellido = Entry(root, bd=3)
apellido.grid(row=3, column=2, padx=5, pady=5)

# Height and Weight labels and entry widgets
Label(root, text="Edad", bg="lightgrey").grid(row=4, column=1, padx=5, pady=5, sticky=E)
#Label(root, text="inches", bg="lightgrey").grid(row=4, column=3, sticky=W)

edad = Entry(root, bd=3)
edad.grid(row=4, column=2, padx=5, pady=5)

Label(root, text="E-mail", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5, sticky=E)
#Label(root, text="lbs", bg="lightgrey").grid(row=5, column=3, sticky=W)

email = Entry(root, bd=3)
email.grid(row=5, column=2, padx=5, pady=5)



def nuevo():
    
    nuevoPaciente = {
            'name' : nombre,
            'surename' : apellido,
            'age' : edad,
            'mail' : email
        }
    print(nuevoPaciente)
    return nuevoPaciente

Button(root, text='Salvar', command = nuevo).grid(row=6, column=1, padx=5, pady=5, sticky=E)
Button(root, text='Mostrar', command = print(nuevo)).grid(row=7, column=1, padx=5, pady=5, sticky=E)

Label(root, text='\nResultado').grid(row=8, column=1, padx=5, pady=5, sticky=E)
Entry(root, justify='center', textvariable = print(type(nuevo)), state='disable').grid(row=9, column=1, padx=5, pady=5, sticky=E) # resultado

root.mainloop()