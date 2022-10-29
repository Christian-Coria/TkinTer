import tkinter as tk
from tkinter import ttk

# entrada de datos

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('soporte.ico')


#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*') # se mostraran * en vez de lo escrito
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL) # desabilitamos la caja de texto tk.DISABLED 

entrada1.grid(row=0, column=0)

entrada1.insert(0, 'introduce texto')
entrada1.insert(5, '**')
entrada1.insert(tk.END, '.')
entrada1.config(state='readonly') #se pone a esta altura para que se ejecute lo anterior

ventana.mainloop()