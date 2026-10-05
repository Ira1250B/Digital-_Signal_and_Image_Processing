import numpy as np
import matplotlib.pyplot as plt
import cv2

#load all input images:
image1=cv2.imread(r"C:\Users\bhoga\Downloads\Picture1-9.png")
image2=cv2.imread(r"C:\Users\bhoga\Downloads\Picture2-9.png")
image3=cv2.imread(r"C:\Users\bhoga\Downloads\Picture3-9.png")
image4=cv2.imread(r"C:\Users\bhoga\Downloads\Picture4-9.png")
image5=cv2.imread(r"C:\Users\bhoga\Downloads\Picture5-9.png")

#smoothing filters
#1 Weighted Mean Filter
def wt_mean(image):
    weighted_kernel=np.asarray([[1,1,1],[1,2,1],[1,1,1]],dtype=np.float32)
    weighted_kernel=weighted_kernel/10
    weighted_mean=cv2.filter2D(image,-1,weighted_kernel)
    return weighted_mean
#2 gaussian filter
def gaussian_filter(image):
    g=cv2.GaussianBlur(image,(5,5),sigmaX=1)
    return g
#weighted mean filter
img1=wt_mean(image1)
img2=wt_mean(image2)
img3=wt_mean(image3)
img4=wt_mean(image4)
img5=wt_mean(image5)
#gaussian blur filter
im1=gaussian_filter(image1)
im2=gaussian_filter(image2)
im3=gaussian_filter(image3)
im4=gaussian_filter(image4)
im5=gaussian_filter(image5)
#plot of them  against orignal image for both filters
def plot(image,img,im):
    plt.figure(figsize=(10,8))
    plt.subplot(1,3,1)
    plt.imshow(image,cmap='gray')
    plt.title("original Image")
    plt.axis('off')
    plt.subplot(1,3,2)
    plt.imshow(img,cmap='gray')
    plt.title("Image with mean filter")
    plt.axis('off')
    plt.subplot(1,3,3)
    plt.imshow(im,cmap='gray')
    plt.title("Image with Gaussian blur filter")
    plt.axis('off')
    plt.tight_layout
    return plt.show()
plt1=plot(image1,img1,im1)
plt2=plot(image2,img2,im2)
plt3=plot(image3,img3,im3)
plt4=plot(image4,img4,im4)
plt5=plot(image5,img5,im5)