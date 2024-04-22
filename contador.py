import sys
import tkinter as tk

ventana = tk.Tk()
ventana.title("Contador")
ventana.minsize(width=200, height=300)


def cuenta_numeros():
    contador = numero["text"]

    contador += 1

    numero.config(text=contador)


titulo = tk.Label(ventana,
                  text="CONTADOR",
                  font=("arial", 24),
                  bg="lightgreen", fg="darkblue",
                  relief=tk.GROOVE,
                  padx=20, pady=20)
titulo.pack()

numero = tk.Label(ventana,
                  text=0,
                  font=("arial", 48),
                  bg="darkgreen", fg="lightblue",
                  padx=20, pady=20)
numero.pack()

contar = tk.Button(ventana,
                   text="CONTAR",
                   font=("arial", 18),
                   bg="lightgrey", fg="black",
                   padx=20, pady=20,
                   relief=tk.GROOVE,
                   bd=10,
                   command=cuenta_numeros)
contar.pack()

ventana.mainloop()
