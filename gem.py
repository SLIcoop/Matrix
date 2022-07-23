#!/usr/bin/env python3
from num_run import Num_Matrix
from py_run import PY_Matrix
import time

N1 = 512
N2 = 64

if __name__ == "__main__":
    flop_num = N1*N1*2*N1
    flop_py = N2*N2*2*N2

    for period in range(1000):
        st1 = time.monotonic()
        nm = Num_Matrix()
        nm.multiply_matrix(N1)
        et1 = time.monotonic()
        t1 = et1 - st1
        #print(nm.multiply_matrix(N))

        st2 = time.time()
        pr = PY_Matrix(N2)
        pr.py_matrix_create(N2)
        pr.py_matrix_multiply(N2)
        t2 = time.time() - st2

        if period % 100 == 99:
            print('--- Period %d' % (period + 1))
            print(f'Numpy Matrix: {flop_num/t1 * 1e-9:.3f} GFLOP/S')
            print(f'Python Matrix: {flop_py/t2 * 1e-9:.7f} GFLOP/S')

    #pr = PY_Matrix(N)
    #pr.py_matrix_create(N)
    #pr.py_matrix_multiply(N)

