import numpy as np
import random

class Matrix:
    def __init__(self, a):
        self.__init_a = a                   # initial extended matrix
        self.__n = len(self.__init_a)       # size
        self.__a = self.__get_a_copy()      # extended matrix
        self.__x = [0] * self.__n           # vector x
        self.__iterations = 0               # iterations

    def get_it(self):
        return self.__iterations

    def get_init_a(self):
        return self.__init_a

    def get_n(self):
        return self.__n

    def get_x(self):
        return self.__x

    def is_solvable(self):
        a = self.__get_matrix_without_b()
        if self.__n > 2:
            det_a =  np.linalg.det(np.array(a))
        else:
            det_a = a[0][0] * a[1][1] - a[0][1] * a[1][0]

        if det_a != 0:
            return True
        else:
            return False

    def __get_a_copy(self):
        a = []
        for row in self.__init_a:
            a.append(row.copy())
        return a

    def __get_matrix_without_b(self):
        a = []
        for i in range(self.__n):
            a.append([])
            for j in range(self.__n):
                    a[i].append(self.__init_a[i][j])
        return a

    def __get_max_in_column(self,col):
        max_el = abs(self.__a[col][col])
        index = col
        for j in range(col + 1, self.__n):
            if abs(self.__a[j][col]) > max_el:
                max_el = abs(self.__a[j][col])
                index = j
                self.__iterations += 1

        return index

    # Зворотній хід
    def __gauss_backward_trace(self):
        n = self.__n
        for i in range(n - 1, -1, -1):
            self.__x[i] = self.__a[i][n] / self.__a[i][i]
            for j in range(i):
                self.__a[j][n] = self.__a[j][n] - self.__a[j][i] * self.__x[i]
                self.__iterations += 1
        return self.__x

    def gauss(self):
        # Цикл по стовпцям
        for i in range(self.__n-1):
            # Шукаємо рядок з найбільшим першим елементом
            index = self.__get_max_in_column(i)
            # Підінімаємо нагору рядок з найбільшим першим елементом
            for j in range(self.__n + 1):
                self.__a[i][j], self.__a[index][j] = self.__a[index][j], self.__a[i][j]
                self.__iterations += 1

            # Обнулення стовпця під діагональним елементом [i][i]
            for j in range(i+1, self.__n):
                temp = self.__a[j][i]/self.__a[i][i]
                for k in range(self.__n + 1):
                    self.__a[j][k] -= self.__a[i][k] * temp
                    self.__iterations += 1

        return self.__gauss_backward_trace()


    def jordan_gauss(self):
        for i in range(self.__n):
            # Шукаємо рядок з найбільшим першим елементом
            index = self.__get_max_in_column(i)
            # Підінімаємо нагору рядок з найбільшим першим елементом
            for j in range(self.__n + 1):
                self.__a[i][j], self.__a[index][j] = self.__a[index][j], self.__a[i][j]
                self.__iterations += 1

            # Робимо одиницею [і][i]-тий елемент головної діагоналі
            temp = self.__a[i][i]
            for k in range(self.__n + 1):
                self.__a[i][k] /= temp
                self.__iterations += 1
            # Робими нулями всі елементи стовпця крім діагонального
            for j in range(self.__n):
                if i != j:
                    temp = self.__a[j][i]
                    for k in range(self.__n + 1):
                        self.__a[j][k] -= self.__a[i][k] * temp
                        self.__iterations += 1
        # Виділення коренів
        for i in range(self.__n):
            self.__x[i] = self.__a[i][-1]
            self.__iterations += 1
        return self.__x

    def rotation(self):
        # Прямий хід
        for i in range(self.__n - 1):
            for j in range(i + 1, self.__n):
                c = self.__a[i][i] / (self.__a[i][i] ** 2 + self.__a[j][i] ** 2) ** 0.5
                s = self.__a[j][i] / (self.__a[i][i] ** 2 + self.__a[j][i] ** 2) ** 0.5
                for k in range(self.__n + 1):
                    tmp1 = round(c * self.__a[i][k] + s * self.__a[j][k], 14)
                    tmp2 = round(-s * self.__a[i][k] + c * self.__a[j][k], 14)
                    self.__a[i][k] = tmp1
                    self.__a[j][k] = tmp2
                    self.__iterations += 1

        # Зворотній хід
        return self.__gauss_backward_trace()



if __name__ == '__main__':
    size = 500
    m = []
    for i in range(size):
        m.append([])
        for j in range(size+1):
            m[i].append(random.randint(1,10))

    # for i in range(size):
    #     print(m[i])




    A = Matrix(m)
    B = Matrix(m)
    C = Matrix(m)

    print("----------------------------------------------------------\nGauss")
    ax = A.gauss()
    #print("x = ", ax)

    print(f"Iterations = {A.get_it()}\n"
          f"Operations = {A.get_op()}")

    print("----------------------------------------------------------\nJordan - Gauss")
    bx = B.jordan_gauss()
    #print("x = ", bx)

    print(f"Iterations = {B.get_it()}\n"
          f"Operations = {B.get_op()}")

    print("----------------------------------------------------------\nRotation")
    cx = C.rotation()
    #print("x = ", cx)

    print(f"Iterations = {C.get_it()}\n"
          f"Operations = {C.get_op()}")