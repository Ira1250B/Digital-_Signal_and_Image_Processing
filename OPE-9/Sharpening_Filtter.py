import numpy as np
import matplotlib.pyplot as plt
import cv2

#load all input images:
image1=cv2.imread(r"C:\Users\bhoga\Downloads\Picture1-9.png")
image2=cv2.imread(r"C:\Users\bhoga\Downloads\Picture2-9.png")
image3=cv2.imread(r"C:\Users\bhoga\Downloads\Picture3-9.png")
image4=cv2.imread(r"C:\Users\bhoga\Downloads\Picture4-9.png")
image5=cv2.imread(r"C:\Users\bhoga\Downloads\Picture5-9.png")

#sharpening filters
#1.Laplacian Filter
def laplacian_filter(image):
    lap=cv2.Laplacian(image,cv2.CV_64F)
    lap_abs=cv2.convertScaleAbs(lap)
    return lap_abs
#2. roberts filter
def robert_filter(image):
    robertx=np.asarray([[1,0],[0,-1]],dtype=np.float32)
    roberty=np.asarray([[0,1],[-1,0]],dtype=np.float32)
    gx=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,robertx)
    gy=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,roberty)

    robert=cv2.magnitude(gx,gy)
    robert=cv2.normalize(robert,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
    return robert
#3. Priwitt filter
def prewitt(image):
    prewitt_x=np.asarray([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=np.float32)
    prewitt_y=np.asarray([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=np.float32)

    px=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,prewitt_x)
    py=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,prewitt_y)
    prewitt=cv2.magnitude(px,py)
    prewitt=cv2.normalize(prewitt,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
    return prewitt
iml1=laplacian_filter(image1)
iml2=laplacian_filter(image2)
iml3=laplacian_filter(image3)
iml4=laplacian_filter(image4)
iml5=laplacian_filter(image5)

imr1=robert_filter(image1)
imr2=robert_filter(image2)
imr3=robert_filter(image3)
imr4=robert_filter(image4)
imr5=robert_filter(image5)


imp1=prewitt(image1)
imp2=prewitt(image2)
imp3=prewitt(image3)
imp4=prewitt(image4)
imp5=prewitt(image5)
def plot(image,iml,imr,imp):
    plt.figure(figsize=(10,8))
    plt.subplot(1,4,1)
    plt.imshow(image,cmap='gray')
    plt.title("Original Image")
    plt.axis('off')
    plt.subplot(1,4,2)
    plt.imshow(iml)
    plt.title("Laplacian Filter")
    plt.axis('off')
    plt.subplot(1,4,3)
    plt.imshow(imr)
    plt.title("Roberts filter")
    plt.axis('off')
    plt.subplot(1,4,4)
    plt.imshow(imp)
    plt.title("Prewitt Filter")
    plt.axis('off')
    plt.tight_layout()
    return plt.show()
plt1=plot(image1,iml1,imr1,imp1)
plt2=plot(image2,iml2,imr2,imp2)
plt3=plot(image3,iml3,imr3,imp3)
plt4=plot(image4,iml4,imr4,imp4)
plt5=plot(image5,iml5,imr5,imp5)