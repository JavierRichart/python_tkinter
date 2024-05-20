import tkinter as tk
from tkinter import ttk

# Ventana principal

ventana = tk.Tk()
ventana.geometry("500x400+600+100")
ventana.config(bg="lightblue")


# Funciones

def elegir(event):
    rotulo.config(text=f"Has elegido {fruta.get()}")


# Widgets

fruta = tk.StringVar()
desplegable = ttk.Combobox(ventana,
                           font="consolas 18 bold",
                           values=["Manzana", "Pera", "Melón", "Naranja", "Melocotón"],
                           state="readonly",
                           textvariable=fruta)
desplegable.pack(pady=50)

desplegable.bind("<<ComboboxSelected>>", elegir)

rotulo = tk.Label(ventana,
                  text="Elige una fruta",
                  font="consolas 20")
rotulo.pack(pady=20)

ventana.mainloop()
