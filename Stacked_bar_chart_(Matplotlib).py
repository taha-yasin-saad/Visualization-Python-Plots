import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data for demonstration
x = np.arange(5)
revenue = [20, 25, 30, 35, 40]
earning = [10, 15, 20, 25, 30]
width = 0.35
year = [2011, 2012, 2013, 2014, 2015]

def billions(x, pos):
    return '$%1.0fb' % (x * 1)

formatter = FuncFormatter(billions)

fig, ax = plt.subplots()
p1 = ax.bar(x, revenue, width)
p2 = ax.bar(x, earning, width, bottom=revenue)

ax.yaxis.set_major_formatter(formatter)
plt.title('MSFT - Annual Data \n (2011-2015)')
plt.xticks(x, year)
plt.ylim(0, 180)
plt.ylabel('Billions of US $')
plt.legend((p1[0], p2[0]), ('Revenue', 'Earning'))
plt.grid(False)
plt.tight_layout()
plt.show()