"plot the signal f(t) = sin (2π10t + π/6)"

import numpy as np
from matplotlib import pyplot as plt

time = np.arange(0,0.2,0.001)
f = np.sin(2*np.pi*10*time + np.pi/6)

#plt.figure(figsize=(10,6))
plt.plot(time,f)
plt.xlabel('time')
plt.ylabel('f(t)')
plt.show()