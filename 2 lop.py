import numpy as np
import pandas as pd

s = 2
m = 8

data = pd.read_csv("du_lieu_tao.csv")
p = np.array([data["can nang"], data["do chin"]]).T
t = np.array([data["t1"], data["t2"]]).T

a = np.array([[0, 0]])
w = np.array([[1, 0], [2, 8]])
b = np.array([[-6, -9]])
k = 0
while True:
    d = True
    k += 1
    print("Lần lặp thứ", k)
    for i in range(m):
        x = np.array([p[i]])
        n = w.dot(x.T) + b.T
        for j in range(s):
            a[0][j] = 1 if n[j][0] >= 0 else 0
        if np.array_equal([t[i]], a) == False:
            e = t[i] - a
            w += e.T.dot(x)
            b += e
            d = False
    print("w =\n", w)
    print("b =\n", b)
    if d == True: break

f = np.array([[9, 2]])
n = w.dot(f.T) + b.T
for j in range(s):
    a[0][j] = 1 if n[j][0] >= 0 else 0

print("Lớp của f là:", a)