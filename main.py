import numpy as np
import hy
import sigma_test as st


def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([[1, 4],
                  [7, 2],
                  [5, 8]])
    print(st.matmul(a, b))

    x = np.array([1, 1, 2, 3])
    y = np.array([5, 8, 13, 21])
    w = np.ones((4, 4, 3))
    wb = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 2, 3, 4, 5, 6, 7, 8]])
    bias = [0, 2, 4]
    print(st.ntn(x, y, w, wb, bias))


if __name__ == '__main__':
    main()
