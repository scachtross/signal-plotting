from scipy import integrate as ng
import numpy as np


# DT Inner Product
n= np.arange(0, 10)
x_dt= np.cos(2 *np.pi *n/10)
y_dt= np.sin(2 *np.pi *n/10)
inner_dt= np.sum(x_dt *np.conj( y_dt ))
#inner_product = np.dot(x_dt, y_dt)  # Alternative
print(f'The Inner product of the 2 DT signals is: {inner_dt}')


# CT Inner Product
t= np.arange(0 , 1 , 0.01)
x_ct= np.sin(2 *np.pi* t)
y_ct= np.cos(2 *np.pi* t)
inner_ct= ng.simpson(x_ct *np.conj( y_ct ), t )
print(f'The inner product of the 2 CT signals is {inner_ct}')

# Energy
energy_x_dt= np.sum(np.abs( x_dt )**2)
print(f'The enery of the signal x[n] is {energy_x_dt}')

energy_y_dt= np.sum(np.abs( y_dt )**2)
print(f'The energy of the signal y[n] is {energy_y_dt}')

energy_x_ct= ng.simpson( np.abs( x_ct )**2, t)
print(f'The energy of the signal x(t) is {energy_x_ct}')

energy_y_ct= ng.simpson(np.abs( y_ct )**2, t)
print(f'The energy of the signal y(t) is {energy_y_ct}')

#calculate the power of x(t) which is given by P = (1/T) * integral of [sin2πt^2] dt from 0 to T 
#period of sin(2πt)
T = 1 

# Compute the power
power, _ = ng.quad(lambda t: np.sin(2 * np.pi * t)**2, 0, T)
print(f"Power of the signal: {power}")


# Cauchy - Schwarz Inequality
cauchy_schwarz_dt= abs(inner_dt ) <= np.sqrt(energy_x_dt *energy_y_dt)
cauchy_schwarz_ct= abs(inner_ct ) <= np.sqrt(energy_x_ct *energy_y_ct)
