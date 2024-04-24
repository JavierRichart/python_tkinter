import tkinter as tk

ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400, height=500)
ventana.configure(bg="lightblue")


def convertir():
    try:
        grados = entrada_grados.get()
        if opcion_coversion.get() == 1:
            resultado = round((float(grados) * 1.8) + 32, 2)
        else:
            resultado = round((float(grados) - 32) / 1.8, 2)
        rotulo_resultado.config(text=resultado)
        entrada_grados.config(state="disabled")
        boton_convertir.config(state="disabled")
    except ValueError:
        if grados == "":
            pass
        else:
            rotulo_resultado.config(text="Error")
    finally:
        entrada_grados.config(state="disabled")
        boton_convertir.config(state="disabled")


def borrar():
    entrada_grados.config(state="normal")
    boton_convertir.config(state="normal")
    entrada_grados.delete(0, tk.END)
    rotulo_resultado.config(text="")


def cambiar():
    if opcion_coversion.get() == 1:
        rotulo_primero.config(text="Celsius:")
        rotulo_segundo.config(text="Fahrenheit:")
    else:
        rotulo_primero.config(text="Fahrenheit:")
        rotulo_segundo.config(text="Celsius:")


rotulo_titulo = tk.Label(ventana,
                         text="CONVERSOR TEMPERATURAS",
                         bg="lightblue", fg="black",
                         font="consolas 20 bold",
                         relief=tk.GROOVE, bd=2,
                         padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

# Botones de opciones

opcion_coversion = tk.IntVar()

opcion1 = tk.Radiobutton(ventana,
                         text="Celsius a Fahrenheit",
                         bg="lightblue",
                         font="consolas 18",
                         variable=opcion_coversion,
                         value=1,
                         command=cambiar)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana,
                         text="Fahrenheit a Celsius",
                         bg="lightblue",
                         font="consolas 18",
                         variable=opcion_coversion,
                         value=2,
                         command=cambiar)
opcion2.pack()

opcion_coversion.set(1)

# Cuadro espacio

cuadro_espacio = tk.Frame(ventana,
                          height=20,
                          bg="lightblue")
cuadro_espacio.pack()



# primer frame

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
                             text="Fahrenheit:",
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

cuadro2.pack()

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