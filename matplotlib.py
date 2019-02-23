# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:11:36 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath, 0) 
    ### reading the single image for the given path
    
    plt.imshow(img, cmap ='gray')
    plt.title('gray Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img)
    plt.title('Default Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    #cv2.imshow('Lena',img) ## showing image
    #cv2.waitKey(0) ## waiting for the keyboard event 
    #cv2.destroyAllWindows() ## distroy all the window
if __name__ == "__main__":
    main()