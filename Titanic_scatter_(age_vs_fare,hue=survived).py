import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

sns.scatterplot(x="age", y="fare", data=titanic, hue="survived", palette="muted")
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Titanic Dataset Scatter Plot (Age vs. Fare)')
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()