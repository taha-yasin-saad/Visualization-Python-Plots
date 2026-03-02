import matplotlib.pyplot as plt
import random

# Generate random data for electricity usage in Riyadh
years = list(range(2010, 2021))
usage = [random.randint(100, 200) for _ in years]  # Random values between 100 and 200 kWh

# Create a line graph
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(years, usage, marker='o', linestyle='-', color='b', label='Electricity Usage')

plt.title('Electricity Usage in Riyadh (2010-2020)')
plt.xlabel('Year')
plt.ylabel('Usage (in kWh)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()