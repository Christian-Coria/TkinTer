import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

#modificamos el tamaño de la ventana 

ventana.geometry('1200x600')

#cambiamos el nombre de la ventana
ventana.title('Nueva Consola')

#cambiar icono
ventana.iconbitmap('soporte.ico')


def evento_click():
    boton1.config(text='Boton Presionado')
    print('ejecucion del evento click') #este mensaje se imprime en consola
    boton2 = ttk.Button(ventana, text='Nuevo Boton')
    boton2.pack()

#agregamos boton widget , y especificamos objeto padre (ventana)
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click) #coman es para definir un evento
#para desplegar el boton:
boton1.pack()

#iniciamos la ventana siempre al final

ventana.mainloop()
