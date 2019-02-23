# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 05:46:01 2019

@author: KIIT
"""

# IMAGE TRACKING BY COLOR 
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
         #Blue Color
        #low = np.array([100, 50, 50])
        #high = np.array([140, 255, 255])
        
        #Green Color
        #low = np.array([40, 50, 50])
        #high = np.array([80, 255, 255])
        
        #Red
        #[0,100,100] and high=[10,255,255]﻿
        #low = np.array([0, 100, 100])
        #high = np.array([10,255, 255])
        
        #body
        low = np.array([0, 20, 70])
        high = np.array([20,255, 255])
        
        image_mask = cv2.inRange(hsv, low, high)
        
        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow("Image mask", image_mask)
        cv2.imshow("Original Webcam Feed", frame)
        cv2.imshow("Color Tracking" , output)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
if __name__ =="__main__":
    main()