
# Load five images individually and apply frequency-domain smoothing, sharpening and boundary detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread(r"C:\Users\bhoga\Downloads\Picture1-9.png", 0)
img2 = cv2.imread(r"C:\Users\bhoga\Downloads\Picture2-9.png", 0)
img3 = cv2.imread(r"C:\Users\bhoga\Downloads\Picture3-9.png", 0)
img4 = cv2.imread(r"C:\Users\bhoga\Downloads\Picture4-9.png", 0)
img5 = cv2.imread(r"C:\Users\bhoga\Downloads\Picture5-9.png", 0)

#Smoothing Filter Butter worth Low pass filter and Gaussian Low pass filter
def gaussian_lpf(img, cutoff=30):
    rows, cols = img.shape
    y, x = np.ogrid[:rows, :cols]
    D = np.sqrt((x - cols//2)**2 + (y - rows//2)**2)

    H = np.exp(-(D**2) / (2 * cutoff**2))

    F = np.fft.fftshift(np.fft.fft2(img))
    result = np.fft.ifft2(np.fft.ifftshift(F * H))

    return np.clip(np.real(result), 0, 255).astype(np.uint8)


def butterworth_lpf(img, cutoff=30, order=2):
    rows, cols = img.shape
    y, x = np.ogrid[:rows, :cols]
    D = np.sqrt((x - cols//2)**2 + (y - rows//2)**2)

    H = 1 / (1 + (D / cutoff)**(2 * order))

    F = np.fft.fftshift(np.fft.fft2(img))
    result = np.fft.ifft2(np.fft.ifftshift(F * H))

    return np.clip(np.real(result), 0, 255).astype(np.uint8)
im_g1=gaussian_lpf(img1)
im_g2=gaussian_lpf(img2)
im_g3=gaussian_lpf(img3)
im_g4=gaussian_lpf(img4)
im_g5=gaussian_lpf(img5)

im_b1=butterworth_lpf(img1)
im_b2=butterworth_lpf(img2)
im_b3=butterworth_lpf(img3)
im_b4=butterworth_lpf(img4)
im_b5=butterworth_lpf(img5)
#Sharpening filters for preserving details. Gaussain high pass filter and high boost filtering 

def gaussian_hpf(img, cutoff=30):
    rows, cols = img.shape
    y, x = np.ogrid[:rows, :cols]
    D = np.sqrt((x - cols//2)**2 + (y - rows//2)**2)

    H = 1 - np.exp(-(D**2) / (2 * cutoff**2))

    F = np.fft.fftshift(np.fft.fft2(img))
    result = np.fft.ifft2(np.fft.ifftshift(F * H))

    result = np.abs(np.real(result))
    return np.clip(result, 0, 255).astype(np.uint8)


def high_boost(img, cutoff=30, strength=2):
    rows, cols = img.shape
    y, x = np.ogrid[:rows, :cols]
    D = np.sqrt((x - cols//2)**2 + (y - rows//2)**2)

    H = 1 + strength * (1 - np.exp(-(D**2) / (2 * cutoff**2)))

    F = np.fft.fftshift(np.fft.fft2(img))
    result = np.fft.ifft2(np.fft.ifftshift(F * H))
    return np.clip(np.real(result), 0, 255).astype(np.uint8)
im_gh1=gaussian_hpf(im_g1)
im_gh2=gaussian_hpf(im_g2)
im_gh3=gaussian_hpf(im_g3)
im_gh4=gaussian_hpf(im_g4)
im_gh5=gaussian_hpf(im_g5)

im_hb1=high_boost(im_g1)
im_hb2=high_boost(im_g2)
im_hb3=high_boost(im_g3)
im_hb4=high_boost(im_g4)
im_hb5=high_boost(im_g5)
# boundry extraction using canny EDge detection
def canny_edges(img):
    edges = cv2.Canny(img,180,60)
    return edges
cn1=canny_edges(im_hb1)
cn2=canny_edges(im_hb2)
cn3=canny_edges(im_hb3)
cn4=canny_edges(im_hb4)
cn5=canny_edges(im_hb5)
def plot(image,im1,im2,im3,im4,im6):
    plt.figure(figsize=(10,8))
    plt.subplot(3,3,1)
    plt.imshow(image,cmap='gray')
    plt.title("Original Image")
    plt.axis('off')
    plt.subplot(3,3,2)
    plt.imshow(im1,cmap='gray')
    plt.title("Gaussian Low Pass Filter")
    plt.axis('off')
    plt.subplot(3,3,3)
    plt.imshow(im2,cmap='gray')
    plt.title("Butterworth Low Pass Filter")
    plt.axis('off')
    plt.subplot(3,3,4)
    plt.imshow(im3,cmap='gray')
    plt.title("Gaussain High Pass Filter")
    plt.axis('off')
    plt.subplot(3,3,5)
    plt.imshow(im4,cmap='gray')
    plt.title("High Boost Filtering")
    plt.axis('off')
    plt.subplot(3,3,6)
    plt.imshow(im6,cmap='gray')
    plt.title("Canny Edge  Detection")
    plt.axis('off')
    plt.tight_layout()
    return plt.show()
plt1=plot(img1,im_g1,im_b1,im_gh1,im_hb1,cn1)
plt2=plot(img2,im_g2,im_b2,im_gh2,im_hb2,cn2)
plt3=plot(img3,im_g3,im_b3,im_gh3,im_hb3,cn3)
plt4=plot(img4,im_g4,im_b4,im_gh4,im_hb4,cn4)
plt5=plot(img5,im_g5,im_b5,im_gh5,im_hb5,cn5)