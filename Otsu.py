# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:29:53 2019

@author: KIIT
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:53:42 2019

@author: KIIT
"""
import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\cameraman.tif"
    img = cv2.imread(imgpath, 0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ### reading the single image for the given path
    
    th = 0  
    max_val = 255
    
    ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    
    output =[img, o1, o2, o3, o4, o5 ]     
    plt.title('Original Image')
    titles = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']
    
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(output[i], cmap ='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
    plt.imshow(o5, cmap ='gray')
    plt.title('tank')
    plt.xticks([])
    plt.yticks([])
    
    
if __name__ =="__main__":
    main()
    