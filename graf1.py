'''Graf1. Дано описание неориентированного графа в текстовом файле с именем FileName. в
виде матрицы смежности. Первая строка файла содержит количество вершин графа (n), а
следующие n строк содержат матрицу смежности (m), m[i][j]=0, если ребра между
вершинами i и j не существует. Определить степень для каждой вершины графа. Вывести
степени вершин, перечисляя их в порядке возрастания номеров вершин. Если в графе
имеются петли, то каждая петля в степени вершины учитывается дважды.'''

with open('FileName1.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0].strip())
matrix = []
idx = 1
for i in range(n):
    row = list(map(int, lines[idx].strip().split()))
    matrix.append(row)
    idx += 1

degrees = []
for i in range(n):
    deg = 0
    for j in range(n):
        if i == j:
            deg += 2 * matrix[i][j]
        else:
            deg += matrix[i][j]
    degrees.append(deg)

print(' '.join(map(str, degrees)))