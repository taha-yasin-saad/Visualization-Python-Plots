import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

sns.scatterplot(
    x="sepal_length",
    y="sepal_width",
    data=iris,
    hue="species",
    palette="Set1"
)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Dataset Scatter Plot (Sepal Length vs. Sepal Width)')
plt.legend(title="Species")
plt.show()