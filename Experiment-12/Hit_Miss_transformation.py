import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the binary image
image = cv2.imread(r"C:\Users\bhoga\Downloads\Picture1-6.png",0)
# Define the structuring element for the pattern to be detected (0 for don't care, 1 for foreground, -1 for background)
pattern = np.array([[-1, 1, -1],
                    [1, 1, 1],
                    [-1, 1, -1]], dtype=np.int8)

# Apply the Hit or Miss Transformation
result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, pattern)

# Display the original image and the result
plt.figure(figsize=(8,6))
plt.subplot(1,2,1)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(result,cmap='gray')
plt.title("Resulting image after transformation")
plt.axis('off')
plt.show()
