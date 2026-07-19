import numpy as np
import matplotlib.pyplot as plt
#x[n]=δ(n)+3δ(n−1)+5δ(n+1)
def funcn(time):
    y=np.zeros_like(time)
    y[time == 0]=1
    y[time == 1]+=3
    y[time == -1]+=5
    return y
time=np.arange(-9,10)
signal=funcn(time)
plt.stem(time,signal)
plt.title("x[n]=δ(n)+3δ(n−1)+5δ(n+1)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()