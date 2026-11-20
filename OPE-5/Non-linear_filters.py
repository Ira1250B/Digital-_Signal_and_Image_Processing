import numpy as np
import matplotlib.pyplot as plt
import cv2

image1=cv2.imread(r"C:\Users\bhoga\Downloads\Picture1-9.png",0)
image2=cv2.imread(r"C:\Users\bhoga\Downloads\Picture2-9.png",0)
image3=cv2.imread(r"C:\Users\bhoga\Downloads\Picture3-9.png",0)
image4=cv2.imread(r"C:\Users\bhoga\Downloads\Picture4-9.png",0)
image5=cv2.imread(r"C:\Users\bhoga\Downloads\Picture5-9.png",0)

def median_filter(image,n):
    img=cv2.medianBlur(image,n)
    return img
filter_img1=median_filter(image1,3)
filter_img2=median_filter(image2,3)
filter_img3=median_filter(image3,3)
filter_img4=median_filter(image4,3)
filter_img5=median_filter(image5,3)

fil_img1=median_filter(image1,5)
fil_img2=median_filter(image2,5)
fil_img3=median_filter(image3,5)
fil_img4=median_filter(image4,5)
fil_img5=median_filter(image5,5)

def plot(image,img1,img2):
    plt.figure(figsize=(8,6))
    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.imshow(image,cmap='gray')
    plt.axis('off')
    plt.subplot(1,3,2)
    plt.title("Medain Filter of window size 3 ")
    plt.imshow(img1,cmap='gray')
    plt.axis('off')
    plt.subplot(1,3,3)
    plt.title("Median Filter of window size 5")
    plt.imshow(img2,cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    return plt.show()
plt1=plot(image1,filter_img1,fil_img1)
plt2=plot(image2,filter_img2,fil_img2)
plt3=plot(image3,filter_img3,fil_img3)
plt4=plot(image4,filter_img4,fil_img4)
plt5=plot(image5,filter_img5,fil_img5)