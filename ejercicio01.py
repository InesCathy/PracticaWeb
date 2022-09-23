import numpy as np
def fibonacci():
    print("Ingrese un valor para n")
    n =int(input())
    a = np.array([[1, 1], [1, 0]])
    potencia=np.linalg.matrix_power(a, (n-1))
    print(potencia)

fibonacci()
