import numpy as np
from numpy import matlib

if __name__ == '__main__':
    def main():
        matrix_in1 = np.matrix(
            [
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.],
                [1.,  2., 3.,  4.,  5.,  6.]

            ]
        )

        vector_in2 = np.transpose(
                np.matrix(
                    [11., 12., 13., 14., 15., 16., 17., 18., 19., 20.]
                ))


        [row, col] = np.shape(matrix_in1)
        [vrow, vcol] = np.shape(vector_in2)

        print(np.shape(vector_in2))

        output = matlib.zeros((row, col), dtype=float)

        for j in range(col):
            for i in range(row):
                output[i, j] = matrix_in1[i, j] + vector_in2[i]

        print(matrix_in1)
        print(vector_in2)
        print(output)
    main()
