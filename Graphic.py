import numpy as np
from matplotlib.figure import Figure
from config import COL2


class Graphic:
    def __init__(self, title, matrix):
        self.__fig = Figure(figsize=(7, 5))
        self.__ax = self.__fig.add_subplot(111)
        self.__fig.suptitle(title, fontsize=14)

        self.__matrix = matrix
        self.__a = self.__matrix.get_init_a()

    def get_fig(self):
        return self.__fig

    def display(self):
        # Сітка
        self.__ax.grid(which='both', color='grey', linewidth=1, alpha=0.2)

        # Назви координатних осей
        self.__ax.set_xlabel('x1', fontsize=14)
        self.__ax.set_ylabel('x2', fontsize=14)

        # Відображення графіків прямих
        self.__display_plots()

        # Точка перетину
        roots = self.__matrix.get_x()
        self.__ax.scatter(roots[0], roots[1], s=100, color=COL2)

        # Легенда графіка
        self.__ax.legend(loc='upper left')

    def __display_plots(self):
        for i in range(2):
            if i == 0:
                color = "red"
            else:
                color = "blue"

            text = self.__get_name(i)
            x, y = self.__get_coordinates(i)

            self.__ax.plot(x, y, label=text, color=color)

    def __get_name(self, i):
        text = f""

        if self.__a[i][0] == 0:
            text += ""
        else:
            text += f"{self.__a[i][0]}x1"

        if self.__a[i][1] != 0:
            if self.__a[i][0] != 0:
                if self.__a[i][1] > 0:
                    text += f" + {self.__a[i][1]}x2"
                else:
                    text += f" - {abs(self.__a[i][1])}x2"
            else:
                text += f"{self.__a[i][1]}x2"

        text += f" = {self.__a[i][2]}"

        return text

    def __get_coordinates(self, i):
        start = -5
        stop = 5
        step = 0.01

        roots = self.__matrix.get_x()

        # Немає нульових коефіцієнтів
        if self.__a[i][1] != 0:
            x = np.arange(roots[0] + start, roots[0] + stop, step)
            y = (self.__a[i][2] - self.__a[i][0] * x) / self.__a[i][1]
        # x = a
        else:
            if i == 0:
                ind = i + 1
            else:
                ind = i - 1
            # x = a and x + y =b
            if self.__a[ind][0] != 0:
                min_x = roots[0] + start
                max_x = roots[0] + stop

                y1 = (self.__a[ind][2] - self.__a[ind][0] * max_x) / self.__a[ind][1]
                y2 = (self.__a[ind][2] - self.__a[ind][0] * min_x) / self.__a[ind][1]

                max_y = max(y1, y2)
                min_y = min(y1, y2)

                y = np.arange(min_y, max_y + step, step)
                x = (self.__a[i][2] - 0 * y) / self.__a[i][0]

            # x = a and y = b
            else:
                min_y = roots[1] + start
                max_y = roots[1] + stop

                y = np.arange(min_y, max_y + step, step)
                x = (self.__a[i][2] - 0 * y) / self.__a[i][0]

        return x, y


