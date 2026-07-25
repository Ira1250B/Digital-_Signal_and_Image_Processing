import numpy as np
import matplotlib.pyplot as plt

def linear_convolution(signal1,signal2):
    lin_conv=np.convolve(signal1,signal2,mode="full")
    return lin_conv
def circular_convolution(signal1,signal2):
    if(len(signal1)>len(signal2)):
        sig_length=len(signal1)
    else:
        sig_length=len(signal2)
    fft_signal1=np.fft.fft(signal1,sig_length)
    fft_signal2=np.fft.fft(signal2,sig_length)
    circu_convo=np.fft.ifft(fft_signal1 * fft_signal2)
    return circu_convo
signal1=[1,2,3,4,5]
signal2=[2,4,6,8,10]
linear=linear_convolution(signal1,signal2)
circular=circular_convolution(signal1,signal2)
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.stem(linear)
plt.title("Linear Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.subplot(2,1,2)
plt.stem(circular)
plt.title("circular Convolution")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

            