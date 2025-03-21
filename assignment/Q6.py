"""use python to plot x(t) = sin(2π5t) for 0<=t<=2π"""

import numpy as np
from matplotlib import pyplot as plt

#define the values of t
time = np.arange(0,1,0.01)

# define the values of x
x = np.sin(2 * np.pi*5*time)

#plot
plt.figure(figsize=(10,6))
plt.plot(time,x)
plt.grid(True)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()