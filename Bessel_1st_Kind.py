import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn

# Define a range for x values
x = np.linspace(0, 20, 500)

# Set the orders of Bessel functions
orders = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a plot
plt.figure(figsize=(8, 6))

# Plot Bessel functions for each order
for n in orders:
    plt.plot(x, jn(n, x), label=f'Order {n}')

# Add labels and title
plt.title('Bessel Functions of the First Kind (Jn(x)) for Different Orders')
plt.xlabel('x')
plt.ylabel('Jn(x)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
