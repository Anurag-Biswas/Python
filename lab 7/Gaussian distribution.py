import numpy as np
import matplotlib.pyplot as plt

# Gaussian distribution function
def gaussian(x, mean, variance):
    return (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-((x - mean) ** 2) / (2 * variance))

# Generate a range of x values
x = np.linspace(-10, 10, 400)

# Define different means and variances to plot
means = [0, -2, 2]
variances = [0.5, 1, 2]

# Plotting the Gaussian distributions for different means and variances
plt.figure(figsize=(10, 6))

for mean in means:
    for variance in variances:
        y = gaussian(x, mean, variance)
        label = f"mean={mean}, variance={variance}"
        plt.plot(x, y, label=label)

# Adding plot details
plt.title('Effect of Varying Mean and Variance on Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
