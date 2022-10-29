import tkinter as tk
from tkinter import ttk

# entrada de datos

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('soporte.ico')


entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER) #aqui definimos la cantidad de caracteres .RIGTH (derecha y asi...)
entrada1.grid(row=0, column=0)
#insert agrega un texto de ayuda
entrada1.insert(0, 'introduce texto')
entrada1.insert(5, '**')
entrada1.insert(tk.END, '.')


ventana.mainloop()