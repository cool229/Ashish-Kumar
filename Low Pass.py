import cv2
import matplotlib.pyplot as plt


def main():
    
    imgpath = "D:\\COURSES\\OpenCV\\Action\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    box = cv2.boxFilter(img, -1, (53, 53))
    
    blur = cv2.blur(img, (50, 50))
    
    gaussian = cv2.GaussianBlur(img, (57, 37), 0)
    
    titles = ['Original Image', 'Box Filter', 
              'Blur', 'Gaussian Blur']

    outputs = [img, box, blur, gaussian]
    
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(outputs[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()