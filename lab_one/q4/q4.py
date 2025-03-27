import numpy as np

# Linearity and Time - Invariance ( CT )
t = np.arange(0, 5, 0.01)
x1 = np.sin(2* np.pi* t)
x2 = np.cos(2* np.pi* t)
y1 = x1 + np.roll(x1, 100)
y2 = x2 + np.roll(x2, 100)
y3 = x1 + x2 + np.roll(x1 + x2, 100)
is_linear_ct = np.allclose(y1 + y2, y3)
print(f'Linearity(CT system): {is_linear_ct}')

# Linearity and Time - Invariance ( DT )
n= np.arange(0 , 51)
x1_dt= np.sin (2* np.pi* n/10)
x2_dt= np.cos (2* np.pi* n/10)
y1_dt= x1_dt + np.roll(x1_dt, 10)
y2_dt= x2_dt + np.roll(x2_dt, 10)
y3_dt= x1_dt + x2_dt + np.roll(x1_dt + x2_dt, 10)
is_linear_dt= np.allclose(y1_dt + y2_dt, y3_dt )
print(f'Linearity(DT system): {is_linear_dt}')

# Causality and Stability ( CT )
is_causal_ct = np.all( t >= 0) # System is causal if t >= 0
x_ct = np.sin(2* np.pi* t)
energy_ct = np.sum(x_ct**2)
is_stable_ct = energy_ct < np.inf # System is stable if energy is finite
print(f'causality(CT system): {is_causal_ct}')
print(f'stability(CT system): {is_stable_ct}')

# Causality and Stability ( DT )
is_causal_dt = np.all ( n >= 0) # System is causal if n >= 0
x_dt = np.sin(2* np.pi* n/10)
energy_dt = np.sum(x_dt**2)
is_stable_dt = energy_dt < np.inf # System is stable if energy is finite
print(f'causality(DT system): {is_causal_dt}')
print(f'stability(DT system): {is_stable_dt}')
