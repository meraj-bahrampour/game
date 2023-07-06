def Baztabi(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
    return matrix


def Motegharen(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j or i + j == len(matrix) - 1:
                matrix[i][j] = 1
    return matrix


def Moteadi(matrix):
    dist = list(map(lambda i: list(map(lambda j: j, i)), matrix))
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n = int(input("n : "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter [{i}][{j}] : "))
        row.append(element)
    matrix.append(row)

print("بستار بازتابی : ")
print(Baztabi(matrix))
print("بستار متقارن : ")
print(Motegharen(matrix))
print("بستار متعدی : ")
print(Moteadi(matrix))
