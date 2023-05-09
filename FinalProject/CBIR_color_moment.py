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
######  useful function   ########
##################################

#find the smallest k 
def KNN(lst,k=9):
    return sorted( list( zip(lst, list(range(len(lst)))) ) )[:k]
#find the top k
def reverseKNN(lst,k=10):
    return sorted( list( zip(lst, list(range(len(lst)))) ) ,reverse = True )[:k]
#sort dictionary in the order of key
def sort_by_value(d): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort() 
    return [ backitems[i][1] for i in range(0,len(backitems))]   
#decrease the image_list
def sample_down(org_list, idx_list):
    return [org_list[i] for i in idx_list]

##################################
###### extract characters ########
##################################

#RGB hiatogram 
def hist(idx,channel):
    return cv2.calcHist([image_list[idx]],channel,None,[256],[0,256]) ##RGB SPACE

#color moment    
def color_moment(idx,channel):
    v = hist(idx,channel).ravel()
    m1 = v.mean()  ## first moment
    m2 = v.std()   ## second moment
    m3 = (np.mean([i-m1 for i in v]))**(1/3)  ## third moment 
    return m1,m2,m3 

##################################
###### compute similarity ########
##################################
#compare color moments
def similarity_moment(idx,channel):
    for i in range(M):
        # print('between %s and %s >>>>'%(idx,i))
        mt = color_moment(idx,channel) ## the color moment of the target
        mv = color_moment(i,channel)   ## the color moment of the variable
        Mm[idx][i]=(1/2)*abs(mt[0]-mv[0])+(1/4)*abs(mt[1]-mv[1])+(1/4)*abs(mt[1]-mv[1])   
    print([x[1] for x in KNN(Mm[idx])])




start = datetime.now()
similarity_moment(1,[0])
end = datetime.now()
print('time consume',end-start)




