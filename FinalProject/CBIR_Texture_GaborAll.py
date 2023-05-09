#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:51:40 2019

@author: mac
"""
#from data.data import image_list
from skimage import data,filters,color,io
from skimage.transform import rotate
from skimage.feature import local_binary_pattern
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

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
    denominator = (denominator1**(1/2)) * (denominator2**(1/2)) 
    if denominator == 0 : Similarity_V1_V2 = 0
    else: Similarity_V1_V2 = numerator/denominator
    return Similarity_V1_V2

##convert the image to vector
def set_list(list):
    new_list = []
    for i in list:
        for k in i:
            new_list.append(k)
    return new_list

##Gabor extraction
def Gabor(p):   
    img=color.rgb2gray(image_list[p])
    real,imag = filters.gabor(img,frequency=0.7) #值越大，越有干扰；值太小，模糊
    #image_list[p] = cv2.cvtColor(image_list[p],cv2.COLOR_BGR2GRAY) 
    return set_list(real)


def sim_2pic(k,i):
    return Cos_Sim(Gabor(k),Gabor(i))
#color_list=[89, 43, 36, 901, 82, 58, 49, 68, 95, 0, 57, 25, 92, 81, 79, 97, 63, 47, 2, 10, 77, 11, 53, 72, 78, 59, 87, 62, 56, 96, 4, 66, 91, 1]
similarity = {}
for q in range(0,100):
#for q in color_list:
    similarity[q] = sim_2pic(1,q)
    sortedsim = sorted(similarity.items(), key = lambda item: item[1])
print(sortedsim)
