import numpy as np
from scipy.linalg import norm
import math

def solve_chebyshev(A, b, x0, iter_num, l_max, l_min):
    d = (l_max + l_min) / 2
    c = (l_max - l_min) / 2
    preCond = np.identity(2)
    x = x0
    r = np.matmul(A, x)
    r = b - r

    for i in range(1, iter_num + 1):
        # print("Iteracja nr {0}".format(i))
        z = np.linalg.solve(A, r)
        alpha = 1
        if i == 1:
            p = z
            alpha = 1 / d
        elif (i == 2):
            beta = (1 / 2) * (c * alpha) ** 2
            alpha = 1 / (d - beta / alpha)
            p = z + beta * p
        else:
            beta = (c * alpha / 2) ** 2
            alpha = 1 / (d - beta / alpha)
            p = z + beta * p
        x = x + alpha * p
        r = np.matmul(A, x)
        r = b - r
        print(x)
        print(norm(r))
        if norm(r) < 1e-10:
            return x


