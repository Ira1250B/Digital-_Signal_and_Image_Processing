import numpy as np
import matplotlib.pyplot as plt

def cross_correlation(sig1,sig2):
    cross_corre=np.correlate(sig1,sig2,mode="full")
    return cross_corre
def auto_correlation(sig1):
    auto_corre=np.correlate(sig1,sig1,mode="full")
    return auto_corre
sig1=np.array([1,2,3,4,5])
sig2=np.array([0,2,4,6,8,10])

#cross correlation
cross=cross_correlation(sig1,sig2)
#auto correlation
auto=auto_correlation(sig1)
#plot both
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.stem(cross)
plt.xlabel("Time Lag")
plt.ylabel("Magnitude")
plt.title("Cross Correlation")
plt.subplot(1,2,2)
plt.stem(auto)
plt.xlabel("Time lag")
plt.ylabel("Magnitude")
plt.title("Auto Correlation")
plt.show()