# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:21:23 2019

@author: KIIT
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 05:53:22 2019

@author: KIIT
"""
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np
def main():
    
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\lena_color_512.tif"
    img1 =cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
 
    #output = cv2.resize(img1, None, fx=0.5, fy = 1.5, interpolation = cv2.INTER_AREA)
    
    rows, columns, channels = img1.shape
    p = 0.2
    
    output = np.zeros(img1.shape, np.uint8)
    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r< p/2:
                # pepper sprinkled
                output[i][j] = [0, 0, 0]
            elif r<p:
                output[i][j] = [255, 255, 255]
            else:
                output[i][j] = img1[i][j]
   
    
    plt.imshow(output)
    plt.title('Image with salt and pepper noise')
    plt.show()
    
if __name__ =="__main__":
    main()          