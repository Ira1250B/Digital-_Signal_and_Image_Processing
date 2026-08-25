import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread(r"C:\Users\bhoga\Downloads\Picture1.png")
img2=cv2.imread(r"C:\Users\bhoga\Downloads\Picture2.png")
img3=cv2.imread(r"C:\Users\bhoga\Downloads\Picture3.png")
img4=cv2.imread(r"C:\Users\bhoga\Downloads\Picture4.png")
img5=cv2.imread(r"C:\Users\bhoga\Downloads\Picture5.png")

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
gray4=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
gray5=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)

def negative_transform(image):
    
    ng_tr_img=255-image
    return ng_tr_img
n_img1=negative_transform(gray1)
n_img2=negative_transform(gray2)
n_img3=negative_transform(gray3)
n_img4=negative_transform(gray4)
n_img5=negative_transform(gray5)
def plots(img,n_img):
    plt.figure(figsize=(6,4))
    plt.subplot(1,2,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original Image")
    plt.axis("off")
    plt.subplot(1,2,2)
    plt.imshow(n_img,cmap='gray')
    plt.title("Negative Transformation image")
    plt.axis("Off")
    plt.tight_layout()
    return plt.show()
p1=plots(gray1,n_img1)
p2=plots(gray2,n_img2)
p3=plots(gray3,n_img3)
p4=plots(gray4,n_img4)
p5=plots(gray5,n_img5)

def log_transform(img):
    img=img.astype(np.float32)
    c=255/np.log1p(np.max(img))
    log_tr_img=c*(np.log1p(img))
    log_tr_img=np.array(log_tr_img,dtype=np.uint8)
    return log_tr_img
l_img1=log_transform(gray1)
l_img2=log_transform(gray2)
l_img3=log_transform(gray3)
l_img4=log_transform(gray4)
l_img5=log_transform(gray5)
def log_plots(img,l_img):
     plt.figure(figsize=(6,4))
     plt.subplot(1,2,1)
     plt.imshow(img,cmap='gray')
     plt.title("Original Image")
     plt.axis("off")
     plt.subplot(1,2,2)
     plt.imshow(l_img,cmap='gray')
     plt.title("Log transformed Transformation image")
     plt.axis("Off")
     plt.tight_layout()
     return plt.show()
p6=log_plots(gray1,l_img1)
p7=log_plots(gray2,l_img2)
p8=log_plots(gray3,l_img3)
p9=log_plots(gray4,l_img4)
p10=log_plots(gray5,l_img5)

def inverse_log_transform(img):
    img=img.astype(np.float32)
    c=255/np.log1p(np.max(img))
    inverse_log_trans=(np.exp(img/c))-1
    inverse_log_trans=inverse_log_trans.astype(np.uint8)
    return inverse_log_trans
il_img1=inverse_log_transform(l_img1)
il_img2=inverse_log_transform(l_img2)
il_img3=inverse_log_transform(l_img3)
il_img4=inverse_log_transform(l_img4)
il_img5=inverse_log_transform(l_img5)
def inverse_plot(img,il_img):
    plt.figure(figsize=(6,4))
    plt.subplot(1,2,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original Image")
    plt.axis("off")
    plt.subplot(1,2,2)
    plt.imshow(il_img,cmap='gray')
    plt.title("Inverse Log transformed image")
    plt.axis("Off")
    plt.tight_layout()
    return plt.show()
plt11=inverse_plot(gray1,il_img1)
plt12=inverse_plot(gray2,il_img2)
plt13=inverse_plot(gray3,il_img3)
plt14=inverse_plot(gray4,il_img4)
plt15=inverse_plot(gray5,il_img5)

# first perform normalization for each image.
# gamma fixied as 2
gamma=2
def gamma_corrected_img(img):
    threshold=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
    n_img=img/255.0
    gamma_corrected_img=np.pow(n_img,gamma)
    return (gamma_corrected_img)*255
g1=gamma_corrected_img(gray1)
g2=gamma_corrected_img(gray2)
g3=gamma_corrected_img(gray3)
g4=gamma_corrected_img(gray4)
g5=gamma_corrected_img(gray5)

def gm_plot(img,g_img):
     plt.figure(figsize=(6,4))
     plt.subplot(1,2,1)
     plt.imshow(img,cmap='gray')
     plt.title("Original Image")
     plt.axis("off")
     plt.subplot(1,2,2)
     plt.imshow(g_img,cmap='gray')
     plt.title("Power Log transformed image")
     plt.axis("Off")
     plt.tight_layout()
     return plt.show()
p16=gm_plot(gray1,g1)
p17=gm_plot(gray2,g2)
p18=gm_plot(gray3,g3)
p19=gm_plot(gray4,g4)
p20=gm_plot(gray5,g5)

