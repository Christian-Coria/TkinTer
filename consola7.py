import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('soporte.ico')


entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL) 

entrada1.grid(row=0, column=0)

entrada1.insert(0, 'introduce texto')
entrada1.insert(5, '**')
entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly') 

def enviar():
    print(entrada1.get())  #recuperamos el texto insertado por medio del metodo get
    boton1.config(text=entrada1.get()) #asi cambiamos el texto del boton que imprime lo introducido en la caja de texto
    #para eliminar el contenido de la caja de texto
    #entrada1.delete(0, tk.END)
    entrada1.select_range(0, tk.END)
    entrada1.focus() #mandamos a llamar el metodo focus para que se seleccione el texto
    

boton1 = ttk.Button(ventana, text='enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()