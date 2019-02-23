# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:09:55 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    z =img.reshape((-1, 3))
    z = np.float32(z)
    
    criteria =(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    k = 2
    ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10,
                                      cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img.shape))
    
    k = 6
    ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10,
                                      cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output2 = res1.reshape((img.shape))
    
    #output2 = img
    k = 12
    ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10,
                                      cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img.shape))
    

    output = [img, output1, output2, output3]
    
    titles = ['Original Image', 'K = 2' , 'K = 4', 'K =12']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
if __name__ =="__main__":
    main()