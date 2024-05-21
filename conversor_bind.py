import tkinter as tk
from tkinter import ttk

# Ventana principal

ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("400x550+700+100")
ventana.minsize(width=400, height=550)
ventana.configure(bg="lightblue")


# Funciones

def convertir():
    try:
        entrada = temp_entrada.get()
        salida = temp_salida.get()
        grados = entrada_grados.get()
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
            if opcion_conversion.get() == 1:
                resultado = f"{resultado}\u00B0F"
            else:
                resultado = f"{resultado}\u00B0C"

        rotulo_resultado.config(text=resultado)
        entrada_grados.config(state="disabled")
        boton_convertir.config(state="disabled")

    except ValueError:
        if grados == "":
            pass
        else:
            rotulo_resultado.config(text="Error")


def borrar():
    entrada_grados.config(state="normal")
    boton_convertir.config(state="normal")
    entrada_grados.delete(0, tk.END),
    rotulo_resultado.config(text="")


def mostrar_entrada(event):
    opcion_entrada = temp_entrada.get()
    opcion_salida = temp_salida.get()

    if opcion_entrada == "Celsius":
        rotulo_primero.config(text="Celsius    : ")
        if opcion_salida == "Celsius":
            rotulo_segundo.config(text="Fahrenheit : ")
            desplegable_salida.set("Fahrenheit")
    elif opcion_entrada == "Fahrenheit":
        rotulo_primero.config(text="Fahrenheit : ")
        if opcion_salida == "Fahrenheit":
            rotulo_segundo.config(text="Celsius    : ")
            desplegable_salida.set("Celsius")
    elif opcion_entrada == "Kelvin":
        rotulo_primero.config(text="Kelvin     : ")
        if opcion_salida == "Kelvin":
            rotulo_segundo.config(text="Celsius    :")
            desplegable_salida.set("Celsius")

    entrada_grados.focus()


def mostrar_salida(event):
    opcion_entrada = temp_entrada.get()
    opcion_salida = temp_salida.get()

    if opcion_salida == "Celsius":
        rotulo_segundo.config(text="Celsius    : ")
        if opcion_entrada == "Celsius":
            rotulo_primero.config(text="Fahrenheit :")
            desplegable_entrada.set("Fahrenheit")
    elif opcion_salida == "Fahrenheit":
        rotulo_segundo.config(text="Fahrenheit : ")
        if opcion_entrada == "Fahrenheit":
            rotulo_primero.config(text="Celsius    :")
            desplegable_entrada.set("Celsius")
    elif opcion_salida == "Kelvin":
        rotulo_segundo.config(text="Kelvin     : ")
        if opcion_entrada == "Kelvin":
            rotulo_primero.config(text="Fahrenheit :")
            desplegable_entrada.set("Fahrenheit")

    entrada_grados.focus()


rotulo_titulo = tk.Label(ventana,
                         text="CONVERSOR TEMPERATURAS",
                         bg="lightblue", fg="black",
                         font="consolas 20 bold",
                         relief=tk.GROOVE, bd=2,
                         padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

rotulo_entrada = tk.Label(ventana,
                          text="Temperatura entrada:",
                          bg="lightblue", fg="black",
                          font="consolas 14 bold",
                          bd=2)
rotulo_entrada.pack()

temp_entrada = tk.StringVar()
desplegable_entrada = ttk.Combobox(ventana,
                                   font="consolas 14 bold",
                                   # width=14,
                                   values=["Celsius", "Fahrenheit", "Kelvin"],
                                   state="readonly",
                                   textvariable=temp_entrada)
desplegable_entrada.pack()
desplegable_entrada.set("Celsius")

rotulo_salida = tk.Label(ventana,
                         text="Temperatura salida:",
                         bg="lightblue", fg="black",
                         font="consolas 14 bold",
                         bd=2)
rotulo_salida.pack()

temp_salida = tk.StringVar()
desplegable_salida = ttk.Combobox(ventana,
                                  font="consolas 14 bold",
                                  values=["Celsius", "Fahrenheit", "Kelvin"],
                                  state="readonly",
                                  textvariable=temp_salida)
desplegable_salida.pack()
desplegable_salida.set("Fahrenheit")

desplegable_entrada.bind("<<ComboboxSelected>>", mostrar_entrada)
desplegable_salida.bind("<<ComboboxSelected>>", mostrar_salida)

cuadro_espacio = tk.Frame(ventana,
                          height=20,
                          bg="lightblue")
cuadro_espacio.pack()

cuadro1 = tk.Frame(ventana,
                   bg="lightblue")

rotulo_primero = tk.Label(cuadro1,
                          text="Celsius:",
                          bg="lightblue",
                          font="consolas 18 bold",
                          width=12,
                          anchor=tk.W)
rotulo_primero.pack(side=tk.LEFT, padx=10)

entrada_grados = tk.Entry(cuadro1,
                          bg="white", fg="black",
                          font="consolas 18 bold",
                          relief=tk.SUNKEN,
                          width=10,
                          justify=tk.RIGHT,
                          state="normal")
entrada_grados.pack(side=tk.LEFT, padx=10)

cuadro1.pack(pady=10)

cuadro2 = tk.Frame(ventana,
                   bg="lightblue")

rotulo_segundo = tk.Label(cuadro2,
                          text="Fahrenheit:",
                          bg="lightblue",
                          font="consolas 18 bold",
                          width=12,
                          anchor=tk.W)
rotulo_segundo.pack(side=tk.LEFT, padx=10)

rotulo_resultado = tk.Label(cuadro2,
                            text="",
                            bg="lightgreen",
                            font="consolas 18 bold",
                            width=10,
                            relief=tk.GROOVE,
                            anchor=tk.E)
rotulo_resultado.pack(side=tk.LEFT, padx=10)

cuadro2.pack(pady=10)

cuadro3 = tk.Frame(ventana,
                   bg="lightblue")

redondeo = tk.BooleanVar()
casilla_redondeo = tk.Checkbutton(cuadro3,
                                  text="Hacer redondeo",
                                  bg="lightblue",
                                  font="consolas 14 bold",
                                  width=15, anchor=tk.W,
                                  variable=redondeo)
casilla_redondeo.pack()

simbolo = tk.BooleanVar()
casilla_simbolo = tk.Checkbutton(cuadro3,
                                 text="Poner símbolo",
                                 bg="lightblue",
                                 font="consolas 14 bold",
                                 width=15, anchor=tk.W,
                                 variable=simbolo)
casilla_simbolo.pack()

cuadro3.pack(pady=10)

cuadro4 = tk.Frame(ventana,
                   bg="lightblue")

boton_borrar = tk.Button(cuadro4,
                         text="Borrar",
                         bg="grey",
                         font="consolas 18 bold",
                         width=10,
                         command=borrar)
boton_borrar.pack(side=tk.LEFT, padx=10)

boton_convertir = tk.Button(cuadro4,
                            text="Convertir",
                            bg="orange",
                            font="consolas 18 bold",
                            width=10,
                            state="normal",
                            command=convertir)
boton_convertir.pack(side=tk.LEFT, padx=10)

cuadro4.pack(pady=20)

entrada_grados.focus()

ventana.mainloop()
