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
    img = cv2.imread(imgpath, 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#    R, G, B = cv2.split(img)
#    plt.subplot(1, 4, 1)
#    plt.imshow(img, cmap='gray')
#    plt.title('Image')
#    plt.xticks([])
#    plt.yticks([])
      
   
    
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap = 'gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    hist, bins = np.histogram(img.ravel(), 256, [0, 255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist)
    plt.title('Histogram')
   
  
    plt.show()
    
    
    
if __name__ =="__main__":
    main()
    