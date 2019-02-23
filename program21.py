# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 05:40:48 2019

@author:  KIIT
"""

import cv2
#import matplotlib.pyplot as plt
def main():
    
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.05.tiff"
    img1 =cv2.imread(imgpath1, 1)
    
    img1 = cv2.resize(img1, None, fx=2, fy = 2, interpolation = cv2.INTER_AREA)
    
    cv2.imshow('Output', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ =="__main__":
    main()          