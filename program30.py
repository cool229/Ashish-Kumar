# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:38:17 2019

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
    
    point1 = np.float32([[0, 0], [400,0], [0, 400], [400, 400]])
    point2 = np.float32([[0, 0], [500,0], [0, 500], [500, 500]])
    p = cv2.getPerspectiveTransform(point1, point2)
    
    print (p)
    
    output = cv2.warpPerspective(img1, p, (columns, rows))
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()
    
if __name__ =="__main__":
    main()