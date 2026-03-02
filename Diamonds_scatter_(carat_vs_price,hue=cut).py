import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.scatterplot(data=diamonds, x="carat", y="price", hue="cut")

plt.xlabel("Carat")
plt.ylabel("Price ($)")
plt.title("Carat vs. Price of Diamonds by Cut")
plt.legend(title="Cut")
plt.show()