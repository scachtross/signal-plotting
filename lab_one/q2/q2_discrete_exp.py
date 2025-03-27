from matplotlib import pyplot as plt
import numpy as np

N = 10
n = np . arange (0 , N )
k = 2
l = N - k

# Students complete the following :
exp_k = np.exp(1j*(2*np.pi*k*n/N))
exp_l = np.exp(1j*(2*np.pi*l*n/N))

#plotting
plt.figure(figsize=(10,8))
plt.subplot(2 , 1 , 1)
plt.stem(n, np.real( exp_k ))
plt.title(f'Exponential : k = { k }')
plt.subplot(2, 1, 2)
plt.stem(n, np.real(exp_l))
plt.title(f'Exponential : l = { l }')
plt.show()

#Both plots are identical ie the amplitude is the same for each value of n
