# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 23:56:28 2019

@author: KIIT
"""

import cv2
import numpy as np

def main():
    
    img1 = np.zeros((512,512,3), np.uint8)
    
    cv2.line(img1, (0, 99), (99, 0), (255,0,0), 2) # passing platform , one-coordinate, other-coordinate , and color , and thickness
    cv2.rectangle(img1, (100, 60), (220, 170), (0, 255, 0), 2)# passing ... coordinates of x and y  and color and size
    cv2.circle(img1, (60, 60), 50, (0, 0, 255), -1) # passing coordinate of centre , radius and color and size
    cv2.ellipse(img1, (160, 260), (120 , 20), 0,  0, 360, (127, 127, 127), -1) # passing one coordinate and major axis and minor axis and angle of rotationa and other all are same
    
    points = np.array([[80,2],[125,0],[179,0],[230,5],[30,50]], np.int32) # collecting various coordinates and datatypes
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img1, [points] , True, (0,255 ,255))# coordinates , ... and others
    
    text1 = 'Ashish Kumar'
    cv2.putText(img1, text1, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1,( 255, 255, 0))
    cv2.imshow('Lena', img1)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
     
if __name__ == "__main__":
    main()