import numpy as np

def crout(A):

    L = np.zeros((3, 3))
    U = np.zeros((3, 3))

    for k in range(0, 3):
        U[k, k] = 1 

        for j in range(k, 3):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, j)]) #range from index 0
            L[j, k] = A[j, k] - sum0 #reversed index

        for j in range(k+1, 3):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)]) #range from index 0
            U[k, j] = (A[k, j] - sum1) / L[k, k]



    print(L)
    print()
    print(U)
    return L, U
# contoh
A = np.array([[1, 3, 1], [1, 5, 5], [2, 7, 5]])
crout(A)