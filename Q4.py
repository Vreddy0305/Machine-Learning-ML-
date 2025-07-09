def matrixtranspose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose =[[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transpose[j][i]= matrix[i][j]
    return transpose
rows = int(input("Enter number of rows"))
cols = int(input("Enter number of columns"))
matrix = [list(map(int,input(f"Enter row {i+1}: ").split())) for i in range(rows)]
transpose = matrixtranspose(matrix)
print(f"Transpose: {transpose}")
