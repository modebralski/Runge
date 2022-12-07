import numpy as np
import matplotlib.pyplot as plt


# Define the function to be interpolated
def f(x):
    return 1 / (1 + 25 * x ** 2)


# Define the interpolation points
x = np.linspace(-1, 1, 10)

# Evaluate the function at the interpolation points
y = f(x)

# Create a set of evenly spaced points for plotting the interpolated function
x_plot = np.linspace(-1, 1, 100)

# Use polynomial interpolation to interpolate the function at the plot points
y_plot = np.polyval(np.polyfit(x, y, len(x) - 1), x_plot)

# Compute the error between the interpolated function and the original function at each plot point
error = np.abs(y_plot - f(x_plot))

# Plot the original function, the interpolated function, and the error
plt.plot(x_plot, f(x_plot), label='Original function')
plt.plot(x_plot, y_plot, label='Interpolated function')
plt.plot(x_plot, error, label='Error')
plt.legend()
plt.show()
print(max(error))
