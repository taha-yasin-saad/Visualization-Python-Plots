import matplotlib.pyplot as plt
import numpy as np

# Sample data for electricity usage in Riyadh, Jeddah, and Alkhobar (replace with actual data)
years = np.arange(2010, 2021)
riyadh_usage = np.array([100, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155])
jeddah_usage = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
alkhobar_usage = np.array([70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120])

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

plt.title('Electricity Usage in Saudi Cities (2010-2020)')
plt.xlabel('Year')
plt.ylabel('Usage (in kWh)')
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()