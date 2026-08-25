import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png")
if image is None:
    print("Error no image found")
    exit()
#input image
plt.figure(figsize=(6,6))
plt.imshow(image)
plt.title("Input image")
plt.show()
#open cv reads in bgr formate hence the image is blue
#convert the image to grya scale
rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#plot input image
plt.figure(figsize=(6,6))
plt.imshow(rgb_image)
plt.title("Input Image")
plt.axis("off")
plt.show()
#this will be red
#read image to gray scale
gray_image=cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png",cv2.IMREAD_GRAYSCALE)#here we can write here 0 instead of IMREAD_GRAYSCALE)
#plot input image
plt.figure(figsize=(6,6))
plt.imshow(gray_image,cmap="gray")
plt.title("Input Image")
plt.axis("off")
plt.show()
#negative transformation
negative_image=255-(gray_image)
#output image
plt.figure(figsize=(6,6))
plt.imshow(negative_image,cmap='gray')
plt.title("output Image")
plt.axis("off")
plt.show()

c=255/np.log1p(np.max(gray_image))
print(c)
#log transform
log_image=c * np.log(1+gray_image.astype(np.float32))
log_image = np.array(log_image,dtype=np.uint8)
#display input image
plt.figure(figsize=(6,6))
plt.imshow(log_image,cmap='gray')
plt.title("output Image")
plt.axis("off")
plt.show()
#inverse log transformation
inverse_log_transform=c*(np.e**(gray_image.astype(np.float32))-1)
#result=inverse_log_transform.astype(np.uint8)
plt.figure(figsize=(6,6))
plt.title("Inverse Log Transform")
plt.imshow(inverse_log_transform,cmap='gray')
plt.show()
#Power Law gamma transformation
threshold_image=cv2.threshold(gray_image,128,255,cv2.THRESH_BINARY)
gamma=2.0
normalized_img=gray_image/255.0
gamma_corrected_img=np.power(normalized_img,gamma)
out_img =(gamma_corrected_img )*255
plt.figure(figsize=(6,6))
plt.imshow(out_img,cmap='gray')
plt.show()
