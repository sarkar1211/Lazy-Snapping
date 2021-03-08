import numpy as np
import cv2
import scipy.sparse
from scipy.sparse.linalg import spsolve

from os import path


def laplacian_matrix(n, m):

    mat_D = scipy.sparse.lil_matrix((m, m))
    mat_D.setdiag(-1, -1)
    mat_D.setdiag(4)
    mat_D.setdiag(-1, 1)

    mat_A = scipy.sparse.block_diag([mat_D] * n).tolil()

    mat_A.setdiag(-1, 1 * m)
    mat_A.setdiag(-1, -1 * m)

    return mat_A


def edit_poisson(source, target, mask, offset):

    y_max, x_max = target.shape[:-1]
    y_min, x_min = 0, 0

    x_range = x_max - x_min
    y_range = y_max - y_min

    M = np.float32([[1, 0, offset[0]], [0, 1, offset[1]]])
    source = cv2.warpAffine(source, M, (x_range, y_range))

    mask = mask[y_min:y_max, x_min:x_max]
    mask[mask != 0] = 1


    matA = laplacian_matrix(y_range, x_range)

    laplacian = matA.tocsc()


    for y in range(1, y_range - 1):
        for x in range(1, x_range - 1):
            if mask[y, x] == 0:
                k = x + y * x_range
                matA[k, k] = 1
                matA[k, k + 1] = 0
                matA[k, k - 1] = 0
                matA[k, k + x_range] = 0
                matA[k, k - x_range] = 0

    matA = matA.tocsc()

    mask_flat = mask.flatten()
    for channel in range(source.shape[2]):
        source_flat = source[y_min:y_max, x_min:x_max, channel].flatten()
        target_flat = target[y_min:y_max, x_min:x_max, channel].flatten()

        alpha = 1
        mat_b = laplacian.dot(source_flat) * alpha


        mat_b[mask_flat == 0] = target_flat[mask_flat == 0]

        x = spsolve(matA, mat_b)

        x = x.reshape((y_range, x_range))

        x[x > 255] = 255
        x[x < 0] = 0
        x = x.astype('uint8')


        target[y_min:y_max, x_min:x_max, channel] = x

    return target