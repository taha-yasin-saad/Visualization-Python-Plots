import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

mean = 50
std_dev = 10
data_size = 1000
data = np.random.normal(mean, std_dev, data_size)

plt.figure(figsize=(8, 6))
sns.histplot(data, bins=30, kde=True, color='blue', label='Histogram')

plt.title('Distribution of Job Applications')
plt.xlabel('Job position')
plt.ylabel('Frequency')
plt.legend()
plt.show()