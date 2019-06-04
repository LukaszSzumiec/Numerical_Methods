import numpy as np
import math

def solve_CG(A, b, x0):
    r = np.matmul(A, x0)
    r = b - r
    p = r
    rsold = r.conj().transpose() #transponowanie macierzy
    rsold = np.matmul(rsold, r)
    x = x0

    for i in range (0, len(x0) + 1):
        # print("WYKONANIE NR {0}".format(i))
        Ap = np.matmul(A, p)
        beta = p.conj().transpose()
        beta = np.matmul(beta, Ap)
        alpha = rsold / beta
        alfa_p1 = alpha * p
        x = x + alfa_p1
        meh = alpha * Ap
        r = r - meh
        up1 = r.conj().transpose()
        up = np.matmul(up1, r)
        rsnew = up
        if math.sqrt(rsnew) < 1e-10:
            return x
        a = rsnew / rsold
        p = p * a
        p = p + r
        rsold = rsnew