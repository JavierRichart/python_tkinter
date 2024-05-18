import tkinter as tk

# Ventana principal

ventana = tk.Tk()
ventana.geometry("500x400+600+100")
ventana.configure(bg="lightblue")


# Funciones

def pulsar():
    rotulo.config(text="Pulsado el botón\nde alarma",
                  bg="red", fg="white", font="consolas 20")


def entrar(event):
    boton.config(text="¿Estás seguro?", bg="red")


def salir(event):
    boton.config(text="BOTÓN DE ALARMA", bg="orange")


# Widgets

boton = tk.Button(ventana,
                  text="BOTÓN DE ALARMA",
                  bg="orange",
                  font="consolas 20",
                  width=20, height=3,
                  command=pulsar)
boton.pack(pady=50)

boton.bind("<Enter>", entrar)
boton.bind("<Leave>", salir)

rotulo = tk.Label(ventana,
                  text="En caso de alarma\n pulsa el botón",
                  font="consolas 20",
                  padx=25, pady=25)
rotulo.pack()

ventana.mainloop()
