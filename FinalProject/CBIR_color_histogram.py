from data3.data import image_list, image_tags
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import os
from datetime import datetime

M = len(image_list)    ## similarity matrix size
Mb = [['' for i in range(M)] for i in range(M)]      ##bhttacharyya similarity matrix
IMco = [['' for i in range(M)]for i in range(M)]    ##correlation similarity matrix  the inverse as correlation coefficience is FANBI 
Mch = [['' for i in range(M)] for i in range(M)]     ##chisquare similarity matrix
Mm = [['' for i in range(M)] for i in range(M)]
##################################

#find the smallest k 
def KNN(lst,k=8):
    return sorted( list( zip(lst, list(range(len(lst)))) ) )[:k]
#find the top k
def abs_rKNN(lst,k=8):
    return sorted( list( zip(lst, list(range(len(lst)))) ) ,reverse = True )[:k]

#RGB hiatogram 
def hist(idx,channel):
    return cv2.calcHist([image_list[idx]],channel,None,[256],[0,256]) ##RGB SPACE

#compare hist RGB 
def compare_hist(idx1,idx2,channel):
    mb = cv2.compareHist(hist(idx1,channel), hist(idx2,channel), cv2.HISTCMP_BHATTACHARYYA)
    imco = cv2.compareHist(hist(idx1,channel), hist(idx2,channel),cv2.HISTCMP_CORREL)
    mch = cv2.compareHist(hist(idx1,channel), hist(idx2,channel),cv2.HISTCMP_CHISQR)
    return mb,imco,mch   

def similarity_hist(idx,channel):
    for i in range(M):
        # print('the distance between %s and %s is'%(idx,i))
        (mb,imco,mch) = compare_hist(idx,i,channel)
        Mb[idx][i] = mb
        IMco[idx][i]=imco
        Mch[idx][i]=mch
    print('Bhattacharyya：%s,\n%s,\ncorrelation：%s，\n%s \nchisquare:%s,\n%s' %(
           KNN(Mb[idx]),   [x[1] for x in KNN(Mb[idx])],
           abs_rKNN(IMco[idx]), [x[1] for x in abs_rKNN(IMco[idx])],
           KNN(Mch[idx]),  [x[1] for x in KNN(Mch[idx])]))

start = datetime.now()
similarity_hist(3,[1])
end = datetime.now()
print('time consume',end-start)