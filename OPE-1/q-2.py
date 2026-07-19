import numpy as np
import matplotlib.pyplot as plt

def simulate_function(time):

    y = np.zeros_like(time)

    y[time == 0] = 1
    y[(time >=0) & (time<2) ] = 2
    y[(time==2)&(time<3)] = 3
    y[(time == 3) & (time<4)] = 3
    y[(time >=4)&(time<5)] = 2
    y[time == 5] = 1

    return y

time = np.linspace(-2,7,6)

function_values = simulate_function(time)

plt.plot(time,function_values)
plt.grid(True)
plt.show()