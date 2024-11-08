import pandas as pd
import numpy as np

data = pd.read_csv("knn2.csv")
p = np.array([data["chay"], data["sut"]]).T
t = np.array([data["loai"]]).T
test = np.array([[1, 7]])
w = np.array([[-1, 0]])
b = -4

a = 0
k = 0
m = len(p)
while True:
    d = True
    k += 1
    print("Lần lặp thứ", k)
    for i in range(m):
        x = np.array([p[i]])
        n = w.dot(x.T) + b
        a = 0 if n < 0 else 1
        if a != t[i]:
            e = t[i] - a
            w += np.dot(e, x)
            b += e
            d = False
    print("w = ", w)
    print("b = ", b)
    if d == True: break

n = w.dot(test.T) + b
wr = "Sản phẩm đạt yêu cầu" if n < 0 else "Sản phẩm không đạt yêu cầu"
print("Sản phẩm test:", wr)