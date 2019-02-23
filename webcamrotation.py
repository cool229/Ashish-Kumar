# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:46:24 2019

@author: KIIT
"""

import cv2
#import matplotlib.pyplot as plt
import time
def main():
    windowName ="Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        
    else:
        ret = False
        
    rows, columns, channels = frame.shape
    angle = 0
#    scale = 1
    scale = 0.1   
    while True: 
        
        ret, frame = cap.read()
        
        if angle == 360:
            angle = 0
            
        if scale < 1.5:
            scale = scale + 0.1
        
        if scale >=1.5:
            scale = 0.1
            

        print(scale)
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle , scale)
        print(scale)
        
        output = cv2.warpAffine(frame, R, (columns, rows))
        
        print(R)
        
        output = cv2.warpAffine(frame, R, (columns, rows))
        
        cv2.imshow(windowName, output)
        angle = angle + 10
        time.sleep(0.05)
        
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyWindow(windowName)
        
    cv2.destroyAllWindows()
    cap.release()
    
    
if __name__ =="__main__":
    main()          