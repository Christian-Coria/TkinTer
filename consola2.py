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



boton1 = ttk.Button(ventana, text='boton1', command=evento1)
boton1.grid(row=0, column=0, sticky='E')                                                '''especificamos la posicion GridManager
                                                                           sticky para fijar o pegar el boton( NW - N - NE
                                                                                                               W  -    - E 
                                                                                                               SW - S - SE)
                                                                           NS seria de norte a sur --- EW de este a oeste toda la linea'''
boton2 = ttk.Button(ventana, text='boton2', command=evento2)
boton2.grid(row=3, column=0, sticky='W')

ventana.mainloop()