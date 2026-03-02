import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset("iris")

sns.set(style="whitegrid")
plt.figure(figsize=(14, 7))

# 1) Sepal Length
plt.subplot(2, 2, 1)
sns.histplot(iris[iris["species"] == "setosa"]["sepal_length"], kde=True, color="blue", label="setosa", bins=20)
sns.histplot(iris[iris["species"] == "versicolor"]["sepal_length"], kde=True, color="green", label="versicolor", bins=20)
sns.histplot(iris[iris["species"] == "virginica"]["sepal_length"], kde=True, color="red", label="virginica", bins=20)
plt.xlabel("Sepal Length (cm)")
plt.title("Sepal Length Distribution")
plt.legend()

# 2) Sepal Width
plt.subplot(2, 2, 2)
sns.histplot(iris[iris["species"] == "setosa"]["sepal_width"], kde=True, color="blue", label="setosa", bins=20)
sns.histplot(iris[iris["species"] == "versicolor"]["sepal_width"], kde=True, color="green", label="versicolor", bins=20)
sns.histplot(iris[iris["species"] == "virginica"]["sepal_width"], kde=True, color="red", label="virginica", bins=20)
plt.xlabel("Sepal Width (cm)")
plt.title("Sepal Width Distribution")
plt.legend()

# 3) Petal Length
plt.subplot(2, 2, 3)
sns.histplot(iris[iris["species"] == "setosa"]["petal_length"], kde=True, color="blue", label="setosa", bins=20)
sns.histplot(iris[iris["species"] == "versicolor"]["petal_length"], kde=True, color="green", label="versicolor", bins=20)
sns.histplot(iris[iris["species"] == "virginica"]["petal_length"], kde=True, color="red", label="virginica", bins=20)
plt.xlabel("Petal Length (cm)")
plt.title("Petal Length Distribution")
plt.legend()

# 4) Petal Width
plt.subplot(2, 2, 4)
sns.histplot(iris[iris["species"] == "setosa"]["petal_width"], kde=True, color="blue", label="setosa", bins=20)
sns.histplot(iris[iris["species"] == "versicolor"]["petal_width"], kde=True, color="green", label="versicolor", bins=20)
sns.histplot(iris[iris["species"] == "virginica"]["petal_width"], kde=True, color="red", label="virginica", bins=20)
plt.xlabel("Petal Width (cm)")
plt.title("Petal Width Distribution")
plt.legend()

plt.tight_layout()
plt.show()