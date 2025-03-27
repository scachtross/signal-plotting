import numpy as np
from matplotlib import pyplot as plt

# CT Signals
t = np . arange( -5 , 5 , 0.01)
sgn_t = np.sign( t )
rect_t = np . where (( t >= -0.5)&( t <= 0.5), 1 , 0)

# Students complete the following :
tri_t = np.maximum(0, 1 - np.abs(t))
sinc_t = np.where(t == 0, 1, np.sin(np.pi*t)/(np.pi*t))


#plotting the CT signals
plt.figure(figsize=(10,6))

#signum function plot
plt.subplot(2 , 2 , 1)
plt.plot(t , sgn_t )
plt.title('Signum Function')

#Rectangular function plot
plt.subplot(2 , 2 , 2)
plt.plot(t , rect_t )
plt.title ('Rectangular Function')

#Triangular function plot
plt.subplot (2 , 2 , 3)
plt.plot (t, tri_t)
plt.title('Triangular Function')

#sinc function plot
plt.subplot(2 , 2 , 4)
plt.plot(t, sinc_t )
plt.title('Sinc Function')

plt.show()
