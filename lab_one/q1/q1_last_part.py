'plot the discrete cosine: x[n] = cos(ωn)'

from matplotlib import pyplot as plt
import numpy as np 

n = np.arange(0, 10,0.01)
angular_frequency = np.pi / 5      

# Discrete cosine signal
x = np.cos(angular_frequency*n)

# Plot the signal
plt.figure()
plt.plot(n,x)
plt.title('Discrete Cosine Signal')
plt.xlabel('n)')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()
