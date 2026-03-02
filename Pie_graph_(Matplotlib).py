import matplotlib.pyplot as plt
import random

# Generate random data for electricity usage in Riyadh, Jeddah, and Alkhobar
cities = ['Riyadh', 'Jeddah', 'Alkhobar']
usage = [random.randint(50, 200) for _ in cities]

plt.figure(figsize=(6, 6))
plt.pie(
    usage,
    labels=['', '', ''],
    autopct='%1.1f%%',
    startangle=140,
    colors=['blue', 'green', 'orange']
)
plt.title('Electricity Usage Distribution (Random Data)')
plt.axis('equal')

plt.legend(cities, title="Cities", loc="upper right")
plt.show()