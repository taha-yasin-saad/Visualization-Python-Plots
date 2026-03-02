import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data for demonstration
x = np.arange(5)
revenue = [20, 25, 30, 35, 40]
earning = [10, 15, 20, 25, 30]
bar_width = 0.35
year = [2011, 2012, 2013, 2014, 2015]

def billions(x, pos):
    return '$%1.0fb' % (x * 1)

formatter = FuncFormatter(billions)

fig, ax = plt.subplots()
bar1 = ax.bar(x - bar_width/2, revenue, bar_width, label='Revenue')
bar2 = ax.bar(x + bar_width/2, earning, bar_width, label='Earning')

ax.yaxis.set_major_formatter(formatter)
plt.title('MSFT - Annual Data \n (2011-2015)')
plt.xticks(x, year)
plt.ylabel('Billions of US $')
plt.legend()
plt.show()