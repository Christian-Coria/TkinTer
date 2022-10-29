import tkinter as tk
from tkinter import ttk

'''Pading es espacio entre elementos
    ipadx : espacio a la izquierda y derecha del boton 
    ipady : espacio inferior o superior
    para informacion externa al componente :
            pady espacio en parte superior inferior
            padx espacio derecha e izquierda '''

''' extender el renglon o celda para que ocupe varias columnas una celda
        columnspan=2   el dos indica la ocupacion de dos columnas
        rowspan=2    el dos indica que ocupamos dos renglones'''

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('soporte.ico')

def evento1():
    boton1.config(text='Boton1 Presionado')

def evento2():
    boton2.config(text='Boton2 Presionado')

def evento3():
    boton4.config(text='Boton 4 Presionado', fg='green' , bg='yellow', relief=tk.GROOVE) 

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text='boton1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', 
                    padx=40, pady=30,ipadx=20, ipady=30, columnspan=2 , rowspan=2)  
 #agregamos espacio de manera externa, interna al elemento  y ocupamos mas columnas y renglones          


                      #Ocultamos el boton 2, 3 , 4 para visualizar la expancion de boton 1
boton2 = ttk.Button(ventana, text='boton2', command=evento2)
#boton2.grid(row=1, column=0, sticky='NSWE', ipadx=20, ipady=30)       
boton3=ttk.Button(ventana, text='boton3')
#boton3.grid(row=0, column=1, sticky='NSWE')      
boton4= tk.Button(ventana, text='boton4', command=evento3)    
#boton4.grid(row=1 , column=1, sticky='NSWE')


ventana.mainloop()