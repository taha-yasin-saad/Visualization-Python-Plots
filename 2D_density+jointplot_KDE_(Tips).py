import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(data=tips, x="total_bill", y="tip", cmap="viridis", fill=True)
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.title('2D Density Plot of Total Bill vs. Tip')
plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde", color="b")
plt.show()