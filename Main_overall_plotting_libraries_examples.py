"""
Chapter 2 - Plotting Libraries (Matplotlib & Seaborn)
Compiled code examples from the lecture slides by Dr. Ali Louati.

How to run:
  1) Create & activate a virtual environment (optional)
  2) Install dependencies:
        pip install matplotlib seaborn numpy
  3) Run:
        python chapter2_plotting_libraries_examples.py

Note:
- Some examples use seaborn built-in datasets (iris, titanic, tips, diamonds).
  Those are fetched by seaborn; if you're offline, dataset loading may fail.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Matplotlib examples
# -----------------------------

def stacked_bar_chart_msft():
    """Stacked bar chart: MSFT revenue vs earning (sample data)."""
    from matplotlib.ticker import FuncFormatter

    x = np.arange(5)
    revenue = [20, 25, 30, 35, 40]
    earning = [10, 15, 20, 25, 30]
    width = 0.35
    year = [2011, 2012, 2013, 2014, 2015]

    def billions(val, pos):
        return '$%1.0fb' % (val * 1)

    formatter = FuncFormatter(billions)

    fig, ax = plt.subplots()
    p1 = ax.bar(x, revenue, width)
    p2 = ax.bar(x, earning, width, bottom=revenue)

    ax.yaxis.set_major_formatter(formatter)
    plt.title('MSFT - Annual Data \n (2011-2015)')
    plt.xticks(x, year)
    plt.ylim(0, 180)
    plt.ylabel('Billions of US $')
    plt.legend((p1[0], p2[0]), ('Revenue', 'Earning'))
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def grouped_bar_chart_msft():
    """Grouped bar chart: MSFT revenue vs earning (sample data)."""
    from matplotlib.ticker import FuncFormatter

    x = np.arange(5)
    revenue = [20, 25, 30, 35, 40]
    earning = [10, 15, 20, 25, 30]
    bar_width = 0.35
    year = [2011, 2012, 2013, 2014, 2015]

    def billions(val, pos):
        return '$%1.0fb' % (val * 1)

    formatter = FuncFormatter(billions)

    fig, ax = plt.subplots()
    bar1 = ax.bar(x - bar_width / 2, revenue, bar_width, label='Revenue')
    bar2 = ax.bar(x + bar_width / 2, earning, bar_width, label='Earning')

    ax.yaxis.set_major_formatter(formatter)
    plt.title('MSFT - Annual Data \n (2011-2015)')
    plt.xticks(x, year)
    plt.ylabel('Billions of US $')
    plt.legend()
    plt.show()


def line_graph_riyadh_random():
    """Line graph: Electricity usage in Riyadh (random)."""
    years = list(range(2010, 2021))
    usage = [random.randint(100, 200) for _ in years]  # kWh

    plt.figure(figsize=(10, 6))
    plt.plot(years, usage, marker='o', linestyle='-', color='b', label='Electricity Usage')

    plt.title('Electricity Usage in Riyadh (2010-2020)')
    plt.xlabel('Year')
    plt.ylabel('Usage (in kWh)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def stacked_area_predefined():
    """Stacked area graph: Electricity usage in Saudi cities (predefined values)."""
    years = np.arange(2010, 2021)
    riyadh_usage = np.array([100, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155])
    jeddah_usage = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
    alkhobar_usage = np.array([70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120])

    plt.figure(figsize=(10, 6))
    plt.stackplot(
        years,
        riyadh_usage,
        jeddah_usage,
        alkhobar_usage,
        labels=['Riyadh', 'Jeddah', 'Alkhobar'],
        colors=['blue', 'green', 'orange']
    )

    plt.title('Electricity Usage in Saudi Cities (2010-2020)')
    plt.xlabel('Year')
    plt.ylabel('Usage (in kWh)')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


def stacked_area_random():
    """Stacked area graph: Random electricity usage in Saudi cities."""
    years = np.arange(2010, 2021)
    riyadh_usage = [random.randint(50, 200) for _ in years]
    jeddah_usage = [random.randint(50, 200) for _ in years]
    alkhobar_usage = [random.randint(50, 200) for _ in years]

    plt.figure(figsize=(10, 6))
    plt.stackplot(
        years,
        riyadh_usage,
        jeddah_usage,
        alkhobar_usage,
        labels=['Riyadh', 'Jeddah', 'Alkhobar'],
        colors=['blue', 'green', 'orange']
    )

    plt.title('Random Electricity Usage in Saudi Cities (2010-2020)')
    plt.xlabel('Year')
    plt.ylabel('Usage (in kWh)')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


def pie_chart_random():
    """Pie chart: Electricity usage distribution (random)."""
    cities = ['Riyadh', 'Jeddah', 'Alkhobar']
    usage = [random.randint(50, 200) for _ in cities]

    plt.figure(figsize=(6, 6))
    plt.pie(
        usage,
        labels=['', '', ''],
        autopct='%1.1f%%',
        startangle=140,
        colors=['blue', 'green', 'orange']
    )
    plt.title('Electricity Usage Distribution (Random Data)')
    plt.axis('equal')
    plt.legend(cities, title="Cities", loc="upper right")
    plt.show()


def histogram_predefined():
    """Histogram: Job applications (predefined values)."""
    job_applications = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

    plt.figure(figsize=(8, 6))
    plt.hist(job_applications, bins=10, edgecolor='black', alpha=0.7)

    plt.title('Distribution of Job Applications')
    plt.xlabel('Number of Applications')
    plt.ylabel('Frequency')
    plt.show()


def histogram_normal_distribution():
    """Histogram: Random normal distribution dataset."""
    mean = 50
    std_dev = 10
    data_size = 1000

    data = np.random.normal(mean, std_dev, data_size)

    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, density=True, edgecolor='black', alpha=0.7)

    plt.title('Distribution of Job Applications')
    plt.xlabel('Job position')
    plt.ylabel('Frequency')
    plt.show()


# -----------------------------
# Seaborn examples
# -----------------------------

def seaborn_hist_kde_mean_line():
    """Seaborn: Histogram + KDE + mean line (synthetic normal data)."""
    import seaborn as sns

    mean = 50
    std_dev = 10
    data_size = 1000
    data = np.random.normal(mean, std_dev, data_size)

    plt.figure(figsize=(8, 6))
    sns.histplot(data, bins=30, kde=False, color='lightblue', label='Histogram')
    sns.kdeplot(data, color='blue', label='Density Plot')
    plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=2, label='Mean')

    plt.title('Distribution of Job Applications')
    plt.xlabel('Job position')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


def seaborn_density_plot():
    """Seaborn: Density plot (KDE)."""
    import seaborn as sns

    mean = 50
    std_dev = 10
    data_size = 1000
    data = np.random.normal(mean, std_dev, data_size)

    plt.figure(figsize=(8, 6))
    # shade=True is deprecated in newer seaborn; fill=True is preferred, but we keep the slide's intent.
    try:
        sns.kdeplot(data, shade=True, color='blue')
    except TypeError:
        sns.kdeplot(data, fill=True, color='blue')

    plt.title('Distribution of Job Applications')
    plt.xlabel('Job position')
    plt.ylabel('Frequency')
    plt.show()


def seaborn_density_with_hist():
    """Seaborn: Histogram with KDE overlay."""
    import seaborn as sns

    mean = 50
    std_dev = 10
    data_size = 1000
    data = np.random.normal(mean, std_dev, data_size)

    plt.figure(figsize=(8, 6))
    sns.histplot(data, bins=30, kde=True, color='blue', label='Histogram')

    plt.title('Distribution of Job Applications')
    plt.xlabel('Job position')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()


def iris_histograms_density_all_features():
    """Iris dataset: Histograms + KDE for sepal/petal length/width by species."""
    import seaborn as sns

    iris = sns.load_dataset("iris")
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 2, 1)
    sns.histplot(iris[iris["species"] == "setosa"]["sepal_length"], kde=True, color="blue", label="setosa", bins=20)
    sns.histplot(iris[iris["species"] == "versicolor"]["sepal_length"], kde=True, color="green", label="versicolor", bins=20)
    sns.histplot(iris[iris["species"] == "virginica"]["sepal_length"], kde=True, color="red", label="virginica", bins=20)
    plt.xlabel("Sepal Length (cm)")
    plt.title("Sepal Length Distribution")
    plt.legend()

    plt.subplot(2, 2, 2)
    sns.histplot(iris[iris["species"] == "setosa"]["sepal_width"], kde=True, color="blue", label="setosa", bins=20)
    sns.histplot(iris[iris["species"] == "versicolor"]["sepal_width"], kde=True, color="green", label="versicolor", bins=20)
    sns.histplot(iris[iris["species"] == "virginica"]["sepal_width"], kde=True, color="red", label="virginica", bins=20)
    plt.xlabel("Sepal Width (cm)")
    plt.title("Sepal Width Distribution")
    plt.legend()

    plt.subplot(2, 2, 3)
    sns.histplot(iris[iris["species"] == "setosa"]["petal_length"], kde=True, color="blue", label="setosa", bins=20)
    sns.histplot(iris[iris["species"] == "versicolor"]["petal_length"], kde=True, color="green", label="versicolor", bins=20)
    sns.histplot(iris[iris["species"] == "virginica"]["petal_length"], kde=True, color="red", label="virginica", bins=20)
    plt.xlabel("Petal Length (cm)")
    plt.title("Petal Length Distribution")
    plt.legend()

    plt.subplot(2, 2, 4)
    sns.histplot(iris[iris["species"] == "setosa"]["petal_width"], kde=True, color="blue", label="setosa", bins=20)
    sns.histplot(iris[iris["species"] == "versicolor"]["petal_width"], kde=True, color="green", label="versicolor", bins=20)
    sns.histplot(iris[iris["species"] == "virginica"]["petal_width"], kde=True, color="red", label="virginica", bins=20)
    plt.xlabel("Petal Width (cm)")
    plt.title("Petal Width Distribution")
    plt.legend()

    plt.tight_layout()
    plt.show()


def scatter_random_matplotlib():
    """Scatter plot example: random points (Matplotlib)."""
    np.random.seed(0)
    x = np.random.rand(50)
    y = np.random.rand(50)

    plt.scatter(x, y, label='Random Data', color='b', marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot Example')
    plt.legend()
    plt.show()


def iris_scatter_petal_hue_sepal_length():
    """Iris scatter: petal_length vs petal_width, hue=sepal_length (Seaborn)."""
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


def iris_scatter_sepal_hue_species():
    """Iris scatter: sepal_length vs sepal_width, hue=species (Seaborn)."""
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


def titanic_scatter_age_fare_hue_survived():
    """Titanic scatter: age vs fare, hue=survived."""
    import seaborn as sns

    titanic = sns.load_dataset("titanic")
    sns.scatterplot(x="age", y="fare", data=titanic, hue="survived", palette="muted")
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Titanic Dataset Scatter Plot (Age vs. Fare)')
    plt.legend(title="Survived", labels=["No", "Yes"])
    plt.show()


def titanic_scatter_with_regression():
    """Titanic scatter + regression line."""
    import seaborn as sns

    titanic = sns.load_dataset("titanic")
    sns.scatterplot(x="age", y="fare", data=titanic, hue="survived", palette="muted")
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Titanic Dataset Scatter Plot (Age vs. Fare)')
    plt.legend(title="Survived", labels=["No", "Yes"])

    sns.regplot(x="age", y="fare", data=titanic, scatter=False, color='red')
    plt.show()


def tips_scatter_totalbill_tip():
    """Tips dataset scatter: total_bill vs tip, hue=day, style=time."""
    import seaborn as sns

    tips = sns.load_dataset("tips")
    sns.set(style="darkgrid")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Tip ($)")
    plt.title("Total Bill vs. Tip Amount by Day and Time")
    plt.legend(title="Day")
    plt.show()


def diamonds_scatter_carat_price():
    """Diamonds dataset scatter: carat vs price, hue=cut."""
    import seaborn as sns

    diamonds = sns.load_dataset("diamonds")
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=diamonds, x="carat", y="price", hue="cut")
    plt.xlabel("Carat")
    plt.ylabel("Price ($)")
    plt.title("Carat vs. Price of Diamonds by Cut")
    plt.legend(title="Cut")
    plt.show()


def tips_jointplot_scatter():
    """Joint plot (Tips): scatter + marginal distributions."""
    import seaborn as sns

    tips = sns.load_dataset("tips")
    sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
    plt.show()


def tips_jointplot_reg():
    """Joint plot (Tips): regression + marginals."""
    import seaborn as sns

    tips = sns.load_dataset("tips")
    sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
    plt.show()


def tips_hexbin_plot():
    """Hexbin joint plot (Tips)."""
    import seaborn as sns

    tips = sns.load_dataset("tips")
    plot = sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
    plot.set_axis_labels('Total Bill ($)', 'Tip ($)')
    plot.fig.suptitle('Hexbin Plot of Total Bill vs. Tip', y=1.02)

    cbar_ax = plot.fig.add_axes([0.85, 0.15, 0.02, 0.6])
    plt.colorbar(cax=cbar_ax).set_label('Density')
    plt.show()


def tips_2d_density_plot():
    """2D density plot (Tips)."""
    import seaborn as sns

    tips = sns.load_dataset("tips")
    sns.kdeplot(data=tips, x="total_bill", y="tip", cmap="viridis", fill=True)
    plt.xlabel('Total Bill ($)')
    plt.ylabel('Tip ($)')
    plt.title('2D Density Plot of Total Bill vs. Tip')
    plt.show()


def tips_2d_density_and_joint_kde():
    """2D density plot + jointplot KDE (Tips)."""
    import seaborn as sns

    tips = sns.load_dataset("tips")

    sns.kdeplot(data=tips, x="total_bill", y="tip", cmap="viridis", fill=True)
    plt.xlabel('Total Bill ($)')
    plt.ylabel('Tip ($)')
    plt.title('2D Density Plot of Total Bill vs. Tip')
    plt.show()

    sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde", color="b")
    plt.show()


def diamonds_boxplot_price_by_cut():
    """Box plot (Diamonds): price distribution by cut."""
    import seaborn as sns

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


def tips_boxplot_tip_by_day():
    """Box plot (Tips): tip distribution by day."""
    import seaborn as sns

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


# -----------------------------
# Run all examples (optional)
# -----------------------------
def run_all():
    """Run all examples in the same order as the lecture."""
    stacked_bar_chart_msft()
    grouped_bar_chart_msft()
    line_graph_riyadh_random()
    stacked_area_predefined()
    stacked_area_random()
    pie_chart_random()
    histogram_predefined()
    histogram_normal_distribution()

    seaborn_hist_kde_mean_line()
    seaborn_density_plot()
    seaborn_density_with_hist()

    iris_histograms_density_all_features()

    scatter_random_matplotlib()
    iris_scatter_petal_hue_sepal_length()
    iris_scatter_sepal_hue_species()

    titanic_scatter_age_fare_hue_survived()
    titanic_scatter_with_regression()

    tips_scatter_totalbill_tip()
    diamonds_scatter_carat_price()

    tips_jointplot_scatter()
    tips_jointplot_reg()
    tips_hexbin_plot()

    tips_2d_density_plot()
    tips_2d_density_and_joint_kde()

    diamonds_boxplot_price_by_cut()
    tips_boxplot_tip_by_day()


if __name__ == "__main__":
    # Choose ONE:
    # 1) run_all()  # runs everything (many figures)
    # 2) Run specific functions by uncommenting them below.

    # run_all()

    stacked_bar_chart_msft()
    # grouped_bar_chart_msft()
    # line_graph_riyadh_random()
    # stacked_area_predefined()
    # stacked_area_random()
    # pie_chart_random()
    # histogram_predefined()
    # histogram_normal_distribution()

    # seaborn_hist_kde_mean_line()
    # seaborn_density_plot()
    # seaborn_density_with_hist()
    # iris_histograms_density_all_features()
    # scatter_random_matplotlib()
    # iris_scatter_petal_hue_sepal_length()
    # iris_scatter_sepal_hue_species()
    # titanic_scatter_age_fare_hue_survived()
    # titanic_scatter_with_regression()
    # tips_scatter_totalbill_tip()
    # diamonds_scatter_carat_price()
    # tips_jointplot_scatter()
    # tips_jointplot_reg()
    # tips_hexbin_plot()
    # tips_2d_density_plot()
    # tips_2d_density_and_joint_kde()
    # diamonds_boxplot_price_by_cut()
    # tips_boxplot_tip_by_day()
