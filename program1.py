# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:23:44 2019

@author: KIIT
"""

import cv2
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath) 
    ### reading the single image for the given path
    
    cv2.imshow('Lena',img) ## showing image
    cv2.waitKey(0) ## waiting for the keyboard event 
    cv2.destroyAllWindows() ## distroy all the window
if __name__ == "__main__":
    main()