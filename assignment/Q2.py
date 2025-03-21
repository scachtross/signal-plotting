"""
Use PYTHON to plot the function x(t) = t sin(2πt) over 0 <= t <= 10 using 501 equally
spaced points. What is the maximum value of x(t) over this range of t?
"""

import numpy as np
from matplotlib import pyplot as plt

# no of points
sample_size = 501

#time values
time_values = np.linspace(0,10,sample_size)
#print(time_values)

#define our function x(t) = t sin(2*pi*t)
x = time_values * np.sin(2*np.pi*time_values)

#print the maximmum value of x(t)
print(f"maximum value of x(t) is {max(x)}")

#plot
plt.figure(figsize=(6,6))
plt.plot(time_values,x,color='red')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.grid(True)
plt.axis('equal')
plt.show()