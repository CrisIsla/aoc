import sys

input = open(sys.argv[1]).read().rstrip()
lines = input.split("\n")


def getSurroundings(i, j, matrix):
    x = len(matrix[0])
    y = len(matrix)
    result = 0
    around = [-1, 0, 1]
    for k in [z for z in around if i + z >= 0 and i + z < x]:
        for l in [x for x in around if j + x >= 0 and j + x <y]:
            result += matrix[i + k][j + l]
    return result - 1


result = 0
matrix = []
for line in lines:
    row = []
    for cell in line:
        row.append(1) if cell == "@" else row.append(0)
    matrix.append(row)

row_len = len(matrix)
col_len = len(matrix[0])

while True:
    changes = []
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 1:
                surr = getSurroundings(i, j, matrix)
                if surr < 4:
                    matrix[i][j] = 0
                    changes.append((i, j))
                    result += 1
    if not changes: 
        break
    else:
        for i, j in changes:
            matrix[i][j] = 0

print(result)
