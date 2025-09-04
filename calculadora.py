import tkinter as tk
import re   

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

            ("A",1,0),('(', 1, 1), (')', 1, 2), ('C', 1, 3), ('<-', 1, 4),
            ("B",2,0),('%', 2, 1), ('√', 2, 2), ('^', 2, 3), ('/', 2, 4),
            ("C",3,0),('9', 3, 1), ('8', 3, 2), ('7', 3, 3), ('*', 3, 4),
            ("D",4,0),('6', 4, 1), ('5', 4, 2), ('4', 4, 3), ('-', 4, 4),
            ("E",5,0),('3', 5, 1), ('2', 5, 2), ('1', 5, 3), ('+', 5, 4),
            ("F",6,0),('/', 6, 1), ('0', 6, 2), ('.', 6, 3), ('=', 6, 4)
        ]

        for (text, row, col) in botones:
            button = tk.Button(self.root, text=text, width=10, height=3, border=2,font=("Arial", 14), bg="lightgray", fg="black",
                               command=lambda t=text: self.btb_click(t))
            button.grid(row=row, column=col)


    def btb_click(self, valor):
        if valor == 'C':
            self.pantalla.delete(0, tk.END)
        elif valor == '<-':
            self.pantalla.delete(len(self.pantalla.get()) - 1, tk.END)
        elif valor == '=':
            self.obtener_resultado(self.pantalla.get())
        else:
            self.pantalla.insert(tk.END, valor)

    def obtener_resultado(self, expresion):
        try:
            # 🔹 reemplaza ^ por **
            expresion = expresion.replace("^", "**")
            # 🔹 transforma √n o √(...) en (n)**0.5 o ((...))**0.5
            expresion = re.sub(r"√(\d+|\([^\)]+\))", r"(\1)**0.5", expresion)
            # 🔹 evalúa la expresión
            resultado = eval(expresion)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, str(resultado))
        except Exception as e:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "Error")
            print("Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
