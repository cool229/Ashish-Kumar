# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:31:11 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\lena_color_512.tif"
    img =cv2.imread(imgpath1, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     
   
    
    k = np.array(np.ones((11, 11), np.float32))/121
    
    k = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
    
    output = cv2.filter2D(img, -1, k)
    
    print(k)
    print(type(k))
    #output = img
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(output)
    plt.title('filtered Image')
    
    plt.show()
    
if __name__ =="__main__":
    main()
    