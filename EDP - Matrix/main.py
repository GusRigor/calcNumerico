import numpy as np
# linha , coluna
z = 18 * 18
print (z)
a = np.zeros((21,22), dtype=np.float64)
b = np.zeros((21,1), dtype=np.float64)

i = 0
j = 0

for i in range(21):
    for j in range(20):
        if i == 0:
            a[i][j] = 0








print(a)

b[1][0] = 12
print(b)

a[0][21] = b[0][0]
a[1][21] = b[1][0]

print(a)
