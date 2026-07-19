import numpy as np
import matplotlib.pyplot as plt

def unit_impulse_train(signal_length,period):
    impulse_length=np.zeros(signal_length)
    for n in range(signal_length):
           if(n%2==0):
               impulse_length[n]=3
           else:
               impulse_length[n]=2
    return impulse_length
signal_length=10
period=2
impulse_signal=unit_impulse_train(signal_length,period)
plt.stem(impulse_signal)
plt.title("x[n]")
plt.show()