import tkinter as tk
import random

class MainApp(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Тест умножения")
        self.geometry("450x150")

        label = tk.Label(self, text="ТРЕНАЖЕР ПО МАТЕМАТИКЕ",
                         font=("Times New Roman", 18, "bold"))
        label.grid(row=0, column=0)

        btn_table = tk.Button(self, text="Теория", command=self.show_table)
        btn_table.grid(row=1, column=0)

        btn_test = tk.Button(self, text="Тест", command=self.show_test)
        btn_test.grid(row=2, column=0)

    def show_table(self):
        Table().mainloop()

    def show_test(self):
        Test().mainloop()


class Table(tk.Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        # Вывод таблицы умножения
        self.title("Таблица умножения")
        for a in range(10):
            for b in range(10):
                lbl = tk.Label(self, text=f"{a} * {b} = {a * b}  |")
                lbl.grid(row=a, column=b)


class Test(tk.Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        # Получим цифры и ответы их умножения
        res = self.get_num()
        # Напишем пример
        label_question = tk.Label(self, text=f"{res[0]} * {res[1]} = ?",
                                  font=("Times New Roman", 12, "bold"))
        label_question.grid(row=0, column=0)
        # Поле для ответа
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0)
        # Кнопка результата
        btn_res = tk.Button(self, text="Проверить ответ", command=lambda: self.check(res[2]))
        btn_res.grid(row=2, column=0)

        # Напишем ответ
        self.label_ans = tk.Label(self, text=f"", font=("Times New Roman", 12, "bold"))
        self.label_ans.grid(row=3, column=0)

    def get_num(self):
        'Получить радомных 2 int числа от 0 до 100 и результат их умножения'
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        ans = a * b
        return (a, b, ans)

    def check(self, res):
        try:
            ans = int(self.entry.get())
            if ans == res:
                self.label_ans['text'] = "Абсолютно правильно!"
            else:
                self.label_ans['text'] = "Решение не верно!"
        except:
            self.label_ans['text'] = "Проверьте ввод!"


if __name__ == '__main__':
    MainApp().mainloop()
