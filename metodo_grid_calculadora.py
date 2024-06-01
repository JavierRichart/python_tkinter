import tkinter as tk

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("+600+100")

marco = tk.Frame(ventana)

# Widgets

pantalla = tk.Label(marco,
                    text="0",
                    bg="white",
                    font="consolas 20 bold",
                    anchor="e",
                    relief="sunken", bd=4)
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

limpiar = tk.Button(marco,
                    text="C",
                    font="consolas 20 bold",
                    relief="raised", bd=3,
                    width=4)
limpiar.grid(row=1, column=0, columnspan=2, sticky="nsew")

division = tk.Button(marco,
                     text="/",
                     font="consolas 20 bold",
                     relief="raised", bd=3,
                     width=4)
division.grid(row=1, column=2)

multiplicacion = tk.Button(marco,
                           text="*",
                           font="consolas 20 bold",
                           relief="raised", bd=3,
                           width=4)
multiplicacion.grid(row=1, column=3)

siete = tk.Button(marco,
                  text="7",
                  font="consolas 20 bold",
                  relief="raised", bd=3,
                  width=4)
siete.grid(row=2, column=0)

ocho = tk.Button(marco,
                 text="8",
                 font="consolas 20 bold",
                 relief="raised", bd=3,
                 width=4)
ocho.grid(row=2, column=1)

nueve = tk.Button(marco,
                  text="9",
                  font="consolas 20 bold",
                  relief="raised", bd=3,
                  width=4)
nueve.grid(row=2, column=2)

restar = tk.Button(marco,
                   text="-",
                   font="consolas 20 bold",
                   relief="raised", bd=3,
                   width=4)
restar.grid(row=2, column=3)

cuatro = tk.Button(marco,
                   text="4",
                   font="consolas 20 bold",
                   relief="raised", bd=3,
                   width=4)
cuatro.grid(row=3, column=0)

cinco = tk.Button(marco,
                  text="5",
                  font="consolas 20 bold",
                  relief="raised", bd=3,
                  width=4)
cinco.grid(row=3, column=1)

seis = tk.Button(marco,
                 text="6",
                 font="consolas 20 bold",
                 relief="raised", bd=3,
                 width=4)
seis.grid(row=3, column=2)

sumar = tk.Button(marco,
                  text="+",
                  font="consolas 20 bold",
                  relief="raised", bd=3,
                  width=4)
sumar.grid(row=3, column=3)

uno = tk.Button(marco,
                text="1",
                font="consolas 20 bold",
                relief="raised", bd=3,
                width=4)
uno.grid(row=4, column=0)

dos = tk.Button(marco,
                text="2",
                font="consolas 20 bold",
                relief="raised", bd=3,
                width=4)
dos.grid(row=4, column=1)

tres = tk.Button(marco,
                 text="3",
                 font="consolas 20 bold",
                 relief="raised", bd=3,
                 width=4)
tres.grid(row=4, column=2)

igual = tk.Button(marco,
                  text="=",
                  font="consolas 20 bold",
                  relief="raised", bd=3,
                  width=4)
igual.grid(row=4, column=3, rowspan=2, sticky="nsew")

punto = tk.Button(marco,
                  text=".",
                  font="consolas 20 bold",
                  relief="raised", bd=3,
                  width=4)
punto.grid(row=5, column=0)

cero = tk.Button(marco,
                 text="0",
                 font="consolas 20 bold",
                 relief="raised", bd=3,
                 width=4)
cero.grid(row=5, column=1)

borrar = tk.Button(marco,
                   text="<-",
                   font="consolas 20 bold",
                   relief="raised", bd=3,
                   width=4)
borrar.grid(row=5, column=2)

marco.pack(padx=3, pady=3)

ventana.mainloop()
