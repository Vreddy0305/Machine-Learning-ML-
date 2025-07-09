def xmatrix(A, B):
    rA = len(A)
    cA = len(A[0])
    rB = len(B)
    cB = len(B[0])
    if cA != rB:
        return "Matrices are not multiplicable since number of columns in the first matrix is not equal to the number of rows from the second matrix"
    result = [[0 for _ in range(cB)] for _ in range(rA)]    
    for i in range(rA):
        for j in range(cB):
            for k in range(cA):
                result[i][j] += A[i][k] * B[k][j]
    return result
rows_A = int(input("Enter number of rows for matrixA"))
cols_A = int(input("Enter number of columns for matrix A"))
A = [list(map(int, input(f"Enter row {i+1} for matrix A").split())) for i in range(rows_A)]
rows_B = int(input("Enter number of rows for matrix B"))
cols_B = int(input("Enter number of columns for matrixB "))
B = [list(map(int, input(f"Enter row {i+1} for matrix B").split())) for i in range(rows_B)]
product = xmatrix(A, B)
print(f"FINAL ANSWER: {product}")
