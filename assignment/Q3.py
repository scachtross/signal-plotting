"""
Use PYTHON to plot x(t) = cos (t) sin (20t) over a suitable range of t
"""

import numpy as np
from matplotlib import pyplot as plt

# define the time values using the arange() from 0 to 10 with a step-size of 0.01
#time = np.arange(0,10,0.01)

#define the time values using linspace() from 0 to 2π
time = np.linspace(0, 2 * np.pi, 1000) 

#define the function x(t)
x = np.cos(time) * np.sin(20 * time)

#plot
plt.figure(figsize=(10,6))
plt.plot(time,x,color='red')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.grid(True)
plt.show()