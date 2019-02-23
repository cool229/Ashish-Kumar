# showing image of the alpha and beta
import cv2
import numpy as np
import time
def main():
    
    #path = "D:\\COURSES\\OpenCV\\Action\\misc\\"
    imgpath1 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.01.tiff"
    imgpath2 = "D:\\COURSES\\OpenCV\\Action\\misc\\4.1.04.tiff"
    img1 = cv2.imread(imgpath1, 1) 
    img2 = cv2.imread(imgpath2, 1)
    
#    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    alpha =0.0
    beta = 1.0
    gamma = 0.0
    
    for i in np.linspace(0, 1, 100):
        alpha = i 
        beta = 1 - i
        output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
        cv2.imshow('Transition', output)
        time.sleep(0.02)
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyAllWindows()
    
   
    
if __name__ == "__main__":
    main()