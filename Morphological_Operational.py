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
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\misc\\4.2.05.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ## reading the single image for the given path
    
#    th = 0  
#    max_val = 255
    
#    ret, binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
#    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#    k =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    
    
    erosion = cv2.erode(img, k, iterations =5)
    
    dilation = cv2.dilate(img, k, iterations = 5)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
    print(k)
    output =[img,erosion,dilation,gradient]     
    plt.title('Original Image')
    titles = ['Original',  'erosion','Dilation','gradient']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap ='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    
        
    plt.show()

    
    
if __name__ =="__main__":
    main()
    