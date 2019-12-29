"""
This file shows the compiled result of sigma_test.hy
"""
import numpy as np


def matmul(a, b):
    c = np.zeros([b.shape[1], a.shape[0]])
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(b.shape[1]):
                c[i, k] += a[i, j] * b[j, k]
    return c


def ntn(x, y, w, wb, bias):
    s1 = np.zeros([w.shape[2]])
    for i in range(x.shape[0]):
        for j in range(y.shape[0]):
            for k in range(w.shape[2]):
                s1[k] += x[i] * y[j] * w[i, j, k]
    xy = np.concatenate([x, y])
    s2 = np.zeros([wb.shape[0]])
    for k in range(wb.shape[0]):
        for i in range(wb.shape[1]):
            s2[k] += wb[k, i] * xy[i]
    return s1 + s2 + bias
