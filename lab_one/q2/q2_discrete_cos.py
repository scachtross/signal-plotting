from matplotlib import pyplot as plt
import numpy as np

N = 10
n = np . arange (0 , N )
k = 2
l = N - k

# Discrete Cosine
cos_k = np . cos (2 * np . pi * k * n / N )

cos_l = np . cos (2 * np . pi * l * n / N )

#plotting
plt.figure(figsize=(10,8))
plt.subplot (2 , 1 , 1)
plt.stem(n , cos_k )
plt.title(f'Cosine : k = {k }')
plt.subplot (2 , 1 , 2)
plt.stem(n , cos_l )
plt.title(f'Cosine : l = {l }')
plt.show () 

#Both plots are identical ie the amplitude is the same for each value of n