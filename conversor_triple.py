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

# Desplegables y rótulos

rotulo_entrada = tk.Label(ventana,
                          text="Temperatua entrada: ",
                          bg="lightblue", fg="black",
                          font="consolas 14 bold",
                          bd=2)
rotulo_entrada.pack()

temp_entrada = tk.StringVar()
desplegable_entrada = ttk.Combobox(ventana,
                                   font="consolas 14 bold",
                                   width=16,
                                   values=["Celsius", "Fahrenheit", "Kelvin"],
                                   state="readonly",
                                   textvariable=temp_entrada)
desplegable_entrada.pack(pady=5)
desplegable_entrada.set("Celsius")

rotulo_salida = tk.Label(ventana,
                         text="Temperatura salida",
                         bg="lightblue", fg="black",
                         font="consolas 14 bold",
                         bd=2)
rotulo_salida.pack()

temp_salida = tk.StringVar()
desplegable_salida = ttk.Combobox(ventana,
                                  font="consolas 14 bold",
                                  width=16,
                                  values=["Celsius", "Farenheit", "Kelvin"],
                                  state="readonly",
                                  textvariable=temp_salida)
desplegable_salida.pack(pady=5)
desplegable_salida.set("Farenheit")


ventana.mainloop()
