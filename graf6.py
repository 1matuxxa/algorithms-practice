'''Graf6. Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=25, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить номера
городов, в которые из города K можно долететь ровно с L пересадками для самого
короткого пути. Перечислите номера таких городов в порядке возрастания. Нумерация
городов начинается с 1. Если таких городов нет, выведите число (-1).'''

with open('FileName6.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0].strip())
matrix = []
idx = 1
for i in range(n):
    row = list(map(int, lines[idx].strip().split()))
    matrix.append(row)
    idx += 1

k, l = map(int, lines[idx].strip().split())
start = k - 1

dist = [-1] * n
dist[start] = 0

q = [start]
while q:
    u = q.pop(0)
    for v in range(n):
        if matrix[u][v] == 1 and dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

result = [i+1 for i in range(n) if dist[i] == l + 1]
result.sort()

if not result:
    print(-1)
else:
    print(' '.join(map(str, result)))