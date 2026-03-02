import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, label='Random Data', color='b', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.legend()
plt.show()