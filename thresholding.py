# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:53:42 2019

@author: KIIT
"""
import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\misc\\gray21.512.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ### reading the single image for the given path
    
    th = 100
    max_val = 255
    
    ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)
    ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)
    ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO)
    ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV)
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC)
    #ret, o6 = cv2.threshold(img, th, max_val, cv2.THRESH_OTSU)
    
    output =[img, o1, o2, o3, o4, o5 ]     
    plt.title('Original Image')
    titles = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']
    
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ =="__main__":
    main()
    