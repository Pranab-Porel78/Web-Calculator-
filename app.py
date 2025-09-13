import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result, width=25, borderwidth=4, font=('Arial', 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                tk.Button(master, text=text, width=5, height=2, command=self.calculate).grid(row=row, column=col)
            elif text == 'C':
                tk.Button(master, text=text, width=22, height=2, command=self.clear).grid(row=row, column=col, columnspan=4)
            else:
                tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.append(t)).grid(row=row, column=col)

    def append(self, char):
        self.result.set(self.result.get() + char)

    def clear(self):
        self.result.set('')

    def calculate(self):
        try:
            result = str(eval(self.result.get()))
            self.result.set(result)
        except Exception:
            self.result.set('Error')

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
