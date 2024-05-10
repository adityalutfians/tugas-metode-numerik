import numpy as np

# Matriks koefisien
A = np.array([[1, -1, 2],
              [3, 0, 1],
              [1, 0, 2]])

# Vektor hasil
B = np.array([5, 10, 5])

# Mencari matriks balikan dari A
A_inv = np.linalg.inv(A)

# Mencari solusi
X = np.dot(A_inv, B)

print("Solusi:")
print("x1 =", X[0])
print("x2 =", X[1])
print("x3 =", X[2])