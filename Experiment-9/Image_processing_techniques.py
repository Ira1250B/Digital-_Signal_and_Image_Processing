import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png")
# plt.imshow(image,cmap='gray')
plt.show()
print(image.shape)
cv2.imwrite(r"D:\DAA\image.jpg",cv2.cvtColor(image,cv2.COLOR_RGB2BGR))
# #if I want ot print height width or plane 
print(image.shape[0])
print(image.shape[1])
print(image.shape[2])
print(image.dtype)
# #now to split image  into three parts we do 
r,g,b=cv2.split(image)
fig,ax=plt.subplots(1,4,figsize=(16,4))
ax[0].imshow(image)
ax[1].imshow(r,cmap='Reds')
ax[2].imshow(g,cmap='Greens')
ax[3].imshow(b,cmap='Blues')
for a in ax: a.axis('off')
plt.show()

# # im2=cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png",1)
# # plt.imshow()
# # plt.figure(figsize=(6,4))
# # plt.sublpot(1,2,1)
plt.axis("on")
plt.show()
crop=image[50:250,50:250]
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.imshow(image)
plt.title("original image")
plt.subplot(1,2,2)
plt.imshow(crop)
plt.show()
#figure resize
rev=cv2.resize(200,200)
#image rotation
h,w=image.shape[:2]
