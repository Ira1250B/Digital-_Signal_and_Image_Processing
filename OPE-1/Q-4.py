#x[n]=u(n)-u(n-3)-5u(n-7)
import numpy as np
import matplotlib.pyplot as plt

def function(time):
    y=np.zeros_like(time)
    y[time >=0 ]=1
    y[time >=3]-=1
    y[time >=7]-=5
    return y
time=np.linspace(-10,10,100)
signal=function(time)
plt.plot(time,signal)
plt.title("x[n]=u(n)-u(n-3)-5u(n-7)")
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()
