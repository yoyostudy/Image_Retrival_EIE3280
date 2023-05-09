#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:31:54 2019

@author: mac
"""
#from data.data import image_list
from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

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

##LBP extraction
def LBP(p):   
    radius = 1
    n_points = 8*radius
    image = cv2.cvtColor(image_list[p],cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    lbp = local_binary_pattern(image,n_points,radius)
    #image_list[p] = cv2.cvtColor(image_list[p],cv2.COLOR_BGR2GRAY) 
    return set_list(lbp)

def sim_2pic(k,i):
    return Cos_Sim(LBP(k),LBP(i))

#color_list=[89, 43, 36, 901, 82, 58, 49, 68, 95, 0, 57, 25, 92, 81, 79, 97, 63, 47, 2, 10, 77, 11, 53, 72, 78, 59, 87, 62, 56, 96, 4, 66, 91, 1]
##similarity in reduced order
similarity = {}
for q in range(0,1000):
#for q in color_list:
    similarity[q] = sim_2pic(1,q)
    sortedsim = sorted(similarity.items(), key = lambda item: item[1])
print(sortedsim)
