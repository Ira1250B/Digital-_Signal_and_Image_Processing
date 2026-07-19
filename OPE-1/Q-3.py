import numpy as np
import matplotlib.pyplot as plt

def conti_step_function(time):
    step_fun=np.zeros_like(time)
    step_fun[time<=-1]=-2
    step_fun[(time>=-1) & (time<=1)]= 2*time[(time>=-1)&(time<=1)]
    step_fun[(time>=2)]=2
    return step_fun
time=np.linspace(-2,2,5)
step_signal=conti_step_function(time)
plt.plot(time,step_signal)
plt.ylim([-3,3])
plt.xlim([-2.5,2.5])
plt.title("x[n]")
plt.show()