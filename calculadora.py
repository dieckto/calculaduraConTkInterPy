import tkinter as tk
import math
import re

from utils import *
   

class Calculadora:
    def __init__(self, root):
        # Ventana
        self.root = root
        self.root.title("Calculadora")
        self.root.config(bg="#F5F5F5")  # gris muy muy claro

        # Pantalla principal
        self.pantalla = tk.Entry(
            self.root, font=("Segoe UI", 22),
            bg="white", fg="black", justify='right',
            relief="flat", highlightthickness=1, highlightbackground="#DDD"
        )
        self.pantalla.grid(row=0, column=0, columnspan=5, padx=20, pady=(20,10), sticky="nsew")

        # Pantalla secundaria (para notaciones)
        self.frame_notaciones = tk.Frame(self.root, bg="#F5F5F5")
        self.frame_notaciones.grid(row=1, column=0, columnspan=5, padx=20, pady=(0,10), sticky="nsew")

        # Hexadecimal
        self.hex_label = tk.Label(self.frame_notaciones, text="Hexadecimal:", font=("Segoe UI", 12), bg="#F5F5F5", fg="black")
        self.hex_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.hex_display = tk.Entry(self.frame_notaciones, font=("Segoe UI", 14), bg="white", fg="black", justify="right", relief="flat")
        self.hex_display.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Octal
        self.oct_label = tk.Label(self.frame_notaciones, text="Octal:", font=("Segoe UI", 12), bg="#F5F5F5", fg="black")
        self.oct_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.oct_display = tk.Entry(self.frame_notaciones, font=("Segoe UI", 14), bg="white", fg="black", justify="right", relief="flat")
        self.oct_display.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        # Binario
        self.bin_label = tk.Label(self.frame_notaciones, text="Binario:", font=("Segoe UI", 12), bg="#F5F5F5", fg="black")
        self.bin_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.bin_display = tk.Entry(self.frame_notaciones, font=("Segoe UI", 14), bg="white", fg="black", justify="right", relief="flat")
        self.bin_display.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")

        # Ajustar proporciones dentro del frame
        for i in range(6):
            self.frame_notaciones.grid_columnconfigure(i, weight=1)
        self.crear_botones()

        # Ajustes proporcionales de la ventana principal
        for i in range(7):  # filas
            self.root.grid_rowconfigure(i, weight=2 if i > 1 else 1)  
        for j in range(5):  # columnas
            self.root.grid_columnconfigure(j, weight=1)

    def crear_botones(self):
        botones = [
            ("A",2,0),('(', 2, 1), (')', 2, 2), ('C', 2, 3), ('<-', 2, 4),
            ("B",3,0),('%', 3, 1), ('√', 3, 2), ('^', 3, 3), ('/', 3, 4),
            ("C",4,0),('9', 4, 1), ('8', 4, 2), ('7', 4, 3), ('*', 4, 4),
            ("D",5,0),('6', 5, 1), ('5', 5, 2), ('4', 5, 3), ('-', 5, 4),
            ("E",6,0),('3', 6, 1), ('2', 6, 2), ('1', 6, 3), ('+', 6, 4),
            ("F",7,0),('!', 7, 1), ('0', 7, 2), ('.', 7, 3), ('=', 7, 4)
        ]

        for (text, row, col) in botones:
            if text == "=":
                boton = tk.Button(
                    self.root, text=text,
                    font=("Segoe UI", 18, "bold"),
                    bg="#0066CC", fg="white", relief="flat",
                    activebackground="#3399FF", activeforeground="white",
                    command=lambda t=text: self.btb_click(t)
                )
            else:
                boton = tk.Button(
                    self.root, text=text,
                    font=("Segoe UI", 18),
                    bg="white", fg="black", relief="flat",
                    activebackground="#4DA6FF", activeforeground="white",
                    command=lambda t=text: self.btb_click(t)
                )

            # Hover effect
            boton.bind("<Enter>", lambda e, b=boton: b.config(bg="#3399FF", fg="white"))
            boton.bind("<Leave>", lambda e, b=boton, t=text: b.config(
                bg="#0066CC" if t == "=" else "white",
                fg="white" if t == "=" else "black"
            ))

            boton.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def btb_click(self, valor):
        if valor == 'C':
            self.pantalla.delete(0, tk.END)
            self.hex_display.delete(0, tk.END)
            self.oct_display.delete(0, tk.END)
            self.bin_display.delete(0, tk.END)
        elif valor == '<-':
            self.pantalla.delete(len(self.pantalla.get()) - 1, tk.END)
        elif valor == '=':
            self.obtener_resultado(self.pantalla.get())
        else:
            self.pantalla.insert(tk.END, valor)

    def obtener_resultado(self, expresion):
        try:
            expresion = expresion.replace("^", "**")
            expresion = re.sub(r"√(\d+|\([^\)]+\))", r"(\1**0.5)",expresion)

                        # 1. Potencias (cambia ^ por **)
            expresion = expresion.replace("^", "**")

            # 2. Raíz cuadrada de un número o expresión
            expresion = re.sub(r"√(\d+)", r"(math.sqrt(\1))", expresion)
            expresion = re.sub(r"√\(([^)]+)\)", r"(math.sqrt(\1))", expresion)

            # 3. Porcentajes A%B → (A*(B/100))
            expresion = re.sub(r"(\d+)%(\d+)", r"(\1*(\2/100))", expresion)

            # 4. Factoriales n! → math.factorial(n)
            expresion = re.sub(r"(\d+)!", r"(math.factorial(\1))", expresion)

            resultado = eval(expresion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, str(resultado))

            entero = int(resultado)
            # Por ahora solo limpiamos las pantallas secundarias
            self.hex_display.delete(0, tk.END)
            self.oct_display.delete(0, tk.END)
            self.bin_display.delete(0, tk.END)

            self.hex_display.insert(0, dec_to_hex(entero))
            self.oct_display.insert(0, dec_to_oct(entero))
            self.bin_display.insert(0, dec_to_bin(entero))

        except Exception as e:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "Error")
            print("Error:", e)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
