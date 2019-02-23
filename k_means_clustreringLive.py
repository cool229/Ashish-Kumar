# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:09:55 2019

@author: KIIT
"""

import cv2
#import matplotlib.pyplot as plt
import numpy as np
def main():
    
    w = 160
    h = 120
    
    cap = cv2.VideoCapture(0)
    cap.set(3, w)
    cap.set(4, h)
   
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
#        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        z =frame.reshape((-1, 3))
        z = np.float32(z)
    
        criteria =(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        k = 5
        ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10,
                                      cv2.KMEANS_RANDOM_CENTERS)
        center1 = np.uint8(center1)
        res1 = center1[label1.flatten()]
        output1 = res1.reshape((frame.shape))
    
      
        cv2.imshow("original", frame)
        cv2.imshow("Quantized", output1)
        
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ =="__main__":
    main()