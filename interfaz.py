# Vamos a importar tkinter
import  tkinter as tk
from tkinter import messagebox

mywindow =tk.Tk()
mywindow.title("mi primera ventana en python")
mywindow.geometry("200x200")

def myMessage():
  messagebox.askquestion("Pregunta", "¿Ya cenaron?...")
	
btn1 = tk.Button(mywindow, text = "Botón", command = myMessage)
btn1.pack()
btn1.place(x=80, y=100)
mywindow.mainloop()
