import tkinter as tk

# Ventana principal

ventana = tk.Tk()
ventana.title("Bind method")
ventana.geometry("500x400+600+100")
ventana.configure(bg="lightblue")


# Funciones

def pulsar(event):
    if event.char == "q":
        rotulo.config(text=f"Muy bien")
    else:
        rotulo.config(text=f"Has pulsado {event.char}")


# Widgets

rotulo = tk.Label(ventana,
                  text="Pulsa la letra q",
                  font="consolas 20",
                  bg="lightblue")
rotulo.pack(pady=20, ipadx=20)

ventana.bind("<Key>", pulsar)
ventana.mainloop()
