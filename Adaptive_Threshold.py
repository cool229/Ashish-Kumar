# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:17:34 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.05.tiff"
    img = cv2.imread(imgpath, 0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ### reading the single image for the given path
    
    block_size = 513
    constant = 2
    
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)    
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)

    output =[img, th1, th2]     
    titles = ['Original', 'Mean Adaptive','Gaussian Adaptive']
    
    
    for i in range(3):
        plt.subplot(1 , 3, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
    
    
if __name__ =="__main__":
    main()
    