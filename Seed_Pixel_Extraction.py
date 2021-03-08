import numpy as np

def extract_seed_pixels(str_img, img):
    arr_str = np.array(str_img)
    arr_img = np.array(img)
    # blue = np.array([6, 0, 255])
    red = np.array([255, 0, 0])
    blue = np.array([0, 0, 255])

    p = 0
    q = 0
    K = []
    L = []
    for i in range(len(arr_str)):
        for j in range(len(arr_str[0])):
            if (arr_str[i][j][0] == blue[0] and arr_str[i][j][1] == blue[1] and arr_str[i][j][2] == blue[2]):
                K = np.append(K, [[arr_img[i][j][0], arr_img[i][j][1], arr_img[i][j][2]]])
                p = p+1
            elif (arr_str[i][j][0] == red[0] and arr_str[i][j][1] == red[1] and arr_str[i][j][2] == red[2]):
                L = np.append(L, [[arr_img[i][j][0], arr_img[i][j][1], arr_img[i][j][2]]])
                q = q+1

    b_g = K.reshape(p, 3)
    f_g = L.reshape(q, 3)

    return f_g, b_g