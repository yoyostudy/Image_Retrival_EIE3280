from data3.data import image_list, image_tags
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import os
from datetime import datetime

##################################
######  global variable   ########
##################################
def sample_down(org_list, idx_list):
    return [org_list[i] for i in idx_list]



# idx_list = [19,42,89,76,43,36,34,73,901,24,82,50,61,28,12,58,30,49,98,9,17,18,68,95,84,29,88,0,57,25,92,67,5,
# 65,81,79,80,51,97,52,63,47,642,48,99,991,10,77,53,40,72,78,27,22,59,75,87,
# 31,8,35,85,62,26,13,33,37,56,70,96,44,4,66,83]
# idx_list = [19, 42, 89, 76, 43, 36, 34, 73, 901, 24, 82, 50, 61, 28, 12, 58, 30, 49, 98, 9,
# 17, 18, 68, 95, 84, 29, 88, 0, 57, 25, 92, 67, 5, 65, 81, 79, 80, 51, 97, 52, 63, 47, 64, 2, 48,
# 99, 991, 10, 77, 3, 11, 53, 40, 72, 78, 27, 22, 59, 75, 87, 31, 8, 35, 85, 62, 26, 13, 33, 37, 56, 70, 96, 44, 4, 66, 83, 14, 91, 409, 1]
# image_list = sample_down(image_list,idx_list)



color = ['blue','yellow','green',
         'red','pink','orange','purple',
         'white','black','gray']
N = len(color)
lower_color = ['lower_'+i for i in color]
upper_color = ['upper_'+i for i in color]
color_mask  = [i+'mask' for i in color]  
M = len(image_list) 
Mm = [['' for i in range(M)] for i in range(M)]

##################################
######  useful function   ########
##################################
#sort the dictionary by value  


def sort_by_value(dic):
    return sorted(dic.items(),reverse = True, key = lambda item: item[1])

#find the smallest k 
def KNN(lst,k=10):
    return sorted( list( zip(lst, list(range(len(lst)))) ) )[:k]

#find the top k
def reverseKNN(lst,k=10):
    return sorted( list( zip(lst, list(range(len(lst)))) ) ,reverse = True )[:k]

##################################
###### extract characters ########
##################################
# the first color moment
def moment1(v):
    return v.mean()

# RGB TO HSV
def HSV(idx):
    return cv2.cvtColor(image_list[idx],cv2.COLOR_BGR2HSV)

# HSV threshold
def set_threshold():
    threshold = [
        [ [70 ,30 ,46 ], [120, 255, 255] ],    # blue 
        [ [20 ,30 ,46 ], [33 , 255, 255] ],    # yellow
        [ [33 ,30 ,46 ], [70 , 255, 255] ],    # green 
        [ [173, 30, 46], [180, 255, 255] ],    # red
        [ [140,30 ,46 ], [173, 255, 255] ],    # pink
        [ [0  ,30 ,46 ], [20 , 255, 255] ],    # orange
        [ [120,30 ,46 ], [140, 255, 255] ],    # purple
        [ [0  ,0  ,240], [180, 50 , 255] ],    # white
        [ [0  ,0  ,0  ], [180, 50 , 70 ] ],    # black
        [ [0  ,0  ,60 ], [180, 50 , 240] ],    # gray
        ]
    lower_dic = {}
    upper_dic = {}
    for i in range(N):
        lower_dic[lower_color[i]] = np.array(threshold[i][0])
        upper_dic[upper_color[i]] = np.array(threshold[i][1])
    return lower_dic , upper_dic

# specified color mask
def mask(idx):
    hsv = HSV(idx)
    (lower_dic,upper_dic) = set_threshold()
    mask_dic = {}
    for i in range(N):
        mask_dic[color_mask[i]] = cv2.inRange(hsv,lower_dic[lower_color[i]],upper_dic[upper_color[i]])    
    return mask_dic

# find major color
def major_color(idx):
    m1 = {}
    for i in range(N):
        M = mask(idx)[color_mask[i]]
        m1[color[i]] = moment1(M.ravel())
    if sort_by_value(m1)[0][1] > 0.3 * 255:
        if sort_by_value(m1)[1][1] > 0.1 * 255:
            return 'mixture,'+sort_by_value(m1)[0][0]+','+sort_by_value(m1)[1][0]
        else:
            return sort_by_value(m1)[0][0]
    else :
        return 'mixture,'+sort_by_value(m1)[0][0]+','+sort_by_value(m1)[1][0] + ','+sort_by_value(m1)[2][0]

def color_classification():
    ccfy_l = {}
    for key in color: ccfy_l[key] = []
    for i in range(M):
        mc = major_color(i)
        mixture_color_list = mc.replace('mixture,','').split(',')
        for c in mixture_color_list:

                #ccfy_l[c].append(idx_list[i])
                ccfy_l[c].append(i) 
    return ccfy_l

def color_moment(color,idx):
    v = mask(idx)[color].ravel()
    m1 = v.mean()  ## first moment
    m2 = v.std()   ## second moment
    l = ( np.array([(i-m1)**3 for i in v]) ).mean()
    m3 = (l)**(1/3)
    return m1,m2,m3 

def similarity_moment(color,idx):
    for i in range(M):
        mt = color_moment(color,i) ## the color moment of the target
        mv = color_moment(color,i)   ## the color moment of the variable
        Mm[idx][i]=(1/2)*abs(mt[0]-mv[0])+(1/4)*abs(mt[1]-mv[1])+(1/4)*abs(mt[1]-mv[1])   
    print([x[1] for x in KNN(Mm[idx])])

##################################
######    main function   ########
##################################

if __name__ == "__main__":
    start_time = datetime.now()
    print(major_color(1))

    o = color_classification()['orange']
    w = color_classification()['white']
    l = []
    # print(w)
    # print(o)
    for i in o:
        if i in w:
            l.append(i)
    print(l)


    end_time = datetime.now()

    print('',end_time-start_time)





