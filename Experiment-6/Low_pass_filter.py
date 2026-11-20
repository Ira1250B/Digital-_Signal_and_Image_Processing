import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

fs = 10000
N = 31

lowpass = firwin(N, 3000, fs=fs, pass_zero='lowpass')
highpass = firwin(N, 3000, fs=fs, pass_zero='highpass')
bandpass = firwin(N, [3000, 4000], fs=fs, pass_zero='bandpass')
bandstop = firwin(N, [3000, 4000], fs=fs, pass_zero='bandstop')

filters = [lowpass, highpass, bandpass, bandstop]

titles = [
    'FIR Low Pass Filter',
    'FIR High Pass Filter',
    'FIR Band Pass Filter',
    'FIR Band Stop Filter'
]

plt.figure(figsize=(12, 8))

for i in range(4):
    w, h = freqz(filters[i], worN=1024, fs=fs)

    plt.subplot(2, 2, i + 1)
    plt.plot(w, 20 * np.log10(np.maximum(abs(h), 1e-10)))
    plt.title(titles[i])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)

plt.tight_layout()
plt.show()