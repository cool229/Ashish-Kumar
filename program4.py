# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 23:17:57 2019

@author: KIIT
"""

import cv2
import numpy as np
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\lena_color_256.tif"
    img1 = cv2.imread(imgpath,0) 
    ### reading the single image for the given path
    print(type(img1))
    print(img1.dtype)
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    cv2.imshow('Lena',img1) ## showing image
    cv2.waitKey(0) ## waiting for the keyboard event 
    cv2.destroyWindow('Lena') ## distroy all the window
if __name__ == "__main__":
    main()