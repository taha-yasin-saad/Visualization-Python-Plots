import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plot = sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plot.set_axis_labels('Total Bill ($)', 'Tip ($)')
plot.fig.suptitle('Hexbin Plot of Total Bill vs. Tip', y=1.02)

# Add a colorbar
cbar_ax = plot.fig.add_axes([0.85, 0.15, 0.02, 0.6])
plt.colorbar(cax=cbar_ax).set_label('Density')

plt.show()