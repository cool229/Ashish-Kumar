# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:00:26 2019

@author: KIIT
"""


import cv2
import matplotlib.pyplot as plt
def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\misc\\7.1.02.tiff"
    img = cv2.imread(imgpath, 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    L1 = cv2.Canny(img, 50, 500, L2gradient = False)
    
    L2 = cv2.Canny(img, 100, 150, L2gradient = True)
    
    titles = ['Original', 'L1 Norm', 'L2 Norm']
    
    output = [img, L1, L2]
    for i in range(3):
        plt.subplot(1 , 3, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
    
    
if __name__ =="__main__":
    main()
    