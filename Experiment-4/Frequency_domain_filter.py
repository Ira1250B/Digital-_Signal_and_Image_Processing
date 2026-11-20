import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,bilinear,freqz,cheby1

#design butterworth filter
def butterworth(filter_order,cutoff_freq,sampeling_freq):
    analog_b,analog_a=butter(filter_order,cutoff_freq,analog='True',btype='low')
    print(analog_b,analog_a)

    digital_b,digital_a=bilinear(analog_b,analog_a,sampeling_freq)
    return digital_b,digital_a

def cheby_filter(filter_order,cutoff_freq,sampeling_freq,ripple):
    analog_b,analog_a=cheby1(filter_order,ripple,cutoff_freq,analog='True',btype='low')

    digital_d,digital_c=bilinear(analog_b,analog_a,sampeling_freq)
    return digital_b,digital_a

def plot_filter(digital_b,digital_a,sampeling_freq):
    freq,magnitude=freqz(digital_b,digital_a,fs=sampeling_freq)
    plt.figure(figsize=(10,6))
    plt.plot(freq,np.abs(magnitude))
    plt.title('Filter Magnitude Response')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)

    _, impulse_response = freqz(digital_b, digital_a, fs=sampeling_freq, worN=4096)

    plt.figure(figsize=(10, 6))
    plt.plot(impulse_response)
    plt.title('Filter Impulse Response')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.grid(True)
    return plt.show()
   
digital_b,digital_a=butterworth(4,4000,8000)
digital_b,digital_a=cheby_filter(4,4000,8000,0.5)
p=plot_filter(digital_b,digital_a,8000)
p2=plot_filter(digital_b,digital_a,8000)
