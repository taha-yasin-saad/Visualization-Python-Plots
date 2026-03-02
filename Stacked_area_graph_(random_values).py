import matplotlib.pyplot as plt
import numpy as np
import random

# Generate random data for electricity usage in Riyadh, Jeddah, and Alkhobar
years = np.arange(2010, 2021)
riyadh_usage = [random.randint(50, 200) for _ in years]
jeddah_usage = [random.randint(50, 200) for _ in years]
alkhobar_usage = [random.randint(50, 200) for _ in years]

# Create a stacked area graph
plt.figure(figsize=(10, 6))
plt.stackplot(
    years,
    riyadh_usage,
    jeddah_usage,
    alkhobar_usage,
    labels=['Riyadh', 'Jeddah', 'Alkhobar'],
    colors=['blue', 'green', 'orange']
)

plt.title('Random Electricity Usage in Saudi Cities (2010-2020)')
plt.xlabel('Year')
plt.ylabel('Usage (in kWh)')
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()