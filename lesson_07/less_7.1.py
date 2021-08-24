print("Исходные матрицы")


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        t = []
        for a in range(len(self.matrix)):
            t.append([])
            for b in range(len(self.matrix[0])):
                t[a].append(self.matrix[a][b] + other.matrix[a][b])

        for el in t:
            print()
            for ins in el:
                print(f"{ins}", end="    ")


    def __str__(self):
        for el in self.matrix:
            print()
            for ins in el:
                print(f"{ins}", end="    ")


matrix1 = Matrix([[94, 43], [45, 63], [20, 14]])
matrix2 = Matrix([[49, 34], [55, 87], [25, 23]])

str(matrix1.__str__())
print()
str(matrix2.__str__())
print("\n\r *******Суммированная матрица*******")

str(matrix1+matrix2)
