
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

def mydisplay(bw, image):

    im = np.array(image.copy())
    im1 = np.array(image.copy())
    for i in range(len(bw)):
        for j in range(len(bw[0])):
            if bw[i][j][0] == 0:
                im[i][j] = [0,0,0]
    for i in range(len(bw)):
        for j in range(len(bw[0])):
            if bw[i][j][0] != 0:
                im1[i][j] = [0,0,0]
    dst = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    dst1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)

    plt.imshow(image)
    plt.show()

    plt.imshow(Image.fromarray(im))
    plt.show()

    plt.imshow(Image.fromarray(im1))
    plt.show()

    return dst, dst1