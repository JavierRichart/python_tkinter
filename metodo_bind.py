import tkinter as tk

# Ventana principal

ventana = tk.Tk()
ventana.title("Bind method")
ventana.geometry("500x400+600+100")
ventana.configure(bg="lightblue")


# Funciones

def saludar(event):
    nombre = entrada.get()
    rotulo.config(text=f"Hola, {nombre}")


# Widgets

entrada = tk.Entry(ventana,
                   font="consolas 20")
entrada.pack(pady=50)
entrada.bind("<Return>", saludar)

rotulo = tk.Label(ventana,
                  text="Introduce nombre",
                  font="consolas 20",
                  bg="lightblue")
rotulo.pack(pady=20)

ventana.mainloop()
