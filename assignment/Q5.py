"""Use PYTHON to represent the function x(t) = e ^ -t """

import numpy as np
from matplotlib import pyplot as plt

#define the values of time
time = np.linspace(0, 2*np.pi, 100)

#define the values of x
x = np.exp(time)

#plot
plt.plot(time, x)
plt.grid(True)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()