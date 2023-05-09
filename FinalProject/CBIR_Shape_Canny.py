from data.data import image_list
from matplotlib import pyplot as plt
from cv2 import cv2
import numpy as np
import matplotlib
import os
from skimage import io

#转化为灰度图
image = cv2.cvtColor(image_list[2],cv2.COLOR_BGR2GRAY) 
#image=cv2.imread('/Users/mac/Desktop/project/code/轮廓CannyThreshold/宇宙2.jpg') 
#canny边缘检测
canny = cv2.Canny(image,100,350)  #threshold

plt.subplot(121)
plt.imshow(image,plt.cm.gray)
plt.title('original image'),plt.xticks([]),plt.yticks([])
plt.subplot(122)
plt.imshow(canny,plt.cm.gray)
plt.title('Ideal image'),plt.xticks([]),plt.yticks([])
cv2.imwrite("###.png",canny) #canny二值图：灰度等级0或255
plt.show()

