import numpy as np
import matplotlib.pyplot as plt

def fractal_equation(x, a, c, iterations):
    """Iterative application of the fractal equation"""
    for _ in range(iterations):
        x = np.sin(a * x) + c
    return x

# Parameters
a_values = np.linspace(0.5, 2.0, 10000)
c_values = np.linspace(-1.0, 1.0, 10000)
initial_x = 0.1
iterations = 100

# Generate fractal data
fractal_data = np.zeros((len(a_values), len(c_values)))
for i, a in enumerate(a_values):
    for j, c in enumerate(c_values):
        result = fractal_equation(initial_x, a, c, iterations)
        fractal_data[i, j] = result

# Plot
plt.imshow(fractal_data, extent=[c_values.min(), c_values.max(), a_values.min(), a_values.max()], cmap='inferno', aspect='auto')
plt.colorbar(label='Fractal Value')
plt.xlabel('c')
plt.ylabel('a')
plt.title('Fractal Landscape')
plt.show()
