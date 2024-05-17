import tkinter as tk

# Ventana

ventana = tk.Tk()
ventana.title("Bind method")
ventana.geometry("500x400+600+100")
ventana.configure(bg="lightblue")


# Funciones

def cambiar_rojo(event):
    rotulo.config(bg="red")
    rotulo.unbind("<Button-3>")


def cambiar_verde(event):
    rotulo.config(bg="green")
    rotulo.unbind("<Button-1>")


def reiniciar():
    rotulo.config(bg="lightgrey")
    rotulo.bind("<Button-1>", cambiar_rojo)
    rotulo.bind("<Button-3>", cambiar_verde)


# Widgets

rotulo = tk.Label(ventana,
                  text=" 1 ",
                  bg="lightgrey",
                  font="consolas 40")
rotulo.pack(pady=50)

rotulo.bind("<Button-1>", cambiar_rojo)

rotulo.bind("<Button-3>", cambiar_verde)

boton = tk.Button(ventana,
                  text="Reiniciar",
                  bg="lightgrey",
                  font="consolas 20",
                  command=reiniciar)
boton.pack(pady=20)

ventana.mainloop()
