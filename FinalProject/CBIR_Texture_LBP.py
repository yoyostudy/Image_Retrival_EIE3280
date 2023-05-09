#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:30:37 2019

@author: mac
"""

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data,io,data_dir,filters,feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

##convert image to gray image
radius = 1
n_points = 8*radius
image = cv2.cvtColor(image_list[184],cv2.COLOR_BGR2RGB)
#image = cv2.imread('/Users/mac/Desktop/project/code/纹理LBP/huang.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

##lbp处理
lbp = local_binary_pattern(image,n_points,radius)

plt.subplot(121)
plt.imshow(image,plt.cm.gray)
plt.title('Original image'),plt.xticks([]),plt.yticks([])

#plt.subplot(122)
plt.imshow(lbp,plt.cm.gray)
plt.title('R=1  P=8'),plt.xticks([]),plt.yticks([])

plt.show()
