# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:55:13 2019

@author: KIIT
"""


import cv2
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\cameraman.tif"
    img = cv2.imread(imgpath,0) 
    ### reading the single image for the given path
    outpath = "D:\\COURSES\\OpenCV\\Action\\output\\cameraman.jpg"
    
    cv2.imshow('Lena',img) ## showing image
    cv2.imwrite(outpath, img)
    cv2.waitKey(0) ## waiting for the keyboard event 
    cv2.destroyWindow('Lena') ## distroy all the window
if __name__ == "__main__":
    main()