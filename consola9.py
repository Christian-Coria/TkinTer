import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('soporte.ico')

entrada_var1 = tk.StringVar(value='Valor por Default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1) 

entrada1.grid(row=0, column=0)

#etiqueta o label
etiqueta1 = tk.Label(ventana, text='Aqui se inserta el texto de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    etiqueta1.config(text=entrada_var1.get())  #reflejamos los cambios de la caja de texto en la etiqueta
    

boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()