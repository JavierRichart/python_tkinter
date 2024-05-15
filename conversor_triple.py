import tkinter as tk
from tkinter import ttk

# Ventana pricipal

ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400, height=550)
ventana.configure(bg="lightblue")


# Funciónes

def convertir():
    try:
        entrada = temp_entrada.get()
        salida = temp_salida.get()
        grados = float(entrada_grados.get())
        if entrada == salida:
            resultado = grados
        elif entrada == "Celsius" and salida == "Fahrenheit":
            resultado = round(grados * 1.8 + 32, 2)
        elif entrada == "Fahrenheit" and salida == "Celsius":
            resultado = round((grados - 32) / 1.8, 2)
        elif entrada == "Celsius" and salida == "Kelvin":
            resultado = round(grados + 273.15, 2)
        elif entrada == "Kelvin" and salida == "Celsius":
            resultado = round(grados - 273.15, 2)
        elif entrada == "Fahrenheit" and salida == "Kelvin":
            resultado = round(((grados - 32) / 1.8) + 273.15, 2)
        elif entrada == "Kelvin" and salida == "Fahrenheit":
            resultado = round(((grados - 273.15) * 1.8) + 32, 2)

        if redondeo.get():
            resultado = round(resultado)

        if simbolo.get():
            if salida == "Celsius":
                resultado = f"{resultado}\u00B0C"
            elif salida == "Farenheit":
                resultado = f"{resultado}\u00B0C"
            else:
                resultado = f"{resultado} K"

            rotulo_resultado.config(text=resultado)
            entrada_grados.config(state="disabled")
            boton_convertir.config(state="disabled")

    except ValueError:
        if entrada_grados.get() == "":
            pass
        else:
            rotulo_resultado.config(text="Error")


def borrar():
    entrada_grados.config(state="normal")
    boton_convertir.config(state="normal")
    entrada_grados.delete(0, tk.END)
    rotulo_resultado.config(text="")


# Rótulo del titulo
rotulo_titulo = tk.Label(ventana,
                         text="CONVERSOR TEMPERATURAS",
                         bg="lightblue", fg="black",
                         font="consolas 20 bold",
                         relief=tk.GROOVE, bd=2,
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

cuadro1 = tk.Frame(ventana,
                   bg="lightblue")
rotulo_primero = tk.Label(cuadro1,
                          text="Celsius:   ",
                          bg="lightblue",
                          font="consolas 18 bold")
rotulo_primero.pack(side=tk.LEFT, padx=20, pady=20)

entrada_grados = tk.Entry(cuadro1,
                          bg="white",
                          fg="black",
                          font="consolas 18 bold",
                          relief=tk.SUNKEN,
                          bd=3,
                          width=10,
                          justify=tk.RIGHT,
                          state="normal")
entrada_grados.pack(side=tk.LEFT, padx=10, pady=10)

cuadro1.pack()

# segundo frame

cuadro2 = tk.Frame(ventana,
                   bg="lightblue")
rotulo_segundo = tk.Label(cuadro2,
                          text="Salida: ",
                          bg="lightblue",
                          font="consolas 18 bold")
rotulo_segundo.pack(side=tk.LEFT, padx=20, pady=20)

rotulo_resultado = tk.Label(cuadro2,
                            text="",
                            bg="lightgreen",
                            font="consolas 18 bold",
                            width=10,
                            relief=tk.GROOVE,
                            anchor=tk.E)
rotulo_resultado.pack(side=tk.LEFT, padx=20, pady=20)

cuadro2.pack(pady=10)

# cuadro widgets

cuadro_widgets = tk.Frame(ventana,
                          bg="lightblue")

redondeo = tk.BooleanVar()
casilla_redondeo = tk.Checkbutton(cuadro_widgets,
                                  text="Redondear",
                                  bg="lightblue",
                                  font="consolas 14 bold",
                                  width=15, anchor=tk.W,
                                  variable=redondeo)
casilla_redondeo.pack()

simbolo = tk.BooleanVar()
casilla_simbolo = tk.Checkbutton(cuadro_widgets,
                                 text="Mostrar símbolo",
                                 bg="lightblue",
                                 font="consolas 14 bold",
                                 width=15, anchor=tk.W,
                                 variable=simbolo)
casilla_simbolo.pack()

cuadro_widgets.pack()

# tercer frame

cuadro3 = tk.Frame(ventana,
                   bg="lightblue")

boton_borrar = tk.Button(cuadro3,
                         text="Borrar",
                         bg="grey",
                         font="consolas 18 bold",
                         width=10,
                         command=borrar)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=20)

boton_convertir = tk.Button(cuadro3,
                            text="Convertir",
                            bg="orange",
                            font="consolas 18 bold",
                            width=10,
                            command=convertir,
                            state="normal")
boton_convertir.pack(side=tk.LEFT, padx=20, pady=20)

cuadro3.pack()

ventana.mainloop()
