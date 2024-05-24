import tkinter as tk

# Ventana principal

ventana = tk.Tk()
# ventana.geometry("600x500+500+100")

# Aplicación

uno = tk.Button(ventana,
                text="1",
                font="consolas 30",
                bg="lightgreen")
uno.grid(row=0, column=0, sticky="nsew")

dos = tk.Button(ventana,
                text="2",
                font="consolas 50",
                bg="lightgreen")
dos.grid(row=0, column=1, sticky="nsew")

tres = tk.Button(ventana,
                 text="3",
                 font="consolas 20",
                 bg="lightgreen",)
tres.grid(row=0, column=2, sticky="nsew")

cuatro = tk.Button(ventana,
                   text="  4  ",
                   font="consolas 30",
                   bg="lightgreen",)
cuatro.grid(row=1, column=0, sticky="nsew")

cinco = tk.Button(ventana,
                  text="5",
                  font="consolas 10",
                  bg="lightgreen",)
cinco.grid(row=1, column=1, sticky="nsew")

seis = tk.Button(ventana,
                 text="6",
                 font="consolas 70",
                 bg="lightgreen",)
seis.grid(row=1, column=2, sticky="nsew")

ventana.mainloop()
