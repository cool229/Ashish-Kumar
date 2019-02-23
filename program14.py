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
    
    titles = ['Girl', 'Lena']
    images = [img1, img2]
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([]) 
        plt.yticks([])

    plt.show()
    
if __name__ == "__main__":
    main()