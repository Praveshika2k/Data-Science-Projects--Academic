import numpy as np
a1 = np.array([[4.3,3.1],[8.2,8.2],[3.2,0.9],[1.6,6.5]])
print("Shape of the matrix:", a1.shape)
a2 = np.delete(a1, 1, axis=0)
print(a2)
print("Shape of the matrix after deletion:", a2.shape)
a3 = np.sort(a1[:,1])
print("Sorted order of 2nd Column:", a3)
a1[:,1] = a3
print("Shape of the matrix after sorting 2nd column:\n",a1)