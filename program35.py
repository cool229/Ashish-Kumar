# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 05:53:22 2019

@author: KIIT
"""
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
    
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.04.tiff"
    img1 =cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
 
    #output = cv2.resize(img1, None, fx=0.5, fy = 1.5, interpolation = cv2.INTER_AREA)
    noisy = np.zeros(img1.shape, np.uint8)
    rows, columns, channels = img1.shape
    p = 0.2
    
#    output = np.zeros(img1.shape, np.uint8)
    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r< p/2:
                # pepper sprinkled
                noisy[i][j] = [0, 0, 0]
            elif r<p:
                noisy[i][j] = [255, 255, 255]
            else:
                noisy[i][j] = img1[i][j]
    #gaussian = cv2.GaussianBlur(img1, (57, 37), 0)
    denoised = cv2.medianBlur(noisy, 5)
    gaussian = cv2.GaussianBlur(denoised, (57, 57), 0)
    output = [img1, noisy, denoised, gaussian]
    
    titles = ['Original', 'Noisy','Denoised', 'gaussian']
    for i in range(4):
        plt.subplot(2 , 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show() 
    
    plt.imshow(output[2])
    plt.title('ashish')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
if __name__ =="__main__":
    main()
    