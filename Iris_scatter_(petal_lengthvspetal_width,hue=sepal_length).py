import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

sns.scatterplot(
    x="petal_length",
    y="petal_width",
    hue="sepal_length",
    data=iris,
    palette="viridis"
)

plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Iris Dataset Scatter Plot')
plt.show()