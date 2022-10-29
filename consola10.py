import tkinter as tk
from tkinter import ttk, messagebox

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
    #creamos mensajes o message box 
    mensaje1= entrada1.get()
    if mensaje1:
        messagebox.showinfo('mostramos informacion', mensaje1 + ' informativo')
        messagebox.showerror('Mensaje de error', mensaje1 + ' Error')
        messagebox.showwarning('Mensaje de cuidado', mensaje1 + ' Alerta')

boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()