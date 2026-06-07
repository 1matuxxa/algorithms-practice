'''Graf10. Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName1. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=15, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить все
маршруты перелета из города К1 в город К2 В файл с именем FileName2 в первой строке
выведите число таких маршрутов, а в следующих строках перечислите все такие
маршруты в порядке от самых коротких к более длинным, маршруты одинаковой длины
перечисляйте в лексикографическом порядке. Маршрут задается перечислением номеров
городов, нумерация городов идет с 1. Если таких маршрутов нет, вывод числа -1'''

with open('FileName1_10.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0].strip())
matrix = []
idx = 1
for i in range(n):
    row = list(map(int, lines[idx].strip().split()))
    matrix.append(row)
    idx += 1

k1, k2 = map(int, lines[idx].strip().split())
start = k1 - 1
end = k2 - 1

paths = []

def dfs(curr, target, path, visited):
    path.append(curr + 1)
    if curr == target:
        paths.append(path[:])
    else:
        for neigh in range(n):
            if matrix[curr][neigh] == 1 and neigh not in visited:
                visited.add(neigh)
                dfs(neigh, target, path, visited)
                visited.remove(neigh)
    path.pop()

visited = set([start])
path = []
dfs(start, end, path, visited)

paths.sort

with open('FileName2_10.txt', 'w') as f:
    if not paths:
        f.write('-1\n')
    else:
        f.write(str(len(paths)) + '\n')
        for p in paths:
            f.write(' '.join(map(str, p)) + '\n')