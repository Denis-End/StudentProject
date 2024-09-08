def get_matrix(n, m, value):
    matrix = []
    for y in range(n):
        l = []
        # n - ЭТО КОЛИЧЕСТВО СПИСКОВ ВНУТРИ СПИСКА МАТРИЦЫ"
        matrix.append(l)
        for j in range(m):
            # m - КОЛИЧЕСТВО ПОВТОРЕНИЙ ВНУТРИ СПИСКА
            l.append(value)
    return matrix
            # value ЗНАЧЕНИЕ В СПИСКЕ КОТОРЫЙ ВЛОЖЕН В МАТРИЦУ


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)



