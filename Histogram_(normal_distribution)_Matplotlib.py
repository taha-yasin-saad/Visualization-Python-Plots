import matplotlib.pyplot as plt
import numpy as np

# Generate a random dataset following a normal distribution
mean = 50
std_dev = 10
data_size = 1000

data = np.random.normal(mean, std_dev, data_size)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, edgecolor='black', alpha=0.7)

plt.title('Distribution of Job Applications')
plt.xlabel('Job position')
plt.ylabel('Frequency')
plt.show()