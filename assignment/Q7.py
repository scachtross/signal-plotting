"""use python to plot the signal x(t) = e^t sin(2π5t)"""

import numpy as np
from matplotlib import pyplot as plt

#define the values of time
time = np.arange(0,1,0.01)

#define the function x(t)
x = np.exp(time) * np.sin(2*np.pi*5*time)

#plot
plt.plot(time,x)
plt.grid(True)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()