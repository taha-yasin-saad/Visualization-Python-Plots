import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.boxplot(
    data=diamonds,
    x="cut",
    y="price",
    order=["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

plt.xlabel("Cut")
plt.ylabel("Price ($)")
plt.title("Distribution of Diamond Prices by Cut Quality")
plt.show()