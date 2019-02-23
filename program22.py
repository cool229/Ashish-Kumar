# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 05:53:22 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
#import numpy as np
def main():
    
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.05.tiff"
    img1 =cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
 
    #output = cv2.resize(img1, None, fx=0.5, fy = 1.5, interpolation = cv2.INTER_AREA)
    
    rows, columns, channels = img1.shape
    
    R = cv2.getRotationMatrix2D((columns/2, rows/2), 370, 0.5)
    # 1st argument is from where to rotate, and angle with which to rotate and scalling i.es smaller
    print(R)
    
    output = cv2.warpAffine(img1, R, (columns, rows))
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()
    
if __name__ =="__main__":
    main()          