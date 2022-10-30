import tkinter as tk
import sys
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

def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

def crear_menu():
    #conf menu principal
    menu_principal = Menu(ventana)
    #tearoff = False   asi se evita que se separe el menu de la interface
    submenu_archivo = Menu(menu_principal, tearoff=0)
    submenu_archivo.add_command(label='Nuevo')
    #agregar separador
    submenu_archivo.add_separator()
    submenu_archivo.add_command(label='Salir', command=salir)
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    #submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    submenu_ayuda.add_command(label='Acerca De')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')

    #mostramos el menu
    #agregamos el submenu al menu principal
    

    ventana.config(menu=menu_principal)

        
boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()


ventana.mainloop()