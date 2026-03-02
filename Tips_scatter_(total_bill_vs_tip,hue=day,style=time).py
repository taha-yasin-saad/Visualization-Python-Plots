import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set(style="darkgrid")
plt.figure(figsize=(8, 6))

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")

plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Total Bill vs. Tip Amount by Day and Time")
plt.legend(title="Day")
plt.show()