import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate a random dataset following a normal distribution
mean = 50
std_dev = 10
data_size = 1000
data = np.random.normal(mean, std_dev, data_size)

plt.figure(figsize=(8, 6))

# Histogram
sns.histplot(data, bins=30, kde=False, color='lightblue', label='Histogram')

# Density plot (KDE)
sns.kdeplot(data, color='blue', label='Density Plot')

# Mean line
plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=2, label='Mean')

plt.title('Distribution of Job Applications')
plt.xlabel('Job position')
plt.ylabel('Frequency')
plt.legend()
plt.show()