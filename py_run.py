#!/usr/bin/env python3
import random

class PY_Matrix(object):
    def __init__(self, N):
        self.matrix_a = []
        self.matrix_b = []
        self.matrix_c = [0] * N

    def py_matrix_create(self, N):
        for self.i in range(0, N):
            self.matrix_a.append([random.random() for _ in range(N)])
            
        for self.i in range(0, N):
            self.matrix_b.append([random.random() for _ in range(N)])

        for i in range(0, N):
            self.matrix_c[i] = [0] * N

    def py_matrix_multiply(self, N):
        for x in range(0, N):
            for y in range(0, N):
                for k in range(0, N):
                    self.matrix_c[x][y] += self.matrix_a[x][k] * self.matrix_b[k][y]

#pm = PY_Matrix(3)
#pm.py_matrix_create(3)
#pm.py_matrix_multiply(3)