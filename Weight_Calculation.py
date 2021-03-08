import numpy as np

def weight(cent, index):
    tsp = len(index)
    k = len(cent)
    num = []
    for i in range(k):
        l = 0
        for j in range(tsp):
            if index[j] == i:
                l += 1
        num = np.append(num, l)
    weight = num/tsp
    return weight