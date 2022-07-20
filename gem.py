#!/usr/bin/env python3
import numpy as np
import random
import time

N = 256

class Matrix(object):
    def num_matrix(self):
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

    def py_matrix_first(self):
        for self.i in range(0, N):
            self.matrix1.append([random.randint(0, 1) for _ in range(N)])

    def cr_mt1(self):
        for i in range(0, N):
            for j in range(0, N):
                print(self.matrix1[i][j], end=' ')
            print()

    def py_matrix_second(self):
        for self.i in range(0, N):
            self.matrix2.append([random.randint(0,1) for _ in range(N)])

    def cr_mt2(self): 
        for i in range(0, N):
            for j in range(0, N):
                print(self.matrix2[i][j], end =' ')
            print()

if __name__ == "__main__":
    flop = N*N*2*N

    st = time.time()
    m = Matrix()
    m.matrix()
    t1 = time.time() - st
    print(f"{flop/t1 * 1e-9:.2f} GFLOP/S")
    
    st = time.monotonic()
    p = PMatrix()
    p.py_matrix_first()
    p.py_matrix_second()
    et = time.monotonic()
    t = et - st
    print(f"{flop/t * 1e-9:.2f} GFLOP/S")
    
    #p.cr_mt1()
    #p.py_matrix_first()
    #print()
    #p.py_matrix_second()