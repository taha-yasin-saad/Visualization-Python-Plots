import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.boxplot(
    data=tips,
    x="day",
    y="tip",
    order=["Thur", "Fri", "Sat", "Sun"]
)

plt.xlabel("Day of the Week")
plt.ylabel("Tip Amount ($)")
plt.title("Distribution of Tips by Day of the Week")
plt.show()