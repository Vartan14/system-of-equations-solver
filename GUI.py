import random
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from tkinter import filedialog as fd


from config import *
from Matrix import Matrix
from SolutionWindow import SolutionWindow


class Window:
    def __init__(self, title="", icon=None):
        self.__root = Tk()
        self.__root.title(title)
        if icon:
            self.__root.iconbitmap(icon)
        self.__root.configure(bg=COL1)
        self.__root.resizable(False, False)
        # Frames
        self.__size_frame = Frame(self.__root, bg=COL1)
        self.__matrix_frame = Frame(self.__root, bg=COL1)
        self.__method_frame = Frame(self.__root, bg=COL1)

        # Widgets
        self.__combo_box = Combobox(self.__size_frame, width=5, font=FONT1,
                                    values=("2", "3", "4", "5", "6", "7", "8"), state="readonly")
        # Матриця полів
        self.__matrix_entry = []
        # Вибір методу
        self.__method_choice = IntVar()

    def open_file(self):
        file_name = fd.askopenfilename(title="Відкрийте текстовий файл з матрицею", initialdir="Examples")

        if not file_name:
            return

        with open(file_name, "r") as file_out:
            text = file_out.read()

        rows = text.split('\n')
        matrix = []
        for row in rows:
            matrix.append(row.split())

        n = len(matrix)

        try:
            self.__combo_box.current(n-2)
            self.__size_selected("unusable")
            for i in range(n):
                for j in range(n+1):
                    self.__matrix_entry[i][j].delete(0, END)
                    self.__matrix_entry[i][j].insert(0, matrix[i][j])
        except IndexError:
            self.__combo_box.current(0)
            self.__size_selected("unusable")
            mb.showerror("Помилка зчитування", "Матриця задана некоректно")

    def __draw_menu(self):
        menu_bar = Menu(self.__root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.__root.configure(menu=menu_bar)

    def run(self):
        self.__draw_widgets()
        self.__draw_menu()
        self.__root.mainloop()

    def __draw_widgets(self):
        # Відображення рамки з вибором розмірності матриці
        self.__size_frame.grid(row=0, column=0, sticky=W, pady=5)
        # Відображення елементів на ній
        self.__fill_size_frame()

        # Відображення рамки з матрицею
        self.__matrix_frame.grid(row=1, column=0, columnspan=2, sticky=EW, pady=5)
        # Відображення поля для вводу матриці 2х2 за замовчуванням
        self.__size_selected()

        # Відображення рамки з вибором методів
        self.__method_frame.grid(row=2, column=0, sticky=W, pady=5)

    def __fill_size_frame(self):
        Label(self.__size_frame, text="Задайте розмірність матриці:", font=FONT2, bg=COL1).grid(
            row=0, column=0, sticky=W)
        self.__combo_box.grid(row=0, column=1, sticky=W)
        self.__combo_box.current(0)
        self.__combo_box.bind("<<ComboboxSelected>>", self.__size_selected)
        Button(self.__size_frame, width=12, height=1, text="Згенерувати", command=self.__generate_btn,
               font=FONT3, bg=COL2).grid(row=0, column=2, padx=5)

    def __size_selected(self, event=None):
        # Поля для введення матриці
        self.__draw_fields()

        # Вибір методу вирішення
        self.__draw_methods()

        # Кнопка вирішення
        Button(self.__root, text="Вирішити", font=FONT2, command=self.__solve_btn, bg=COL2).grid(
            row=5, column=0, sticky=SW, pady=5, padx=5)

    def __draw_fields(self):
        # Отримання розмірності матриці
        n = int(self.__combo_box.get())

        # Очищення рамки з попередньою матрицею
        self.__clear_frame(self.__matrix_frame)

        # Створення масиву для Entry
        self.__matrix_entry = []

        #  Заповнення матриці A entry
        for i in range(n):
            self.__matrix_entry.append([])
            for j in range(n + 1):
                self.__matrix_entry[i].append(Entry(self.__matrix_frame, width=7, font=FONT1, relief=SUNKEN))
                self.__matrix_entry[i][j].insert(0, 0)

        # Розміщення полів для вводу матриці
        for i in range(n):
            for j in range(n * 2 + 1):
                ind = j // 2
                if j % 2 == 0:
                    temp = self.__matrix_entry[i][ind]
                else:
                    if j != n * 2 - 1:
                        temp = Label(self.__matrix_frame, text=f"x{ind + 1} +", font=FONT1, bg=COL1)
                    else:
                        temp = Label(self.__matrix_frame, text=f"x{ind + 1} =", font=FONT1, bg=COL1)
                temp.grid(row=i, column=j, sticky=W, padx=5)

    def __draw_methods(self):
        Label(self.__method_frame, text="Оберіть метод вирішення:", font=FONT2, bg=COL1).grid(
            row=0, column=0, columnspan=3, sticky=W)
        Radiobutton(self.__method_frame, text="Метод Гауса", font=FONT1, bg=COL1, selectcolor=COL2,
                    activebackground=COL2, variable=self.__method_choice, value=0).grid(row=1, column=0, sticky=W)
        Radiobutton(self.__method_frame, text="Метод Жордана-Гауса", font=FONT1, bg=COL1, selectcolor=COL2,
                    activebackground=COL2, variable=self.__method_choice, value=1).grid(row=2, column=0, sticky=W)
        Radiobutton(self.__method_frame, text="Метод обертання", font=FONT1, bg=COL1, selectcolor=COL2,
                    activebackground=COL2, variable=self.__method_choice, value=2).grid(row=3, column=0, sticky=W)

    def __generate_btn(self):
        # Заповнення полів випадковими числами
        while True:
            for row in self.__matrix_entry:
                for entry in row:
                    random.seed()
                    entry.delete(0, END)
                    entry.insert(0, round(random.uniform(-50, 50), 3))

            matrix = Matrix(self.__get_matrix())
            # Перевірка чи має СЛАР розв'язки
            if matrix.is_solvable():
                return

    def __solve_btn(self):
        # Отримання матриці
        a = self.__get_matrix()
        if a:
            matrix = Matrix(a)
        else:
            return

        # Якщо матриця не має розв'язків
        if not matrix.is_solvable():
            mb.showerror(title="Помилка", message="Визначник дорівнює нулю. Розв'язків немає!")
            return
        # Отримання методу
        method = self.__method_choice.get()

        # Виклик дочірнього вікна з розв'язанням
        solution = SolutionWindow(self.__root, method, matrix, title="Розв'язання СЛАР")
        solution.display_solution()

    @staticmethod
    def __clear_frame(frame):
        # Очищення усіх віджетів, що є у рамці
        for widget in frame.winfo_children():
            widget.destroy()

    # Отримання матриці з Entry
    def __get_matrix(self):
        n = int(self.__combo_box.get())
        matrix = []
        try:
            for i in range(n):
                matrix.append([])
                for j in range(n + 1):
                    line = self.__matrix_entry[i][j].get()
                    if len(line) <= 15:
                        matrix[i].append(float(line))
                    else:
                        mb.showerror("Помилка", "Вводьте не більше 15 цифр!")
                        self.__matrix_entry[i][j].delete(0, END)
                        self.__matrix_entry[i][j].insert(0, 0)
                        return

        except ValueError:
            mb.showerror("Помилка", "Вводьте в поля для коефіцієнтів тільки цифри!")
            return

        return matrix
