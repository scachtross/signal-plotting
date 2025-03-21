"""
When plotted in the complex plane for !π + ω + π, the function f (ω) =cos(ω) + j0.1 sin(2ω) 
results in a so-called Lissajous figure that resembles a two-bladed propeller.
(a) In PYTHON, create two row vectors fr and fi corresponding to the real and imaginary
portions of f (ω), respectively, over a suitable number N samples of ω. Plot the real
portion against the imaginary portion and verify the figure resembles a propeller.
"""

import numpy as np
from matplotlib import pyplot as plt

#sample size/no of points
sample_size = 1000

#range of values from -pi to pi (angular frequency)
angular_frequency = np.linspace(-np.pi, np.pi, sample_size)
#print(angular_frequency)

#real part function  fr=cos(angular_frequency)
fr = np.cos(angular_frequency)

#imaginary part function  fi = 0.1*sin(2*angular_requency)
fi = 0.1*np.sin(2*angular_frequency)

#plot fi against fr
plt.figure(figsize=(8,8))
plt.plot(fr,fi,color='red')
plt.xlabel('real part')
plt.ylabel('imaginary part')
plt.grid(True)
plt.axis('equal')
plt.show()


