import tkinter as tk
#import pytest

def create_calculator():
    window = tk.Tk()
    b = 1;
    #12345
    window.title("Калькулятор")
    window.geometry("300x400")
    window.resizable(False, False)

    entry_field = tk.Entry(window, width=20, font=('Arial', 20), bd=5, insertwidth=4, justify='right')
    entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def button_click(item):
        current = entry_field.get()
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(current) + str(item))

    def button_clear():
        entry_field.delete(0, tk.END)

    def button_equal():
        try:
            expression = entry_field.get()
            result = str(eval(expression))
            entry_field.delete(0, tk.END)
            entry_field.insert(0, result)
        except Exception as e:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, "Ошибка")

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 2),
        ('+', 4, 3),
        ('C', 5, 0),
        ('=', 5, 2)
    ]

    for (text, row, col) in buttons:
        if text == 'C':
            btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=button_clear, bg="#ff9999")
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        elif text == '=':
            btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=button_equal, bg="#99ff99")
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        elif text == '0':
            btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t), bg="#e6e6e6")
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        else:
            btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t), bg="#e6e6e6" if text not in ('/', '*', '-', '+') else "#cceeff")
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    for i in range(6):
        window.grid_rowconfigure(i, weight=1)
    for i in range(4):
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()

if __name__ == "__main__":
    create_calculator()