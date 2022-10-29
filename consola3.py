import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('soporte.ico')

def evento1():
    boton1.config(text='Boton1 Presionado')

def evento2():
    boton2.config(text='Boton2 Presionado')

def evento3():
    boton4.config(text='Boton 4 Presionado', fg='green' , bg='yellow', relief=tk.GROOVE) '''relief es el contorno - 
                                                            fg o fr es el color de la fuente , Groove es contorno, bg color de fondo
                                                            para que no alla error debe ser creado el boton con el pauqte tk y no ttk'''
                                                            
#Configuramos el Grid    1 o 3 O el numero que se coloque es el espacio proporcional de cada boton 
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text='boton1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE')                                             
boton2 = ttk.Button(ventana, text='boton2', command=evento2)
boton2.grid(row=1, column=0, sticky='NSWE')
boton3=ttk.Button(ventana, text='boton3')
boton3.grid(row=0, column=1, sticky='NSWE')
boton4= tk.Button(ventana, text='boton4', command=evento3)    # para que no alla error debe ser creado el boton con el pauqte tk y no ttk
boton4.grid(row=1 , column=1, sticky='NSWE')


ventana.mainloop()
