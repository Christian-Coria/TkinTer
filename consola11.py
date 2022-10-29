import tkinter as tk
from tkinter import ttk, messagebox, Menu

# Manejo de Menus

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('soporte.ico')


entrada1 = ttk.Entry(ventana, width=30) 

entrada1.grid(row=0, column=0)

etiqueta1 = tk.Label(ventana, text='Aqui se inserta el texto de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    etiqueta1.config(text=entrada1.get()) 
    mensaje1= entrada1.get()
    if mensaje1:
        messagebox.showinfo('mostramos informacion', mensaje1 + ' informativo')


def crear_menu():
    #conf menu principal
    menu_principal = Menu(ventana)
    #tearoff = False   asi se evita que se separe el menu de la interface
    submenu_archivo = Menu(menu_principal, tearoff=0)
    submenu_archivo.add_command(label='Nuevo')
    #agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')

    #mostramos el menu
    ventana.config(menu=menu_principal)

        
boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()


ventana.mainloop()