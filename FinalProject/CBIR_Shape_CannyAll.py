from data.data import image_list
from matplotlib import pyplot as plt
from cv2 import cv2
import numpy as np
import matplotlib
import os
import math

##similarity calculation
def Cos_Sim (Vector1 , Vector2):
    num = 0
    numerator = 0 
    denominator1 = 0 
    denominator2 = 0
    while num < min(len(Vector1),len(Vector2)):
        numerator += Vector1[num] * Vector2[num]
        denominator1 += Vector1[num] * Vector1[num]
        denominator2 += Vector2[num] * Vector2[num]
        num += 1
    #print(numerator,denominator1,denominator2)
    denominator = (denominator1**(1/2)) * (denominator2**(1/2)) 
    #print(denominator)
    if denominator == 0 : Similarity_V1_V2 = 0
    else: Similarity_V1_V2 = numerator/denominator
    return Similarity_V1_V2

##convert the image to vector
def set_list(list):
    new_list = []
    for i in list:
        for k in i:
            if k == 255: new_list.append(1)
            else: new_list.append(0)
    return new_list


##canny examination
def Canny(p):   
    #image_list[p] = cv2.cvtColor(image_list[p],cv2.COLOR_BGR2GRAY) 
    img_canny = cv2.Canny(image_list[p],100,200) #threshold
    return set_list(img_canny)

def sim_2pic(k,i):
    return Cos_Sim(Canny(k),Canny(i))
#color_list=[49,56,91,81,89,95,2,4,47,63,36,62,10,77,53,72] #after texture test
##similarity in reduced order
similarity = {}
for q in range(0,1000):
#for q in color_list:
    similarity[q] = sim_2pic(1,q)
    sortedsim = sorted(similarity.items(), key = lambda item: item[1])
print(sortedsim)













