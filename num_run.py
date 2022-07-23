#!/usr/bin/env python3
import numpy as np

class Num_Matrix(object):
    def multiply_matrix(self, N):
        self.matrix_a = np.random.randn(N, N).astype(np.float32)
        self.matrix_b = np.random.randn(N, N).astype(np.float32)
        return self.matrix_a @ self.matrix_b

#nm = Num_Matrix()
#print(nm.multiply_matrix(128))