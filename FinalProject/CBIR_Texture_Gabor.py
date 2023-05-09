#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:28:03 2019

@author: mac
"""

from skimage import data,filters,color,io
from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

#Gabor 滤波器'
img=color.rgb2gray(image_list[308])
#img=color.rgb2gray(io.imread('/Users/mac/Desktop/project/code/纹理GaborFre/树叶.jpg'))
real,imag = filters.gabor(img,frequency=0.65) #值越大，越有干扰；值太小，模糊


plt.subplot(121)
plt.imshow(imag,plt.cm.gray)
plt.title('Ideal image'),plt.xticks([]),plt.yticks([])

plt.subplot(122)
plt.imshow(real,plt.cm.gray)
plt.title('Real image'),plt.xticks([]),plt.yticks([])

plt.show()
