import numpy as np


def kmeanalgo(k, arr_im):
     centroids = centroids_generate(k ,arr_im)
     cent1 = np.empty_like(centroids )
     itr =0
     while not np.array_equal(cent1, centroids) :
          if itr <=200:
               itr+=1
               cent1 = centroids
               index = getting_index(arr_im , centroids)
               centroids = centroid_update(arr_im ,index , k)
          else:
               cent1 = centroids
     print('total_number_of_iterations:')
     print(itr)
     return centroids , index


def centroids_generate(k,arrc) :
    hi=0
    centroid =[]
    while hi < (k * 3):
        r = np.random.randint(np.amin(np.amin(arrc)),np.amax(np.amax(arrc)))
        if r not in centroid:
            hi += 1
            centroid = np.append(centroid,r)
    c = centroid.reshape(k,3)
    return c


def getting_index(arri, cent):
    imdx =[]
    for w in range(len(arri)):
        dis = []
        for i in range(len(cent)):
            d = arri[w] - cent[i]
            dd = (np.linalg.norm(d))
            dis = np.append(dis,dd)
        imdx = np.append(imdx, np.argmin(dis))
    return imdx


def centroid_update(arr, ind, k):
    average =[]
    for i in range(k):
        hh =[]
        m=0
        for j in range(len(arr)):
            if ind[j]== i :
                hh=np.append(hh , arr[j])
                m+=1
        if len(hh)!= 0:
            hh=hh.reshape(m, 3)
            average=np.append(average,(sum(hh)/len(hh)))
        else:
            average=np.append(average , arr[i])
    average=average.reshape(k, 3)
    return average