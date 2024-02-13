import numpy as np

n = int(input())  # ROWS строки!
m = int(input())  # COLS СТОЛБЦЫ!


def do_matrix_by_compression(chars='C', rows=6, cols=4):

    matrix = [[chars for _ in range(cols)] for _ in range(rows)]

    for row in matrix:
        print(*row)


def do_matrix_by_cycles(chars='C', rows=6, cols=4):

    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(chars)
        matrix.append(row)

    for r in matrix:
        print(*r)


# MATRIX 0 var numbers per strings
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
# MATRIX 1 var!
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)
# PRINT 1 var на ПЕЧАТЬ!!!
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# MATRIX FULL Заполненная строками матрица!
matrix = [[input() for _ in range(m)] for _ in range(n)]
# PRINT вывод на печать заполненной строками матрицы!
for row in matrix:
    print(*row)

# MATRIX построчная с шаблоном для операций над элементами матрицы:
n = int(input())
m = int(input())

matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix[i][j])

# Умножение матрицЖ
a = np.array(matrix)
b = np.array(matrix)
res = a.dot(b)
print(res)