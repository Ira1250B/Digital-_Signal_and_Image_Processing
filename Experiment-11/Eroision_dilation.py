import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'C:\Users\bhoga\Downloads\dealer-2-scaled-1.jpg', 0)  # Load as grayscale
iimage=255-image
# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform Erosion
erosion = cv2.erode(image, kernel, iterations=3)

# Perform Dilation
dilation = cv2.dilate(image, kernel, iterations=3)

# Perform Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Perform Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original image and the results
plt.figure(figsize=(10,8))
plt.subplot(2,3,1)
plt.imshow(image,cmap='gray')
plt.title("Original image")
plt.axis('off')
plt.subplot(2,3,2)
plt.imshow(erosion,cmap='gray')
plt.title("Erodded image")
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(dilation,cmap='gray')
plt.title("Dilated Image")
plt.axis('off')
plt.subplot(2,3,4)
plt.imshow(opening,cmap='gray')
plt.title("Applied Opeaning on image")
plt.axis('off')
plt.subplot(2,3,5)
plt.imshow(closing,cmap='gray')
plt.title("Applied closing on image")
plt.axis('off')
plt.tight_layout()
plt.show()


