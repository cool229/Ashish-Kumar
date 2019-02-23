# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:12:42 2019

@author: KIIT
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
  #path = "D:\\COURSES\\OpenCV\\Action\\misc\\"
    #imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.01.tiff"
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.04.tiff"
    img1 = cv2.imread(imgpath1, 1) 
    img1 = cv2.imread(imgpath1, cv2.COLOR_BGR2RGB)
    
    rows , columns , channels = img1.shape
    
    point1 = np.float32([[100, 100], [300,100], [100, 300]])
    point2 = np.float32([[200, 150], [400,150], [200, 400]])
    A = cv2.getAffineTransform(point1, point2)
    
    print (A)
    
    output = cv2.warpAffine(img1, A, (columns, rows))
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()
    
if __name__ =="__main__":
    main()