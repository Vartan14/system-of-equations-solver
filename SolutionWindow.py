from tkinter import *
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from Graphic import Graphic
from config import *


class SolutionWindow:
    def __init__(self, parent, method, matrix, title=""):
        self.__root = Toplevel(parent)
        self.__method = method
        self.__matrix = matrix
        self.__root.title(title)

        self.__solution_frame = Frame(self.__root, bg=COL1)
        self.__solution_labels = []

    def display_solution(self):
        # root configure
        self.__root.resizable(False, False)
        self.__root.configure(bg=COL1)

        # Відображення розв'язків
        self.__draw_widgets()
        self.__root.grab_set()

        # Графічний розв'язок СЛАР 2х2
        if self.__matrix.get_n() == 2:
            self.__draw_plot()

    def __draw_widgets(self):
        text = "Розв'язання заданої системи методом "

        if self.__method == 0:
            text += "Гауса:"
            vector_x = self.__matrix.gauss()
        elif self.__method == 1:
            text += "Жордана-Гауса:"
            vector_x = self.__matrix.jordan_gauss()
        else:
            text += "обертання:"
            vector_x = self.__matrix.rotation()

        # Розміщення рамки
        self.__solution_frame.grid(row=0, column=0)

        # Назва методу
        Label(self.__solution_frame, font=FONT2, text=text, bg=COL1).grid(row=0, column=0)

        # Виведення коренів
        n = len(vector_x)
        for i in range(n):
            x = round(vector_x[i], 3)
            if x == -0.0:
                x = 0.0
            text = f"x{i + 1} = {x}"
            self.__solution_labels.append(text)
            Label(self.__solution_frame, text=text, font=FONT1, bg=COL1).grid(row=i + 1, column=0, sticky=W)

        # Кількість ітерацій
        Label(self.__solution_frame, text=f"Ітерацій = {self.__matrix.get_it()}", font=FONT1, bg=COL1).grid(
            row=n+2, column=0, pady=5, sticky=W)

        # Кнопка збереження
        Button(self.__solution_frame, text="Зберегти", command=self.__save_btn, font=FONT2, bg=COL2).grid(
            row=n + 3, column=0, pady=5)

    def __save_btn(self):
        # Отримання назви файлу для запису
        file_name = fd.asksaveasfilename(initialdir="Saved Matriсes",
                                         title="Збереження текстово файлу з матрицею",
                                         filetypes=(("TEXT files", "*.txt"),))
        # Якщо не вибрано ніякого файлу
        if not file_name:
            return

        a = self.__matrix.get_init_a()
        n = len(a)

        # Запис у файл
        with open(file_name, "w") as fin:
            fin.write("Matrix:\n")
            for i in range(n):
                for j in range(n + 1):
                    fin.write(str(a[i][j]))
                    if j != n:
                        fin.write(' ')
                fin.write('\n')

            fin.write("\nSolution:\n")
            for i in range(n):
                fin.write(self.__solution_labels[i] + '\n')

            fin.write("\nIterations:\n" + str(self.__matrix.get_it()))

    def __draw_plot(self):
        # Рамка для графіку
        plt_frame = Frame(self.__root)
        plt_frame.grid(row=0, column=1)

        graphic = Graphic("Графічний розв'язок системи 2х2", self.__matrix)
        graphic.display()

        # Розміщення графіку у вікні з розв'язками
        canvas = FigureCanvasTkAgg(graphic.get_fig(), master=plt_frame)
        canvas.get_tk_widget().grid(row=0, column=0)

        # Розміщення набору інструментів
        toolbar_frame = Frame(plt_frame)
        toolbar_frame.grid(row=1, column=0, sticky=W)
        NavigationToolbar2Tk(canvas, toolbar_frame)
