import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1

    for k in range(n):
        U[k, k:] = A[k, k:]
        L[k+1:, k] = A[k+1:, k] / U[k, k]
        for j in range(k+1, n):
            U[j, k:] -= L[j, k] * U[k, k:]

    return L, U

def solve_lu(A, b):
    L, U = lu_decomposition(A)
    n = len(A)
    y = np.zeros(n)
    x = np.zeros(n)

    # Forward substitution (Ly = b)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    # Backward substitution (Ux = y)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x

# Contoh
A = np.array([[1, 1, -1],
              [2, 2, 1],
              [-1, 1, 1]])
b = np.array([1, 5, 1])

x = solve_lu(A, b)
print("Solusi x:", x)