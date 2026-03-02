import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
plt.show()