import tkinter as tk


class Calculadora:
    def __init__(self, root):
        #configuraciones de la ventana
        self.root = root
        self.root.title("Calculadora")
        self.root.config(bg="black")

        #configuraciones de la pantalla 
        self.pantalla = tk.Entry(self.root, width=40, font=("Arial", 16), bg="white", fg="black", justify='right')
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('CE', 5, 1), ('(', 5, 2), (')', 5, 3)
        ]

        for (text, row, col) in botones:
            button = tk.Button(self.root, text=text, width=10, height=3, border=2,font=("Arial", 14), bg="lightgray", fg="black",
                               command=lambda t=text: self.btb_click(t))
            button.grid(row=row, column=col)


    def btb_click(self, valor):
        if valor == 'C':
            self.pantalla.delete(0, tk.END)
        elif valor == 'CE':
            self.pantalla.delete(len(self.pantalla.get()) - 1, tk.END)
        elif valor == '=':
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except Exception as e:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        else:
            self.pantalla.insert(tk.END, valor)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
