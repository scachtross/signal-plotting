from matplotlib import pyplot as plt
import numpy as np

n = np.arange(-10 , 11)
delta_n =( n == 0).astype(int)
u_n =( n >= 0).astype( int )
square_n =(( n >= 0) & ( n < 5) ).astype(int)
exp_n=np.exp(1j *np.pi*n/5)
cos_n=np.cos( np.pi*n/5)

#plotting the signals
plt.figure(figsize=(10,8))

#impulse function plot
plt.subplot(2 , 2 , 1)
plt.stem(n , delta_n )
plt.title('Impulse Function')

#step function plot
plt.subplot(2, 2, 2)
plt.stem(n , u_n )
plt.title('Step Function')

#square impulse function plot
plt.subplot(2 , 2 , 3)
plt.stem(n, square_n)
plt.title('SquareImpulse')

#Discrete exponential function plot
plt.subplot(2, 2, 4)
plt.stem(n, np.real(exp_n))
plt.title('Discrete Exponential')

plt.show()