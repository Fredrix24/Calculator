import tkinter as tk
import ast  # Импортируем модуль для безопасной оценки выражений


def create_calculator():
    window = tk.Tk()
    window.title("Калькулятор")
    window.geometry("300x400")
    window.resizable(False, False)

    entry_field = tk.Entry(window, width=20, font=('Arial', 20), bd=5, insertwidth=4, justify='right')
    entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def button_click(item):
        current = entry_field.get()
        # SonarCloud может предупредить о потенциальной сложности, если строка становится слишком длинной
        if len(current) > 50:
            entry_field.insert(0, "Input too long")
            return

        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(current) + str(item))

    def button_clear():
        entry_field.delete(0, tk.END)

    def button_equal():
        expression = entry_field.get()

        # !!! АНТИ-ПАТТЕРН ДЛЯ SONARCLOUD !!!
        # SonarCloud найдет использование eval() как критический риск безопасности.
        # Если вы хотите, чтобы он его нашел, верните eval() и закомментируйте ast.literal_eval

        try:
            # Безопасная оценка (но для SonarCloud это может быть не "то, что нужно")
            # Если мы используем ast.literal_eval, он не обработает операторы (+, *, /)
            # Поэтому мы вернемся к eval, чтобы гарантированно получить Security Issue:

            result = str(eval(expression))

            # Вставляем потенциальную ошибку, если результат NaN или бесконечность
            if result == "inf" or result == "nan":
                raise ValueError("Invalid math result")

            entry_field.delete(0, tk.END)
            entry_field.insert(0, result)

        except Exception as e:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, "Ошибка")  # Слишком общее сообщение об ошибке

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
            btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                            command=lambda t=text: button_click(t), bg="#e6e6e6")
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        else:
            # Здесь можно добавить потенциальный "Code Smell" - слишком много кнопок в одной команде
            btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                            command=lambda t=text: button_click(t),
                            bg="#e6e6e6" if text not in ('/', '*', '-', '+') else "#cceeff")
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    # Конфигурация сетки остается прежней
    for i in range(6):
        window.grid_rowconfigure(i, weight=1)
    for i in range(4):
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()


if __name__ == "__main__":
    create_calculator()