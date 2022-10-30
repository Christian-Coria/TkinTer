import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')
ventana.iconbitmap('soporte.ico')
ventana.resizable(0,0) #fijamos a un unico tamaño no modificable

ventana.columnconfigure(0, weight=1) #fijamos espacio de columnas
ventana.columnconfigure(1, weight=3)

etiqueta1 = tk.Label(ventana, text='Usuario: ')
etiqueta1.grid(row=0, column=0, sticky=tk.E, padx=5 , pady=5)
entrada1 = ttk.Entry(ventana) 
entrada1.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

etiqueta2 = tk.Label(ventana, text='Contraseña')
etiqueta2.grid(row=1, column=0, sticky=tk.E, padx=5 , pady=5)
entrada2 = ttk.Entry(ventana, show='*') 
entrada2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

def login():
    
    messagebox.showinfo('Datos Login',
                        f' Usuario: {entrada1.get()}, Password: {entrada2.get()}')  
    

boton1 = ttk.Button(ventana, text='login', command=login)
boton1.grid(row=3, column=0, columnspan=2)

ventana.mainloop()