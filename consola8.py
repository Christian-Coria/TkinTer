import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('soporte.ico')

#definimos una variable para modificar posteriorm
entrada_var1 = tk.StringVar(value='Valor por Default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1) #ingresamos el componente en textvariable

entrada1.grid(row=0, column=0)

# entrada1.insert(0, 'introduce texto')
# entrada1.insert(5, '**')
# entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly') 

def enviar():
    #recuperamos la info de la variable asociada.
    boton1.config(text=entrada_var1.get()) 
    # Para modificaciones se usa variable de texto y metodo set
    entrada_var1.set('cambio')
    

boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()