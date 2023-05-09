from matplotlib import pyplot as plt
from cv2 import cv2
import numpy as np
import matplotlib
import os

#the path of the folder pic which collects all the pictures
picture_path = 'C:\\Users\\16593\\Desktop\\images'
#the file name of image titles
img_name_filename = 'img_name.txt'
#the file name of image titles
img_tags_filename = 'img_tags.txt'

def get_image_number():
    idx_list = []
    for pic_title in os.listdir(picture_path):
        idx_list.append( int(str(pic_title).replace('.jpg','')) )
    return len(idx_list)

def get_image(idx):
    img_file_name = picture_path + '\\{}.jpg'.format(idx)
    img = cv2.imread(img_file_name)
    return img

def load_image_list():
    image_list = []
    n = get_image_number()
    for i in range(0,n):
        image_list.append(get_image(i))
    return image_list



#list of all images in the form of matrices
image_list = load_image_list()

#list of tags of all images
image_tags = []
with open(img_tags_filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        tag = list(eval(line))
        image_tags.append(tag) 

if __name__ == '__main__':
    for tag in image_tags:
        print(tag)
    for img in image_list:
        print(img)
