# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:56:25 2019

@author: KIIT
"""


#
import cv2
import matplotlib.pyplot as plt
def main():
    
    #path = "D:\\COURSES\\OpenCV\\Action\\misc\\"
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.01.tiff"
    imgpath2 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.04.tiff"
    img1 = cv2.imread(imgpath1, 1) 
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    alpha = 0.7
    beta = 0.3
    gamma = 0
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    titles = ['Girl', 'Lena','Weighted Addition']
    images = [img1, img2, output]
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    plt.imshow(output)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
   
    
if __name__ == "__main__":
    main()