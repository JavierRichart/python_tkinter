import tkinter as tk
from tkinter import ttk

# Ventana pricipal

ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400, height=550)
ventana.configure(bg="lightblue")


# Rótulo del titulo
rotulo_titulo = tk.Label(ventana,
                         text="CONVERSOR TEMPERATURAS",
                         bg="lightblue", fg="black",
                         font="consolas 20 bold",
                         relief= tk.GROOVE, bd=2,
                         padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

ventana.mainloop()
