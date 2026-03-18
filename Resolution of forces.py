import numpy as np

A = 30
B = 34

m = 295
g = 9.81
F1 = m * g / ( (np.sin(A)) + ((np.cos(A))/(np.cos(B)) * (np.sin(B))))
F2 = F1 * ((np.cos(A)) / (np.cos(B)))

print(F1)