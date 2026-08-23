import cv2
import numpy as np
import matplotlib.pyplot as plt
#nask means a part of image only some part of image will be used here I will set it to null
#when I remove cmap gray aprt I see green and bluish image that is because it uses the by default pallate verdic.
#also if I want normalizatioon to be good like not almost zero then I should take image size small as I will get the image range less and it will show proper normalization
def generate_histogram(image):
    histogram=cv2.calcHist([image],[0],None,[256],[0,256])
    return histogram
image_path=cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png")


gray_image=cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)
input_hist=generate_histogram(gray_image)
intensity=np.arange(256)
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.imshow(gray_image,cmap="gray")
plt.title("Input image")
plt.axis("off")
plt.subplot(1,2,2)
plt.bar(intensity, input_hist)
plt.title("Input Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency / number of pixels")
plt.xlim([0, 255])
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()
total_pixels = gray_image.size

# Normalize the histogram
normalized_hist = input_hist / total_pixels

# Display original and normalized histograms
plt.figure(figsize=(12, 5))

# Original histogram
plt.subplot(1, 2, 1)
plt.bar(intensity, input_hist, width=1)
plt.title("Original Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency / Number of Pixels")
plt.xlim([0, 255])
plt.grid(alpha=0.25)

# Normalized histogram
plt.subplot(1, 2, 2)
plt.bar(intensity, normalized_hist)
plt.title("Normalized Histogram")
plt.xlabel("Intensity")
plt.ylabel("Probability")
plt.xlim([0, 255])
plt.ylim([0, 1])
plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()

def perform_histogram_equalization(image):
  # Convert image to grayscale
  gray_image = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

  # Apply histogram equalization
  equalized_image = cv2.equalizeHist(gray_image)
  return equalized_image
# Perform histogram equalization
equalized_image = perform_histogram_equalization(image_path)

# Generate histograms
original_hist = generate_histogram(gray_image)
equalized_hist = generate_histogram(equalized_image)

# Create intensity values from 0 to 255
intensity = np.arange(256)

# Display everything in a 2 × 2 layout
plt.figure(figsize=(12, 8))

# 1. Original Image
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# 2. Original Histogram
plt.subplot(2, 2, 2)
plt.bar(intensity, original_hist)
plt.title("Original Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 255])
plt.grid(alpha=0.25)

# 3. Equalized Image
plt.subplot(2, 2, 3)
plt.imshow(equalized_image)
plt.title("Equalized Image")
plt.axis("off")

# 4. Equalized Histogram
plt.subplot(2, 2, 4)
plt.bar(intensity, equalized_hist)
plt.title("Equalized Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 255])
plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()
## Histogram Matching
# Load the input image
input_image = cv2.imread(r"C:\Users\bhoga\Downloads\Final_Image.png")

# Convert the image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Load the reference image

reference_image = cv2.imread(r"C:\Users\bhoga\Downloads\ChatGPT Image Mar 24, 2026, 04_02_56 PM.png")

# Convert the reference image to grayscale
gray_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

from skimage.exposure import match_histograms
# Perform histogram matching
matched_image = match_histograms(gray_image,gray_reference)
matched_image.dtype
# Convert the matched image to 8-bit format
matched_image = np.uint8(matched_image)
matched_image.dtype
# Generate the histogram of the original image
original_hist = generate_histogram(gray_image)

# Generate the histogram of the reference image
reference_hist = generate_histogram(gray_reference)

# Generate the histogram of the matched image
matched_hist = generate_histogram(matched_image)
# Create intensity values from 0 to 255
intensity = np.arange(256)

# Display images and histograms
plt.figure(figsize=(15, 9))

# Display the original image
plt.subplot(2, 3, 1)
plt.imshow(gray_image)
plt.title("Original Image")
plt.axis("off")

# Display the reference image
plt.subplot(2, 3, 2)
plt.imshow(gray_reference)
plt.title("Reference Image")
plt.axis("off")

# Display the matched image
plt.subplot(2, 3, 3)
plt.imshow(matched_image)
plt.title("Histogram Matched Image")
plt.axis("off")

# Display the original histogram
plt.subplot(2, 3, 4)
plt.bar(intensity, original_hist, width=1)
plt.title("Original Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency / number of pixels")
plt.xlim([0, 255])
plt.grid(alpha=0.25)

# Display the reference histogram
plt.subplot(2, 3, 5)
plt.bar(intensity, reference_hist, width=1)
plt.title("Reference Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency / number of pixels")
plt.xlim([0, 255])
plt.grid(alpha=0.25)

# Display the matched histogram
plt.subplot(2, 3, 6)
plt.bar(intensity, matched_hist, width=1)
plt.title("Matched Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency / number of pixels")
plt.xlim([0, 255])
plt.grid(alpha=0.25)


plt.tight_layout()


plt.show()
