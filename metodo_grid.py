import tkinter as tk

# Ventana principal

ventana = tk.Tk()
ventana.geometry("600x500+500+100")

# Aplicación

uno = tk.Button(ventana,
                text="1",
                font="consolas 30",
                bg="lightgreen",
                width=3)
uno.grid(row=0, column=0, padx=10, pady=10)

dos = tk.Button(ventana,
                text="2",
                font="consolas 30",
                bg="lightgreen",
                width=3)
dos.grid(row=0, column=1, padx=10, pady=10)

tres = tk.Button(ventana,
                 text="3",
                 font="consolas 30",
                 bg="lightgreen",
                 width=3)
tres.grid(row=0, column=2, padx=10, pady=10)

cuatro = tk.Button(ventana,
                   text="4",
                   font="consolas 30",
                   bg="lightgreen",
                   width=3)
cuatro.grid(row=1, column=0, padx=10, pady=10)

cinco = tk.Button(ventana,
                  text="5",
                  font="consolas 30",
                  bg="lightgreen",
                  width=3)
cinco.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

seis = tk.Button(ventana,
                 text="6",
                 font="consolas 30",
                 bg="lightgreen",
                 width=3)
seis.grid(row=3, rowspan=2, column=0, padx=10, pady=10)

ventana.mainloop()
