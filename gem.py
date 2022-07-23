#!/usr/bin/env python3
import numpy as np
import random
import time

N = 64

class Matrix(object):
    def mul_matrix(self):
        self.A = np.random.randn(N, N).astype(np.float32)
        self.B = np.random.randn(N, N).astype(np.float32)
        self.C = self.A @ self.B
        return self.C

    def matrix(self):
        self.mat1 = np.random.randint(2, size=(N, N)).astype(np.int32)
        self.mat2 = np.random.randint(2, size=(N, N)).astype(np.int32)
        return self.mat1, self.mat2

class PMatrix(object):
    def __init__(self):
        self.matrix1 = []
        self.matrix2 = []
        self.matrix3 = [0] * N

    def py_matrix_first(self):
        for self.i in range(0, N):
            self.matrix1.append([random.random() for _ in range(N)])

    #def cr_mt1(self):
    #    for i in range(0, N):
    #        for j in range(0, N):
    #            print(self.matrix1[i][j], end=' ')
    #        print()

    def show_matrix_first(self):
        for i in range(0, N):
            print(self.matrix1[i])

    def py_matrix_second(self):
        for self.i in range(0, N):
            self.matrix2.append([random.random() for _ in range(N)])

    #def cr_mt2(self): 
    #    for i in range(0, N):
    #        for j in range(0, N):
    #            print(self.matrix2[i][j], end =' ')
    #        print()

    def show_matrix_second(self):
        for i in range(0, N):
            print(self.matrix2[i])

    def multiply_matrtix(self):
        for i in range(N):
            self.matrix3[i] = [0] * N

        for x in range(N):
            for y in range(N):
                for k in range(N):
                    self.matrix3[x][y] += self.matrix1[x][k] * self.matrix2[k][y]
        
        #for r in self.matrix3:
        #    print(r)
                

if __name__ == "__main__":
    flop = N*N*2*N

    #for i in range(100):
    #    st = time.time()
    #    m = Matrix()
    #    m.mul_matrix()
    #    t1 = time.time() - st
    #    print(f"{flop/t1 * 1e-9:.2f} GFLOP/S")

    for i in range(100):
        st = time.monotonic()
        p = PMatrix()
        p.py_matrix_first()
        p.py_matrix_second()
        p.multiply_matrtix()
        et = time.monotonic()
        t = et - st
        print(f"{flop/t * 1e-9:.7f} GFLOP/S")