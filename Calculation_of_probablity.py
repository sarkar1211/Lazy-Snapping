from Weight_Calculation import weight
import numpy as np
import math

def calc_probability(image,forecent,foredpincent,backcent,backdpincent):
    imag1 = image
    im1=np.array(imag1)
    print(im1.shape)
    fww=weight(forecent,foredpincent)
    bww=weight(backcent,backdpincent)
    back=np.zeros([len(im1),len(im1[0]),3])
    p1=np.zeros([1,3])
    for i in range (0,len(im1)):
        for j in range(0,len(im1[0])):
            p1[0][0] = im1[i][j][0]
            p1[0][1] = im1[i][j][1]
            p1[0][2] = im1[i][j][2]
            adding=0
            for k in range (0,len(forecent)) :
                wk= fww[k]
                norm1=(np.linalg.norm(p1 - forecent[k]))
                expo=math.exp(-(norm1))
                adding=adding+(wk* expo )
            foreground=adding
            adding1=0
            for m in range(0, len(backcent)):
                wk1= bww[m]
                norm2=(np.linalg.norm(p1 - backcent[m]))
                expo2=math.exp(-(norm2))
                adding1= adding1 + (wk1* expo2)
            background=adding1
            if foreground > background:
                back[i][j] = [255 , 255 , 255]
            else:
                back[i][j] = [0 ,0 ,0]
    return back