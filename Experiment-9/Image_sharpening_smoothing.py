import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png")
#mean filter, in weighted mean we have to count the additional number that I have given as weight in sort sum of all the values
#as kernel size increases smoothening will increase
weighted_kernel=np.asarray([[1,1,1],[1,2,1],[1,1,1]],dtype=np.float32)
weighted_kernel=weighted_kernel/10
weighted_mean=cv2.filter2D(image,-1,weighted_kernel)
kernel2=np.asarray([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]],dtype=np.float32)
kernel2=kernel2/26
kernel2_mean=cv2.filter2D(image,-1,kernel2)

plt.figure(figsize=(6,4))
plt.subplot(1,3,1)
plt.imshow(image,cmap='gray')
plt.title("Original image")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(weighted_mean,cv2.COLOR_BGR2RGB))
plt.title("Weighted Mean Filter")
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(kernel2_mean,cv2.COLOR_BGR2RGB))
plt.title("Image with 5x5 kernel")
plt.axis('off')
plt.show()
#gaussina filter
#here the image smoothing depends on value of sigma
g0=cv2.GaussianBlur(image,(5,5),sigmaX=0)
g1=cv2.GaussianBlur(image,(5,5),sigmaX=1)
plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(g0,cv2.COLOR_BGR2RGB))
plt.title("sigma=0")
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(g1,cv2.COLOR_BGR2RGB))
plt.title("sigma=1")
plt.axis('off')
plt.show()

#sharpening Filters
#1.Laplasian filter
laplasian=cv2.Laplacian(image,cv2.CV_64F)
#CV_64F allows all positive negative and decimal values
laplasian_abs=cv2.convertScaleAbs(laplasian)
#convert signed laplacian values to positive magnitudes and 8-bit formates for visualization
plt.imshow(laplasian_abs,cmap='gray')
plt.title("Laplacian edge detection")
plt.axis('off')
plt.show()

#roberts filter 
roberts_x=np.asarray([[1,0],[0,-1]],dtype=np.float32)
roberts_y=np.asarray([[0,1],[-1,0]],dtype=np.float32)

gx=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,roberts_x)
gy=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,roberts_y)

roberts=cv2.magnitude(gx,gy)
roberts=cv2.normalize(roberts,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
plt.imshow(roberts,cmap='gray')
plt.title('Roberts Edge Detection')
plt.axis('off')
plt.show()

#Prewitt operator
prewitt_x=np.asarray([[-1,0,1],[-1,0,1],[-1,0,1]],dtype=np.float32)
prewitt_y=np.asarray([[-1,-1,-1],[0,0,0],[1,1,1]],dtype=np.float32)

px=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,prewitt_x)
py=cv2.filter2D(image.astype(np.float32),cv2.CV_32F,prewitt_y)
prewitt=cv2.magnitude(px,py)
prewitt=cv2.normalize(prewitt,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
plt.imshow(prewitt,cmap='gray')
plt.show()