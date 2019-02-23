# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:34:51 2019

@author: KIIT
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\misc\\4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #R, G, B = cv2.split(img)
    red_hist = cv2.calcHist([img], [0], None, [256], [0, 255])
    green_hist = cv2.calcHist([img], [1], None, [256], [0, 255])
    blue_hist = cv2.calcHist([img], [2], None, [256], [0, 255])
    
    plt.subplot(3, 1, 1)
    plt.xlim([0, 255])
    plt.plot(red_hist, color = 'r')
    plt.title('RED Histogram')
    plt.show()
    
    plt.subplot(3, 1, 2)
    plt.xlim([0, 255])
    plt.plot(green_hist, color = 'g')
    plt.title('GREEN Histogram')
    plt.show()
    
    plt.subplot(3, 1, 3)
    plt.xlim([0, 255])
    plt.plot(blue_hist, color = 'b')
    plt.title('BLUE Histogram')
   
    plt.show()
    
    
    
if __name__ =="__main__":
    main()
    