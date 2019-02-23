# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 04:23:19 2019

@author: KIIT
"""
# Transition Effect
import cv2

def emptyFunction():
    pass

def main():
    
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.01.tiff"
    imgpath2 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.02.tiff"
    img1 = cv2.imread(imgpath1, 1) 
    img2 = cv2.imread(imgpath2, 1)  
    
    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    
    windowName = "Transtion Demo"
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('Alpha', windowName, 0, 1000, emptyFunction)
    while(True):
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
        
        alpha = cv2.getTrackbarPos('Alpha', windowName) / 1000
        beta = 1 - alpha 
        
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        
        print(alpha, beta)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()