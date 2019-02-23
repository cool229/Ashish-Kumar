# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 10:06:29 2019

@author: KIIT
"""

import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\misc\\4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    ret, thresh = cv2.threshold(gray , 50, 255, 0)
    
    img2, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
#    print(contours)
#    print(hierachy)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    
    original = cv2.imread(imgpath, 1)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
      
    output =[original,img]     

    titles = ['Original',  'Contours']
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()     
    """
    plt.imshow(output[1])
    plt.title(output)
    """    
    plt.show()

if __name__ =="__main__":
    main()
    