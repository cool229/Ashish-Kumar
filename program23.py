# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 06:31:21 2019

@author: KIIT
"""


import cv2
#import matplotlib.pyplot as plt
import time
def main():
    
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.05.tiff"
    img1 =cv2.imread(imgpath1, 1)
    #img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
 
    img1 = cv2.resize(img1, None, fx=2, fy = 2, interpolation = cv2.INTER_AREA)
    rows, columns, channels = img1.shape
    angle = 360
    
    while True: 
        if angle == 0:
            angle = 360
        
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle , 0.5)
        print(R)
        
        output = cv2.warpAffine(img1, R, (columns, rows))
        
        
        cv2.imshow('Rotated Image', output)
        angle = angle - 1
        time.sleep(0.01)
        
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyWindow('Rotated Image')
    
    
if __name__ =="__main__":
    main()          