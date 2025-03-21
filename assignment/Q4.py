"""
Use PYTHON  to plot x(t) = ∑(k=1 to k=10) cos (2πkt) over a suitable range of t.
"""

import numpy as np
from matplotlib import pyplot as plt

# define the time values using the arange() from 0 to 10 with a step-size of 0.01
time = np.arange(0,10,0.01)
#print(time)


#define the function x(t)
# initialize a list of the values of x with zeros
x = np.zeros_like(time)
#print(x)

#compute the sumation of x for k=1 to k=10
for k in range(1,11):
    x += np.cos(2*np.pi*k*time)

#plot
plt.figure(figsize=(10,6))
plt.plot(time, x)
plt.grid(True)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()