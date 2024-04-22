import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("700x500+500+100")


# Función

def mostrar():
    titulo.set(entrada.get())


# Rótulo

titulo = tk.StringVar()

rotulo = tk.Label(ventana,
                  # text="Título",
                  bg="coral",
                  font="consolas 24 bold",
                  textvariable=titulo)
rotulo.pack(padx=20, pady=20)

titulo.set("Título")

# Entrada

entrada = tk.Entry(ventana,
                   bg="lightgreen",
                   font="consolas 24 bold",
                   textvariable=titulo)
entrada.pack(padx=20, pady=20)

# Botón

boton = tk.Button(ventana,
                  bg="lightblue",
                  # text="Botón",
                  textvariable=titulo,
                  font="consolas 24 bold",
                  command=mostrar)
boton.pack(padx=20, pady=20)

ventana.mainloop()
