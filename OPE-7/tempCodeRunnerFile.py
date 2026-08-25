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

