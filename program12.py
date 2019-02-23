# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 05:23:04 2019

@author: KIIT
"""
# RUNNING A VIDEO FILE WITHOUT ANY SOUND

import cv2

def main():
    windowName ="OpenCV Video Player"
    cv2.namedWindow(windowName)
    
    filename = 'D:\\COURSES\\OpenCV\\Action\\output\\Output.avi'
    cap = cv2.VideoCapture(filename)
    
    
        
    while (cap.isOpened()):
        ret, frame = cap.read()
        print(ret)
        
        if ret:  
            cv2.imshow(windowName, frame)
            if cv2.waitKey(33) == 27:
                break
        else:
            break
        
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":        
    main()