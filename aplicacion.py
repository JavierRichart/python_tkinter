import tkinter as tk

name = "Javi"

ventana = tk.Tk()
ventana.title(f"Aplicación [Usuario: {name}]")
ventana.geometry("800x500+500+200")

# ventana.resizable(width=False, height=False)
# ventana.minsize(width=300, height=200)
# ventana.maxsize(width=1000, height=800)
# ventana.configure(background="snow2")

rotulo = tk.Label(ventana,
                  text="APLICACIÓN",
                  font=("consolas", 12, "bold")
                  )
rotulo.pack()


ventana.mainloop()
