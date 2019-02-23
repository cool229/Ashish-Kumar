# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:41:36 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath, 1) 
    ### reading the single image for the given path
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('Color Image with default colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()


   # img1 = cv2.cvtColor(img1, cv2.COLOR_BAYER_BG2BGR )
    plt.imshow(img1)
    plt.title('Color Image with default colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    
    #cv2.imshow('Lena',img) ## showing image
    #cv2.waitKey(0) ## waiting for the keyboard event 
    #cv2.destroyAllWindows() ## distroy all the window
if __name__ == "__main__":
    main()