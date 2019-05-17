from tkinter import *
master = Tk() #declarar una ventana 
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)" #asiganar el texto a una variable
msg = Message(master, text = whatever_you_do) #crear una ventana de mensaje
msg.config(bg='lightgreen', font=('times', 24, 'italic')) #propiedades de la ventana de mensaje (color de ventana, tipo y fuente de letra)
msg.pack( )
mainloop( )