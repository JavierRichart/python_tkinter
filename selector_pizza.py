import tkinter as tk

ventana = tk.Tk()
ventana.title("Selector")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400, height=600)
ventana.configure(bg="wheat")


# Funciones

def enviar():
    pizza_elegida = opcion_seleccionada.get()
    if pizza_elegida == 1:
        resultado = "Margarita"
    elif pizza_elegida == 2:
        resultado = "Hawai"
    elif pizza_elegida == 3:
        resultado = "Napolitana"
    elif pizza_elegida == 4:
        resultado = "Carbonara"
    elif pizza_elegida == 5:
        resultado = "Barbacora"
    else:
        resultado = "No hay selección"
    rotulo_resultado.config(text=f"Su pizza:\n{resultado}")
    boton_enviar['state'] = 'disabled'
    boton_reiniciar['state'] = 'normal'


def reiniciar():
    opcion_seleccionada.set(0)
    rotulo_resultado.config(text=f"Elija su pizza y pulse enviar")
    boton_enviar['state'] = 'disabled'
    boton_reiniciar['state'] = 'normal'


# Rotulo del título

rotulo_titulo = tk.Label(ventana,
                         text="Selector pizzas",
                         bg="wheat", fg="black",
                         font="consolas 20 bold",
                         relief=tk.GROOVE, bd=2,
                         width=18, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

# Botones de opciones

cuadro1 = tk.LabelFrame(ventana,
                        bg="wheat",
                        text="Variedades",
                        font="arial 16 underline")

opcion_seleccionada = tk.IntVar()

opcion1 = tk.Radiobutton(cuadro1,
                         text="Margarita",
                         bg="wheat",
                         font="consolas 16",
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=1)
opcion1.pack()

opcion2 = tk.Radiobutton(cuadro1,
                         text="Hawai",
                         bg="wheat",
                         font="consolas 16",
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=2)
opcion2.pack()

opcion3 = tk.Radiobutton(cuadro1,
                         text="Napolitana",
                         bg="wheat",
                         font="consolas 16",
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=3)
opcion3.pack()

opcion4 = tk.Radiobutton(cuadro1,
                         text="Carbonara",
                         bg="wheat",
                         font="consolas 16",
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=4)
opcion4.pack()

opcion5 = tk.Radiobutton(cuadro1,
                         text="Barbacoa",
                         bg="wheat",
                         font="consolas 16",
                         width=20, anchor=tk.W,
                         variable=opcion_seleccionada,
                         value=5)
opcion5.pack()

cuadro1.pack()

# Cuadro botones

cuadro2 = tk.Frame(ventana, bg="wheat")

boton_reiniciar = tk.Button(cuadro2,
                            text="Reinicio",
                            command=reiniciar
                            )
boton_reiniciar.pack(side=tk.LEFT, padx=20, pady=20)

boton_enviar = tk.Button(cuadro2,
                         text="Enviar",
                         command=enviar)
boton_enviar.pack(side=tk.LEFT, padx=20, pady=20)

cuadro2.pack(padx=20, pady=20)

cuadro3 = tk.Frame(ventana, bg="white")

rotulo_resultado = tk.Label(cuadro3,
                            text="Elija su pizza y pulse enviar")
rotulo_resultado.pack()

cuadro3.pack()

ventana.mainloop()
